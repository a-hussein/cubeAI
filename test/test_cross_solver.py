import random


from cube import do_scramble, iterate_through_scrambles_for_testing, cross_solver


def test_seven_type_cross_solver():
    scrambles = [
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
            "B2",
            "Rp",
            "F",
            "R",
        ],  # seven/seven/bottum/bottum
        ["Rp", "Fp", "Lp", "R", "Bp", "Rp", "F", "R", "Fp"],  # seven/seven/seven/bottum
        ["Rp", "Fp", "Lp", "R", "Bp", "Rp"],  # seven/seven/seven/seven
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
            "Bp",
        ],  # seven/one/bottum/bottum
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
        ],  # seven/three/one/bottum
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
            "B",
        ],  # seven/one/top/bottum
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
            "B2",
        ],  # seven/seven/one/bottum
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
        ],  # seven/top/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].seven_type_cross_solver() == [
        ["I", "B"],
        ["I", "B"],
        ["Dp", "F"],
        ["Dp", "F"],
    ]
    assert cubes[1].seven_type_cross_solver() == [["I", "L"], ["I", "B"], ["I", "F"]]
    assert cubes[2].seven_type_cross_solver() == [
        ["I", "L"],
        ["I", "B"],
        ["I", "R"],
        ["I", "F"],
    ]
    assert cubes[3].seven_type_cross_solver() == [["U", "Dp", "F"], ["U", "Dp", "F"]]
    assert cubes[4].seven_type_cross_solver() == [["U", "Dp", "F"]]
    assert cubes[5].seven_type_cross_solver() == [["U", "Dp", "F"], ["U2", "Dp", "F"]]
    assert cubes[6].seven_type_cross_solver() == [["Up", "I", "B"], ["U", "Dp", "F"]]
    assert cubes[7].seven_type_cross_solver() == [["U2", "D2", "F"], ["U2", "D2", "F"]]


def test_three_type_cross_solver():
    scrambles = [
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
            "F2",
        ],  # three/three/one/bottum
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
            "Fp",
        ],  # three/one/top/bottum
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
        ],  # seven/three/one/bottum
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
            "U",
            "Fp",
            "L",
            "F",
            "Lp",
        ],  # seven/seven/three/bottum
        ["Fp", "R", "Fp", "Bp", "L", "Bp"],  # one/one/one/one
        [
            "Fp",
            "R",
            "Fp",
            "Bp",
            "L",
            "Bp",
            "Fp",
            "Rp",
            "Bp",
            "Fp",
            "Lp",
            "F2",
            "F",
            "B2",
        ],  # three/three/three/three
        ["D", "Fp", "Lp", "B", "D2", "L", "B", "Lp", "Bp"],  # seven/seven/seven/three
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
        ],  # three/top/five/five
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].three_type_cross_solver() == [["U", "Dp", "Fp"], ["Up", "I", "Bp"]]
    assert cubes[1].three_type_cross_solver() == [["Up", "I", "Bp"], ["U2", "I", "Bp"]]
    assert cubes[2].three_type_cross_solver() == [["Up", "I", "Bp"]]
    assert cubes[3].three_type_cross_solver() == [["I", "Bp"]]
    assert cubes[4].three_type_cross_solver() is None
    assert cubes[5].three_type_cross_solver() == [
        ["I", "Rp"],
        ["I", "Fp"],
        ["I", "Lp"],
        ["I", "Bp"],
    ]
    assert cubes[6].three_type_cross_solver() == [["I", "Lp"], ["I", "Bp"]]
    assert cubes[7].three_type_cross_solver() == [["U", "D2", "Rp"], ["U", "Dp", "Rp"]]


def test_one_type_cross_solver():
    scrambles = [
        ["L", "D", "L", "Dp", "B", "Dp", "R2", "D"],  # one/top/bottum/bottum
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
            "F2",
        ],  # three/three/one/bottum
        ["L", "D", "L", "Dp", "B", "Dp", "R2", "D2", "L"],  # seven/one/bottum/bottum
        ["Fp", "R", "Fp", "Bp", "L", "Bp"],  # one/one/one/one
        ["Fp", "R", "Fp", "Bp", "L", "Bp", "F", "Lp", "Bp"],  # seven/three/top/one
        ["F", "Lp", "B", "R", "Dp", "Rp", "Dp"],  # seven/one/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].one_type_cross_solver() == [
        ["I", "R"],
        ["I", "Rp"],
        ["D", "R"],
        ["D", "Rp"],
        ["Dp", "R"],
        ["Dp", "Rp"],
    ]
    assert cubes[1].one_type_cross_solver() == [["I", "R"], ["I", "Rp"]]
    assert cubes[2].one_type_cross_solver() == [
        ["D", "R"],
        ["D", "Rp"],
        ["Dp", "R"],
        ["Dp", "Rp"],
        ["I", "R"],
        ["I", "Rp"],
    ]
    assert cubes[3].one_type_cross_solver() == [
        ["I", "F"],
        ["I", "Fp"],
        ["I", "L"],
        ["I", "Lp"],
        ["I", "B"],
        ["I", "Bp"],
        ["I", "R"],
        ["I", "Rp"],
    ]
    assert cubes[4].one_type_cross_solver() == [["I", "R"], ["I", "Rp"]]
    assert cubes[5].one_type_cross_solver() == [
        ["I", "L"],
        ["I", "Lp"],
        ["I", "L"],
        ["I", "Lp"],
    ]


