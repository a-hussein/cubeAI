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

# Base Twizzle editor URL (no alg here)
BASE_URL = "https://alpha.twizzle.net/edit/?puzzle=3x3x3"

# Always-prepended code-level setup
CODE_DEFAULT_SETUP = "r2 L2 u2 D2"

# Optional named presets (each is just more moves to append)
PRESETS: dict[str, str] = {
    # example: another orientation or helper sequence
    "gf_yu": "R U",
    # add more as needed
}


def _normalize_moves(moves: str | None) -> str:
    """
    Normalize a move string:
    - allow either spaces or '+' as separators
    - collapse extra whitespace
    """
    if not moves:
        return ""
    # Allow "R+U+F" style and normalize to spaces
    cleaned = moves.replace("+", " ")
    tokens = [t for t in cleaned.split() if t]
    return " ".join(tokens)


def _join_alg_parts(*parts: str | None) -> str:
    """
    Join multiple move strings into a single alg string, skipping empties.
    """
    tokens: list[str] = []
    for part in parts:
        if not part:
            continue
        norm = _normalize_moves(part)
        if not norm:
            continue
        tokens.extend(norm.split())
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
    Build a Twizzle URL with a single `alg=` parameter.

    Final alg order (based on your description):

        CODE_DEFAULT_SETUP  +  user_alg  +  preset_moves  +  cli_setup

    Example:
        CODE_DEFAULT_SETUP = "r2 L2 u2 D2"
        user_alg   = "D R U"
        cli_setup  = "R U F"
        preset     = None

        => "r2 L2 u2 D2 D R U R U F"
    """
    parsed = urlparse(base_url)
    query = parse_qs(parsed.query, keep_blank_values=True)

    # Resolve preset to its move string if provided
    preset_moves = PRESETS.get(preset) if preset else None

    final_alg = _join_alg_parts(
        code_setup,
        user_alg,
        preset_moves,
        cli_setup,
    )

    # Put everything in a single `alg` param
    query["alg"] = [final_alg]

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
        default=None,
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






















# from __future__ import annotations

# import argparse
# import webbrowser
# from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# # Copy your own favorite Twizzle editor URL here after you tweak settings
# # in the UI (stickers, tempo, etc.) and hit copy address.
# # For now we just use a basic 3x3x3 editor.
# DEFAULT_BASE_URL = "https://alpha.twizzle.net/edit/?puzzle=3x3x3"

# PRESETS: dict[str, str] = {
#     "gf_yu": "r2 L2 u2 D2", # Example: orient to Green-Front / Yellow-Up, since that's my convention; # could have used "z2"     
# }

# def build_twizzle_url(alg: str, base_url: str = DEFAULT_BASE_URL, setup: str | None = None) -> str:
#     """
#     Take a move sequence in WCA notation and inject it into a Twizzle URL.

#     Example:
#         build_twizzle_url("R U R' U'")
#     """
#     # Parse the base Twizzle URL
#     parsed = urlparse(base_url)

#     # Turn the query string into a dict
#     query = parse_qs(parsed.query, keep_blank_values=True)

#     if setup:
#         query["setup"] = [setup]

#     # Overwrite the 'alg' parameter with our sequence
#     # Twizzle expects spaces between moves (e.g. "R U R' U'")
#     query["alg"] = [alg]

#     # Rebuild the URL
#     new_query = urlencode(query, doseq=True)
#     new_parsed = parsed._replace(query=new_query)
#     return urlunparse(new_parsed)


# def open_in_twizzle(alg: str, base_url: str = DEFAULT_BASE_URL, setup: str | None = None) -> str:
#     """
#     Build the Twizzle URL and open it in the default web browser.

#     Returns the URL (in case you want to log or print it).
#     """
#     url = build_twizzle_url(alg=alg, base_url=base_url, setup=setup)
#     webbrowser.open(url)
#     return url


# def main() -> None:
#     parser = argparse.ArgumentParser(
#         description="Open Twizzle Editor with a given Rubik's cube algorithm."
#     )

#     parser.add_argument(
#         "alg",
#         nargs="+",
#         help="Algorithm moves in WCA notation (e.g. R U R' U'). "
#              "You can separate moves with spaces; they will be joined.",
#     )

#     parser.add_argument(
#         "--setup",
#         default=None,
#         help="Optional setup moves to load into Twizzle's Setup area (e.g. \"r2 L2 u2 D2\").",
#     )

#     parser.add_argument(
#         "--preset",
#         default=None,
#         choices=sorted(PRESETS.keys()) if PRESETS else None,
#         help="Optional named preset (maps to a setup sequence).",
#     )

#     parser.add_argument(
#         "--base-url",
#         default=DEFAULT_BASE_URL,
#         help="Base Twizzle editor URL to use (with your preferred settings).",
#     )

#     parser.add_argument(
#         "--no-open",
#         action="store_true",
#         help="Don't open the browser, just print the URL.",
#     )

#     args = parser.parse_args()
#     alg_str = " ".join(args.alg)


#     setup_str = args.setup
#     if args.preset:
#         preset_moves = PRESETS.get(args.preset)
#         if preset_moves:
#             setup_str = preset_moves if not setup_str else f"{preset_moves} {setup_str}"

#     url = build_twizzle_url(alg=alg_str, base_url=args.base_url, setup=setup_str)

#     if args.no_open:
#         print(url)
#     else:
#         print(f"Opening Twizzle with alg: {alg_str}")
#         print(f"URL: {url}")
#         webbrowser.open(url)


# if __name__ == "__main__":
#     main()
