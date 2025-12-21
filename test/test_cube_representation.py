import random

# import numpy as np
from cube import Cube  # see alpha in cube/__init__.py
from cube import iterate_through_scrambles_for_testing


def test_generate_states():
    r""" """
    random.seed(0)

    moves = ["R", "U", "F", "D", "L", "B", "Rp", "Up", "Fp", "Dp", "Lp", "Bp"]
    cube_states = []
    cube_moves = []
    for state in range(3):
        solved = {
            "white": ["w"] * 9,
            "yellow": ["y"] * 9,
            "green": ["g"] * 9,
            "blue": ["b"] * 9,
            "red": ["r"] * 9,
            "orange": ["o"] * 9,
        }
        cube = Cube(solved)
        _cube_moves = []

        for move in range(3):
            mv = random.choice(moves)
            _cube_moves.append(mv)
            getattr(cube, mv)()

        cube_moves.append(_cube_moves)
        cube_states.append(cube.cube_state)
    assert cube_states[0] == {
        "white": ["w", "w", "g", "g", "g", "w", "w", "w", "w"],
        "yellow": ["y", "y", "b", "b", "b", "y", "y", "y", "y"],
        "green": ["g", "g", "y", "y", "y", "g", "g", "g", "g"],
        "blue": ["w", "b", "b", "b", "b", "b", "w", "w", "b"],
        "red": ["r", "r", "r", "r", "r", "r", "r", "r", "r"],
        "orange": ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
    }
    assert cube_states[1] == {
        "white": ["r", "r", "r", "w", "w", "w", "g", "g", "w"],
        "yellow": ["y", "y", "o", "o", "o", "b", "b", "y", "y"],
        "green": ["r", "r", "y", "g", "y", "y", "y", "g", "g"],
        "blue": ["w", "o", "o", "w", "w", "b", "b", "b", "b"],
        "red": ["b", "b", "w", "y", "b", "r", "r", "r", "r"],
        "orange": ["g", "g", "g", "o", "o", "o", "g", "w", "o"],
    }
    assert cube_states[2] == {
        "white": ["g", "w", "g", "g", "g", "w", "g", "g", "w"],
        "yellow": ["b", "b", "b", "y", "b", "b", "b", "y", "y"],
        "green": ["r", "r", "r", "y", "y", "g", "y", "y", "g"],
        "blue": ["o", "o", "o", "w", "w", "b", "w", "w", "b"],
        "red": ["w", "b", "w", "r", "r", "r", "r", "r", "r"],
        "orange": ["y", "g", "y", "o", "o", "o", "o", "o", "o"],
    }


def test_edge_count():
    solved = {
        "white": ["w"] * 9,
        "yellow": ["y"] * 9,
        "green": ["g"] * 9,
        "blue": ["b"] * 9,
        "red": ["r"] * 9,
        "orange": ["o"] * 9,
    }
    cube = Cube(solved)

    cube.R()
    cube.F()
    cube.L()
    cube.D()
    cube.Fp()
    cube.Bp()
    cube.R()
    cube.Lp()
    cube.L()
    cube.Fp()
    cube.Bp()
    cube.Up()

    assert cube.get_edge_count() == {
        "white": 1,
        "yellow": 0,
        "green": 2,
        "blue": 0,
        "red": 0,
        "orange": 1,
    }


def test_cross_oriented():
    moves = [
        ["R", "Dp", "Rp", "D", "R"],  # False
        ["D"],  # True
        ["R", "D", "Lp", "Dp", "Rp", "D", "L"],  # True
    ]

    cubes = []

    for state in range(3):
        solved = {
            "white": ["w"] * 9,
            "yellow": ["y"] * 9,
            "green": ["g"] * 9,
            "blue": ["b"] * 9,
            "red": ["r"] * 9,
            "orange": ["o"] * 9,
        }
        cube = Cube(solved)

        for move in range(len(moves[state])):
            getattr(cube, moves[state][move])()

        cubes.append(cube)

    assert not cubes[0].cross_oriented()
    assert cubes[1].cross_oriented()
    assert cubes[
        2
    ].cross_oriented()  # used to be == True; like saying if flaf == True vs if flag:


