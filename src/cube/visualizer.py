"""
Simple Twizzle Editor wrapper.

Usage (CLI):
    python twizzle_wrapper.py R U R' U'

This will open alpha.twizzle.net/edit with that alg in your default browser.

Usage (from your solver code):
    from twizzle_wrapper import open_in_twizzle

    alg = "R U R' U R U2 R'"
    open_in_twizzle(alg)

https://alpha.twizzle.net/edit/?setup-alg=r+r+L2

"""

from __future__ import annotations

import argparse
import webbrowser
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

CODE_IN_SETUP = False  # if True, need to hit play, else, will arrive preset up with no need to hit play (but notice that the set up moves will look like moves)

# Base Twizzle editor URL (no alg here)
BASE_URL = "https://alpha.twizzle.net/edit/?puzzle=3x3x3"

# Always-prepended code-level setup
CODE_DEFAULT_SETUP = "r2 L2 u2 D2"

# Optional named presets (each is just more moves to append)
PRESETS: dict[str, str] = {
    # example: another orientation or helper sequence
    "checkered": "R2 L2 F2 B2 U2 D2",
    # add more as needed
}


def _normalize_moves(moves: str | None) -> list[str]:
    """
    Normalize a move string into a list of tokens:

    - allow either spaces or '+' as separators
    - collapse extra whitespace
    - convert your `p` notation (Rp -> R') into Twizzle/WCA notation
    """
    if not moves:
        return []

    # Allow "R+U+F" style and normalize to spaces
    cleaned = moves.replace("+", " ")
    raw_tokens = [t for t in cleaned.split() if t]

    return [_convert_p_notation(t) for t in raw_tokens]


def _convert_p_notation(token: str) -> str:
    """
    Convert your internal `p`-prime notation to WCA-style prime for Twizzle.

    Examples:
        "Rp"  -> "R'"
        "Up"  -> "U'"
        "Fp"  -> "F'"
        "R"   -> "R"
        "R2"  -> "R2"
        "R'"  -> "R'"   (already fine)
    """
    # If the token already contains a prime, leave it alone
    if "'" in token:
        return token

    # If it ends with 'p', treat that as prime
    if token.endswith("p") and len(token) > 1:
        return token[:-1] + "'"

    return token


def _join_alg_parts(*parts: str | None) -> str:
    """
    Join multiple move strings into a single alg string, skipping empties.

    Each part is normalized and converted from your `p` notation to WCA.
    """
    tokens: list[str] = []
    for part in parts:
        if not part:
            continue
        tokens.extend(_normalize_moves(part))
    return " ".join(tokens)


def build_twizzle_url(
    user_alg: str | None = None,
    *,
    base_url: str = BASE_URL,
    code_setup: str | None = CODE_DEFAULT_SETUP,
    preset: str | None = None,
    cli_setup: str | None = None,
) -> str:
    """
    Build a Twizzle URL using:

        setup-alg = CODE_DEFAULT_SETUP   (always)
        alg       = preset + moves + setup

    This uses Twizzle exactly as intended:
    - code setup shows in the Setup panel (not as executed moves)
    - actual moves show in the Algorithm panel
    """
    parsed = urlparse(base_url)
    query = parse_qs(parsed.query, keep_blank_values=True)

    if CODE_IN_SETUP:  # see note in reference to this variable above
        # Twizzle-style: setup in its own box, but must hit play
        final_setup = _join_alg_parts(code_setup)
        if final_setup:
            query["setup-alg"] = [final_setup]
        code_for_alg = None
    else:
        # Old-style: treat code setup as part of the main alg (lands at executed state), no need to hit play
        final_setup = None
        code_for_alg = code_setup

    # Resolve preset moves
    preset_moves = PRESETS.get(preset) if preset else None

    # Now build the REAL executable moves (this becomes Twizzle's alg=)
    final_alg = _join_alg_parts(
        code_for_alg,  # only non-None when CODE_IN_SETUP is False
        preset_moves,  # preset now BEFORE moves
        user_alg,  # positional moves from CLI
        cli_setup,  # --setup (optional)
    )
    query["alg"] = [final_alg] if final_alg else [""]

    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


