"""
This script enables: make demo b="R U Rp Up"
Essentially, script version of `demo/specific_scramble.ipynb`
"""

import sys
import os

from cube import (
    move_notation_converter,
    cross_solver,
    compress_moves,
    do_scramble,
)
from cube.visualizer import open_in_twizzle

DEFAULT_SCRAMBLE = ["R2", "L", "U", "D", "F", "B"]


def main(your_scramble):

    move_converted = move_notation_converter(your_scramble)

    if os.getenv("NO_TWIZZLE") == "1":
        print(f"Sramble:")
    open_in_twizzle(move_converted)

    cube = do_scramble(your_scramble)
    solutions = cross_solver(cube)

    final_solution = {}
    local_min = float("inf")

    for sol in solutions:
        compressed_solution = compress_moves(sol[1])
        L = len(compressed_solution)
        if L < local_min:
            final_solution["cube"] = compressed_solution
            local_min = L

    print("a compressed solution:")
    print("\t", len(final_solution["cube"]), final_solution["cube"])

    solved_cube = do_scramble(cube=cube, moves=final_solution["cube"])

    if not solved_cube.cross_solved():
        print("cube's white cross is not solved")
    else:
        print("YES, cube's white cross is solved!")

    scramble_plus_solution = (
        move_converted + " " + move_notation_converter(final_solution["cube"])
    )

    if os.getenv("NO_TWIZZLE") == "1":
        print(f"Solution:")
    open_in_twizzle(scramble_plus_solution)


if __name__ == "__main__":
    moves = sys.argv[1:]
    your_scramble = moves if moves else DEFAULT_SCRAMBLE
    main(your_scramble)