def test_identify_cross_edge_type():
    scrambles = [
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2"],
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2", "L", "L"],
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2", "L", "L", "Rp"],
        [
            "R2",
            "Fp",
            "Dp",
            "B",
            "D2",
            "Lp",
            "Fp",
            "D",
            "F",
            "R2",
            "D2",
            "Lp",
            "Up",
            "B",
        ],
        [
            "R2",
            "Fp",
            "Dp",
            "B",
            "D2",
            "Lp",
            "Fp",
            "D",
            "F",
            "R2",
            "D2",
            "D",
            "B",
            "Rp",
            "D",
            "Rp",
            "D",
            "R2",
        ],
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].identify_cross_edge_type() == [
        {"_seven_type": {"orange": ["g", "r"]}},
        {"_three_type": {"orange": ["b", "g"]}},
        {"_one_type": {"orange": ["y", "b"]}},
        {"_top_type": {}},
        {"_five_type": {}},
        {"bottum_type": {"white_r": ["r", "o"]}},
    ]

    assert cubes[1].identify_cross_edge_type() == [
        {"_seven_type": {"orange": ["g", "r"]}},
        {"_three_type": {"orange": ["b", "g"]}},
        {"_one_type": {"orange": ["y", "b"]}},
        {"_top_type": {"yellow_r": ["r", "o"]}},
        {"_five_type": {}},
        {"bottum_type": {}},
    ]

    assert cubes[2].identify_cross_edge_type() == [
        {"_seven_type": {"orange": ["g", "b"]}},
        {"_three_type": {}},
        {"_one_type": {"orange": ["y", "g"]}},
        {"_top_type": {"yellow_r": ["r", "o"]}},
        {"_five_type": {"orange": ["w", "r"]}},
        {"bottum_type": {}},
    ]

    assert cubes[3].identify_cross_edge_type() == [
        {"_seven_type": {"green": ["r", "o"], "orange": ["g", "r"]}},
        {"_three_type": {"blue": ["r", "b"]}},
        {"_one_type": {}},
        {"_top_type": {"yellow_b": ["b", "g"]}},
        {"_five_type": {}},
        {"bottum_type": {}},
    ]

    assert cubes[4].identify_cross_edge_type() == [
        {"_seven_type": {}},
        {"_three_type": {"green": ["o", "o"]}},
        {"_one_type": {}},
        {"_top_type": {"yellow_b": ["b", "g"]}},
        {"_five_type": {"red": ["w", "r"], "blue": ["w", "b"]}},
        {"bottum_type": {}},
    ]


def test_cross_permuted():
    scrambles = [
        ["F2", "R2", "Up", "R2", "U2", "F2"],  # bottum/bottum/bottum/bottum
        ["F2", "R2", "Up", "R2", "U2", "F2", "D"],  # bottum/bottum/bottum/bottum
        ["F2", "R2", "Up", "R2", "U2", "F2", "D2"],  # bottum/bottum/bottum/bottum
        ["F2", "R2", "Up", "R2", "U2", "F2", "Dp"],  # bottum/bottum/bottum/bottum
        ["D"],  # bottum/bottum/bottum/bottum
        ["D2"],  # bottum/bottum/bottum/bottum
        ["Dp"],  # bottum/bottum/bottum/bottum
        ["F", "B", "D2", "Fp", "Bp"],  # bottum/bottum/bottum/bottum
        ["F", "B", "D2", "Fp", "Bp", "D"],  # bottum/bottum/bottum/bottum
        ["F", "B", "D2", "Fp", "Bp", "D2"],  # bottum/bottum/bottum/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].cross_permuted() == [2, 3]  # blue and red
    assert cubes[1].cross_permuted() == [1]  # orange
    assert cubes[2].cross_permuted() == []  # none
    assert cubes[3].cross_permuted() == [0]  # green
    assert cubes[4].cross_permuted() == []  # none
    assert cubes[5].cross_permuted() == []  # none
    assert cubes[6].cross_permuted() == []  # none
    assert cubes[7].cross_permuted() == [0, 2]  # green and blue
    assert cubes[8].cross_permuted() == []  # none
    assert cubes[9].cross_permuted() == [1, 3]  # red and orange