def open_in_twizzle(
    alg: str | None = None,
    *,
    base_url: str = BASE_URL,
    code_setup: str | None = CODE_DEFAULT_SETUP,
    preset: str | None = None,
    cli_setup: str | None = None,
) -> str:
    """
    Convenience wrapper: build URL and open in browser. Returns the URL.
    """
    url = build_twizzle_url(
        user_alg=alg,
        base_url=base_url,
        code_setup=code_setup,
        preset=preset,
        cli_setup=cli_setup,
    )
    webbrowser.open(url)
    return url


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Open Twizzle Editor with a Rubik's Cube algorithm.\n\n"
            "Final alg = CODE_DEFAULT_SETUP + CLI alg moves + preset + --setup."
        )
    )
    parser.add_argument(
        "alg",
        nargs="*",
        help="Main algorithm moves (e.g. D R U). Optional; can be empty.",
    )
    parser.add_argument(
        "--setup",
        default=None,  # this could be modified to not need to except quotes, but better this way as it will read each string seperate instead of part of args
        help='Extra setup moves to append at the end (e.g. "R U F").',
    )
    parser.add_argument(
        "--preset",
        default=None,
        choices=sorted(PRESETS.keys()) if PRESETS else None,
        help="Named preset to insert before --setup (e.g. gf_yu).",
    )
    parser.add_argument(
        "--base-url",
        default=BASE_URL,
        help="Base Twizzle editor URL (without alg).",
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Don't open the browser, just print the URL.",
    )

    args = parser.parse_args()
    user_alg_str = " ".join(args.alg) if args.alg else None

    url = build_twizzle_url(
        user_alg=user_alg_str,
        base_url=args.base_url,
        code_setup=CODE_DEFAULT_SETUP,
        preset=args.preset,
        cli_setup=args.setup,
    )

    # Small debug print so you can see exactly what Twizzle will get
    parsed = urlparse(url)
    q = parse_qs(parsed.query)
    alg_value = q.get("alg", [""])[0]
    print("alg =", alg_value)
    print("URL:", url)

    if not args.no_open:
        webbrowser.open(url)


if __name__ == "__main__":
    main()


"""
per final_alg, the order will be no matter how its types in cli
    - CODE_DEFAULT_SETUP
        - this is set up in this file
    - preset
        - this is set up in this file and is triggered via key word
    - moves
        - this could use quotes as optional
        - this will need spaces, eg: R U Rp Up
        - can also "'" notation: R U R\' U\'
    - setup
        - this will always need to be quotes with spaces
        - eg: "R U Rp Up"


# uv run python src/cube/ui.py R
    # this will run the default CODE_DEFAULT_SETUP so green front yellow top
    # followed by R
    # could be in quotes but dont need to be

# uv run python src/cube/ui.py Rp
    # this will run the default CODE_DEFAULT_SETUP so green front yellow top
    # followed by R prime
    # could be in quotes but dont need to be

# uv run python src/cube/ui.py R\'
    # this will run the default CODE_DEFAULT_SETUP so green front yellow top
    # followed by R prime

# uv run python src/cube/ui.py --preset checkered
    # this will run the default CODE_DEFAULT_SETUP so green front yellow top
    # followed by checkered moves

# uv run python src/cube/ui.py R U --preset checkered
    # this will run the default CODE_DEFAULT_SETUP so green front yellow top
    # R U
    # followed by checkered moves
    # doesnt matter if R U before/after --preset

# uv run python src/cube/ui.py R U --setup "Rp Up"
    # this will run the default CODE_DEFAULT_SETUP so green front yellow top
    # followed by R U
    # could be in quotes but dont need to be
    # followed up the --setup, in this case: Rp Up
    # must be in quotes

# make visual a="R U --setup 'Rp Up'"
    # everything in args must be in quotes

"""