def test_top_type_cross_solver():
    scrambles = [
        ["L", "D", "L", "Dp", "B", "Dp", "R2", "D"],  # one/top/bottum/bottum
        ["Fp", "R", "Fp", "Bp", "L", "Bp", "F", "Lp", "Bp"],  # seven/three/one/top
        ["R", "F", "Dp", "F", "R2", "Dp"],  # top/top/five/bottum
        ["R", "F", "Dp", "F", "R2"],  # top/top/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].top_type_cross_solver() == [
        ["I", "L"],
        ["I", "Lp"],
        ["I", "L"],
        ["I", "Lp"],
    ]
    assert cubes[1].top_type_cross_solver() == [["I", "B"], ["I", "Bp"]]
    assert cubes[2].top_type_cross_solver() == [
        ["Dp", "R"],
        ["Dp", "Rp"],
        ["D", "R"],
        ["D", "Rp"],
        ["D2", "F"],
        ["D2", "Fp"],
        ["D2", "F"],
        ["D2", "Fp"],
    ]
    assert cubes[3].top_type_cross_solver() == [
        ["D2", "R"],
        ["D2", "Rp"],
        ["I", "R"],
        ["I", "Rp"],
        ["D", "F"],
        ["D", "Fp"],
        ["D", "F"],
        ["D", "Fp"],
    ]


def test_five_type_cross_solver():
    scrambles = [
        ["R", "F", "Dp", "F", "R2"],  # top/top/five/bottum
        ["R", "F", "Bp", "L", "U2", "L"],  # seven/one/top/five
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
            "Dp",
            "B",
            "Rp",
            "D",
        ],  # seven/top/five/bottum
        [
            "F2",
            "Rp",
            "D",
            "Bp",
            "Fp",
            "Rp",
            "L",
            "L",
            "R",
            "B2",
            "F",
            "D2",
            "R",
        ],  # one/top/five/bottum
        ["R", "F", "L", "Bp", "U", "B"],  # one/five/five/bottum
        ["L", "D", "L", "Dp", "B", "Dp"],  # top/five/bottum/bottum
        ["F2", "Rp", "D", "Bp", "Fp", "Rp", "L", "L"],  # seven/top/five/five
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].five_type_cross_solver() == [
        ["U2", "L"],
        ["U2", "Lp"],
        ["U", "L"],
        ["U", "Lp"],
    ]
    assert cubes[1].five_type_cross_solver() == [
        ["U", "F"],
        ["U", "Fp"],
        ["Up", "F"],
        ["Up", "Fp"],
    ]
    assert cubes[2].five_type_cross_solver() == [["I", "B"], ["I", "Bp"]]
    assert cubes[3].five_type_cross_solver() == [
        ["U", "R"],
        ["U", "Rp"],
        ["U2", "R"],
        ["U2", "Rp"],
    ]
    assert cubes[4].five_type_cross_solver() == [
        ["U", "F"],
        ["U", "Fp"],
        ["U2", "L"],
        ["U2", "Lp"],
    ]
    assert cubes[5].five_type_cross_solver() == [["U2", "R"], ["U2", "Rp"]]
    assert cubes[6].five_type_cross_solver() == [
        ["U", "B"],
        ["U", "Bp"],
        ["U2", "R"],
        ["U2", "Rp"],
    ]


