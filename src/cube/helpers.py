from copy import deepcopy
from .cube_representation import Cube
from .cross_solver import CrossSolver
import random


def solved_cube():
    solved = {
        "white": ["w"] * 9,
        "yellow": ["y"] * 9,
        "green": ["g"] * 9,
        "blue": ["b"] * 9,
        "red": ["r"] * 9,
        "orange": ["o"] * 9,
    }

    solved_cube = Cube(solved)

    return solved_cube


def do_scramble(moves, cube=solved_cube(), in_place=False):
    """
    This function performs a set of moves on a `cube` object.

    It takes input of list of strings as moves.

    Input: ["R", "U", "Rp", "Up"]
    Output: a `cube` object with the above moves applied to it.

    The default is to apply the moves to a `solved_cube()`, however, one may apply it on a cube with already done moves

    """
    if not in_place:
        cube_copy = deepcopy(cube)
        for move in range(len(moves)):
            getattr(cube_copy, moves[move])()
        return cube_copy

    else:
        for move in range(len(moves)):
            getattr(cube, moves[move])()
        return cube


# use multiple scrambles - useful for testing
def iterate_through_scrambles_for_testing(many_scrambles):
    cubes = []
    for scramble in range(len(many_scrambles)):
        cube = do_scramble(many_scrambles[scramble])
        cubes.append(cube)
    return cubes


def sanitize(moves):
    unique_list = []
    seen = set()
    if moves is not None:
        for sublist in moves:
            cleaned_sublist = [item for item in sublist if item != "I"]
            cleaned_tuple = tuple(cleaned_sublist)
            if cleaned_tuple not in seen:
                unique_list.append(cleaned_sublist)
                seen.add(cleaned_tuple)
    else:
        pass
    return unique_list


def generate_random_scramble(num_moves=10):
    moves = [
        "R",
        "U",
        "F",
        "D",
        "L",
        "B",
        "Rp",
        "Up",
        "Fp",
        "Dp",
        "Lp",
        "Bp",
        "R2",
        "U2",
        "F2",
        "D2",
        "L2",
        "B2",
    ]
    scramble = []
    while len(scramble) < num_moves:
        mv = random.choice(moves)
        if len(scramble) == 0:
            scramble.append(mv)
        elif (
            len(scramble) > 0 and mv[0] != scramble[-1][0]
        ):  # check if first subletter of the moveset (F2 is a move set) is same as prior (you dont want F2 followed by F for example)
            scramble.append(mv)
        else:
            continue
    return scramble


def cross_solver(cube, min_move_only=True, max_num_of_moves_in_solution=10):
    """
    An easier way to streamline the cross_solver. Usefulwith testing.
    If min_move_only = True, then the next param doesn't matter.
    Outputs a list of potential solution(s) with repeats removed and sorted.
    """
    solver = CrossSolver()
    solver.treeify(cube, [])
    _solutions = solver.solutions

    unique_solutions = [
        list(t) for t in set(tuple(inner_list) for inner_list in _solutions)
    ]
    solns = [[len(solution), solution] for solution in unique_solutions]
    sorted_solns = sorted(solns, key=lambda x: x[0])

    k = []
    for i in sorted_solns:
        if i[0] <= max_num_of_moves_in_solution:
            k.append(i)

    min_k = min([i[0] for i in k])
    if min_move_only:
        min_move_only = min_k
        k = [i for i in k if i[0] == min_k]
    else:
        k = [i for i in k if i[0]]

    return k


def compress_moves(moves):
    m = moves
    while True:
        n = len(m)
        moves = 0
        tmp = []

        for i, letter in enumerate(m):
            if i == len(m) - 1:
                tmp.append(letter)
                break

            # R R -> R2
            if letter == m[i + 1] and len(letter) == 1:
                tmp.append(letter + "2")
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break

            # Rp Rp -> R2
            elif letter == m[i + 1] and len(letter) == 2 and letter[1] == "p":
                tmp.append(letter[0] + "2")
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break
            # R2 R2 -> pass
            elif letter == m[i + 1] and len(letter) == 2 and letter[1] == "2":
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break
            # R2 R -> Rp
            elif (len(letter) == 2 and letter[1] == "2") and (
                letter[0] == m[i + 1][0] and len(m[i + 1]) == 1
            ):
                tmp.append(letter[0] + "p")
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break
            # R R2 -> Rp
            elif (len(letter) == 1 and m[i + 1][-1] == "2") and (
                letter[0] == m[i + 1][0] and len(m[i + 1]) == 2
            ):
                tmp.append(letter[0] + "p")
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break
            # Rp R -> pass
            elif (
                len(letter) == 2
                and letter[1] == "p"
                and letter[0] == m[i + 1][0]
                and len(m[i + 1]) == 1
            ):
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break
            # R Rp -> pass
            elif (
                len(letter) == 1
                and m[i + 1][-1] == "p"
                and letter[0] == m[i + 1][0]
                and len(m[i + 1]) == 2
            ):
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break
            # Rp R2 -> R
            elif (
                len(letter) == 2
                and letter[1] == "p"
                and m[i + 1][-1] == "2"
                and letter[0] == m[i + 1][0]
                and len(m[i + 1]) == 2
            ):
                tmp.append(letter[0])
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break
            #         R2 Rp -> R
            elif (
                len(letter) == 2
                and letter[1] == "2"
                and m[i + 1][-1] == "p"
                and letter[0] == m[i + 1][0]
                and len(m[i + 1]) == 2
            ):
                tmp.append(letter[0])
                if i + 2 < n:
                    tmp.extend(m[i + 2 :])
                moves += 1
                break

            else:
                tmp.append(letter)
        if moves != 0:
            m = tmp
        elif m == tmp:
            break
        m = tmp
    return m


def move_notation_converter(scramble):
    """
    This function converts the notation that I have been using on the `cube` object to the notation used in the cli visualizer.
    My notation has been moves as strings within a list, eg: ["R", "U",...]
    The visualizer simply uses moves with spaces, eg: "R U..."

    Input: ["R", "U"]
    Output: "R U"
    """

    updated_scramble = ""
    counter = 0
    for i in scramble:
        if counter == len(scramble) - 1:
            updated_scramble += i
        else:
            updated_scramble += i + " "
        counter += 1
    return updated_scramble