def test_bottum_type_cross_solver():
    random.seed(0)
    scrambles = [
        ["F2", "R2", "Up", "R2", "U2", "F2"],  # bottum/bottum/bottum/bottum
        ["F2", "R2", "Up", "R2", "U2", "F2", "D"],  # bottum/bottum/bottum/bottum
        ["F2", "R2", "Up", "R2", "U2", "F2", "D2"],  # bottum/bottum/bottum/bottum
        ["F2", "R2", "Up", "R2", "U2", "F2", "Dp"],  # bottum/bottum/bottum/bottum
        ["D", "F2", "R2", "Up", "R2", "U2", "F2", "Dp"],  # bottum/bottum/bottum/bottum
        ["D", "F2", "R2", "Up", "R2", "U2", "F2", "D2"],  # bottum/bottum/bottum/bottum
        ["D"],  # bottum/bottum/bottum/bottum
        ["D2"],  # bottum/bottum/bottum/bottum
        ["Dp"],  # bottum/bottum/bottum/bottum
        ["F2", "B2", "U2", "F2", "B2"],  # bottum/bottum/bottum/bottum
        ["F2", "B2", "U2", "F2", "B2", "D2"],  # bottum/bottum/bottum/bottum
        ["F2", "B2", "U2", "F2", "B2", "Dp"],  # bottum/bottum/bottum/bottum
        ["F2", "B2", "U2", "F2", "B2", "D"],  # bottum/bottum/bottum/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].bottum_type_cross_solver() == [
        ["R", "D", "Rp", "Dp", "R"]
    ]  # alpha green
    assert cubes[1].bottum_type_cross_solver() == [
        ["Dp", "R", "D", "Rp", "Dp", "R"]
    ]  # alpha green
    assert cubes[2].bottum_type_cross_solver() == [
        ["D2", "R", "D", "Rp", "Dp", "R"]
    ]  # alpha green
    assert cubes[3].bottum_type_cross_solver() == [
        ["D", "R", "D", "Rp", "Dp", "R"]
    ]  # alpha green
    assert cubes[4].bottum_type_cross_solver() == [
        ["F", "D", "Fp", "Dp", "F"]
    ]  # alpha red
    assert cubes[5].bottum_type_cross_solver() == [
        ["D", "F", "D", "Fp", "Dp", "F"]
    ]  # alpha red
    assert cubes[6].bottum_type_cross_solver() == [["Dp"]]
    assert cubes[7].bottum_type_cross_solver() == [["D2"]]
    assert cubes[8].bottum_type_cross_solver() == [["D"]]
    assert cubes[9].bottum_type_cross_solver() == [["L", "R", "D2", "Lp", "Rp"]]  # beta
    assert cubes[10].bottum_type_cross_solver() == [
        ["F", "B", "D2", "Fp", "Bp"]
    ]  # beta
    assert cubes[11].bottum_type_cross_solver() == [
        ["Dp", "F", "B", "D2", "Fp", "Bp"]
    ]  # gamma
    assert cubes[12].bottum_type_cross_solver() == [
        ["D", "F", "B", "D2", "Fp", "Bp"]
    ]  # gamma


def test_treeify_cross_solver():
    # 8 moves with len(all_moves) <=5
    # however, if compression worked, this would be seven!
    _cube = do_scramble(
        [
            "F2",
            "L",
            "D2",
            "Lp",
            "R2",
            "U2",
            "B2",
            "Rp",
            "U2",
            "F2",
            "Rp",
            "D",
            "B2",
            "R",
            "F2",
            "Bp",
            "L",
            "F",
            "U",
            "Dp",
        ]
    )
    k = cross_solver(_cube, min_move_only=True)

    # k is many solutions. idk how to assert on this since the solves come in diff orders for some reaosn
    # for now doing individual checks and confirming that the len's are same in case other solves missed
    assert k[0] in k
    assert k[1] in k
    assert k[2] in k
    assert k[3] in k
    assert k[4] in k
    assert k[5] in k
    assert k[6] in k
    assert len(k) == int(len(k[0] + k[1] + k[2] + k[3] + k[4] + k[5] + k[6]) / 2)

    # 7 moves with len(all_moves) <=5 (alhtough, this could be done in 5, but i think it will change once i fix the set up move)
    _cube = do_scramble(["R2", "U2", "Fp", "L2", "D2", "R2", "Dp", "Bp", "Rp", "L2"])
    k = cross_solver(_cube, min_move_only=True)
    assert k == [[7, ["U2", "Rp", "Dp", "Rp", "D2", "R", "Dp"]]]

    # 2 moves with len(all_moves) <=5
    _cube = do_scramble(["R", "F"])
    k = cross_solver(_cube, min_move_only=True)
    assert k == [[2, ["Fp", "Rp"]]]

    # 1 move with len(all_moves) <=5
    _cube = do_scramble(["D"])
    k = cross_solver(_cube, min_move_only=True)
    assert k == [[1, ["Dp"]]]
