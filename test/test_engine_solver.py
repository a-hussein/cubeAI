from cube import iterate_through_scrambles_for_testing


def test_combo():
    scrambles = [
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2"],
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
        ],
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2", "Bp"],
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2", "B2"],
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2", "B"],
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2", "F2"],
        ["R2", "Fp", "Dp", "B", "D2", "Lp", "Fp", "D", "F", "R2", "D2", "Fp"],
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

    assert cubes[0].combo() == [
        ["_seven_type", "orange", "g", "r"],
        ["_three_type", "orange", "b", "g"],
        ["_one_type", "orange", "y", "b"],
        ["bottum_type", "white_r", "r", "o"],
    ]

    assert cubes[1].combo() == [
        ["_seven_type", "red", "b", "g"],
        ["_seven_type", "orange", "g", "r"],
        ["bottum_type", "white_g", "g", "b"],
        ["bottum_type", "white_r", "r", "o"],
    ]

    assert cubes[2].combo() == [
        ["_seven_type", "orange", "g", "r"],
        ["_one_type", "orange", "y", "b"],
        ["bottum_type", "white_b", "b", "g"],
        ["bottum_type", "white_r", "r", "o"],
    ]

    assert cubes[3].combo() == [
        ["_seven_type", "red", "b", "g"],
        ["_seven_type", "orange", "g", "r"],
        ["_one_type", "orange", "y", "b"],
        ["bottum_type", "white_r", "r", "o"],
    ]

    assert cubes[4].combo() == [
        ["_seven_type", "orange", "g", "r"],
        ["_one_type", "orange", "y", "b"],
        ["_top_type", "yellow_b", "b", "g"],
        ["bottum_type", "white_r", "r", "o"],
    ]
    assert cubes[5].combo() == [
        ["_three_type", "red", "g", "r"],
        ["_three_type", "orange", "b", "g"],
        ["_one_type", "orange", "y", "b"],
        ["bottum_type", "white_r", "r", "o"],
    ]
    assert cubes[6].combo() == [
        ["_three_type", "orange", "b", "g"],
        ["_one_type", "orange", "y", "b"],
        ["_top_type", "yellow_g", "g", "r"],
        ["bottum_type", "white_r", "r", "o"],
    ]

    assert cubes[7].combo() == [
        ["_three_type", "green", "o", "o"],
        ["_top_type", "yellow_b", "b", "g"],
        ["_five_type", "red", "w", "r"],
        ["_five_type", "blue", "w", "b"],
    ]


def test_seven_three_orientation_delta():
    many_scrambles = [
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
            "D",
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
            "D",
            "B",
            "Rp",
            "D",
        ],  # seven/top/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(many_scrambles)

    assert cubes[0].seven_three_orientation_delta(0, 3) == ["Dp"]
    assert cubes[0].seven_three_orientation_delta(0, 2) == ["U"]
    assert cubes[0].seven_three_orientation_delta(1, 3) == ["I"]
    assert cubes[0].seven_three_orientation_delta(1, 2) == ["Up"]

    assert cubes[1].seven_three_orientation_delta(0, 3) == ["D2"]
    assert cubes[1].seven_three_orientation_delta(0, 1) == ["U"]
    assert cubes[1].seven_three_orientation_delta(0, 2) == ["U2"]

    assert cubes[2].seven_three_orientation_delta(0, 3) == ["D2"]
    assert cubes[2].seven_three_orientation_delta(0, 1) == ["U2"]
    assert cubes[2].seven_three_orientation_delta(0, 2) == ["D2"]


def test_combine_seven_three_orientation_delta():
    many_scrambles = [
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
            "D",
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
            "D",
            "B",
            "Rp",
            "D",
        ],  # seven/top/five/bottum
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

    cubes = iterate_through_scrambles_for_testing(many_scrambles)

    assert cubes[0].combine_seven_three_orientation_delta(0, 3, 2) == ["Dp", "U"]
    assert cubes[0].combine_seven_three_orientation_delta(1, 3, 2) == ["I", "Up"]

    assert cubes[1].combine_seven_three_orientation_delta(0, 3, 1) == ["D2", "U"]
    assert cubes[1].combine_seven_three_orientation_delta(0, 3, 2) == ["D2", "U2"]

    assert cubes[2].combine_seven_three_orientation_delta(0, 1, 2) == ["U2", "D2"]
    assert cubes[2].combine_seven_three_orientation_delta(0, 1, 3) == ["U2", "D2"]

    assert cubes[3].combine_seven_three_orientation_delta(0, 1, 2) == ["U", "D2"]
    assert cubes[3].combine_seven_three_orientation_delta(0, 1, 3) == ["U", "Dp"]


def test_one_orientation_delta():
    scrambles = [
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
        ["R", "F", "L", "Bp", "U", "B", "Dp"],  # one/five/five/bottum
        ["R", "F", "L", "Bp", "U", "B", "Dp", "Dp"],  # one/five/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].one_orientation_delta(0, 1) == ["I"]
    assert cubes[0].one_orientation_delta(0, 2) == ["D"]
    assert cubes[0].one_orientation_delta(0, 3) == ["D", "Dp"]

    assert cubes[1].one_orientation_delta(0, 1) == ["D"]
    assert cubes[1].one_orientation_delta(0, 2) == ["D2"]
    assert cubes[1].one_orientation_delta(0, 3) == ["I"]

    assert cubes[2].one_orientation_delta(0, 1) == ["D2"]
    assert cubes[2].one_orientation_delta(0, 2) == ["Dp"]
    assert cubes[2].one_orientation_delta(0, 3) == ["D", "Dp"]

    assert cubes[3].one_orientation_delta(0, 1) == ["Dp"]
    assert cubes[3].one_orientation_delta(0, 2) == ["I"]
    assert cubes[3].one_orientation_delta(0, 3) == ["I"]


def test_top_orientation_delta():
    scrambles = [
        ["L", "D", "L", "Dp", "B", "Dp"],  # top/five/bottum/bottum
        ["F2", "Rp", "D", "Bp", "Fp", "Rp", "L", "L"],  # seven/top/five/five
        ["F2", "Rp", "D", "Bp", "Fp", "Rp", "L", "L", "R", "B2"],  # seven/three/one/top
        ["L", "D", "L", "Dp", "B"],  # top/five/bottum/bottum
        ["L", "D", "L", "Dp", "B", "D"],  # top/five/bottum/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].top_orientation_delta(0, 1) == ["D2"]
    assert cubes[0].top_orientation_delta(0, 2) == ["D"]
    assert cubes[0].top_orientation_delta(0, 3) == ["D"]

    assert cubes[1].top_orientation_delta(1, 2) == ["D"]
    assert cubes[1].top_orientation_delta(1, 3) == ["D2"]

    assert cubes[2].top_orientation_delta(3, 0) == ["I"]
    assert cubes[2].top_orientation_delta(3, 1) == ["I"]
    assert cubes[2].top_orientation_delta(3, 2) == ["I"]

    assert cubes[3].top_orientation_delta(0, 1) == ["D"]
    assert cubes[3].top_orientation_delta(0, 2) == ["I"]
    assert cubes[3].top_orientation_delta(0, 3) == ["I"]

    assert cubes[4].top_orientation_delta(0, 1) == ["I"]
    assert cubes[4].top_orientation_delta(0, 2) == ["Dp"]
    assert cubes[4].top_orientation_delta(0, 3) == ["Dp"]


def test_five_orientation_delta():
    scrambles = [
        ["R", "F", "Dp", "F", "R2"],  # top/top/five/bottum
        ["R", "F", "Bp", "L", "U2", "L"],  # seven/one/top/five
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].five_orientation_delta(2, 0) == ["U2"]
    assert cubes[0].five_orientation_delta(2, 1) == ["U"]
    assert cubes[0].five_orientation_delta(2, 3) == ["I"]

    assert cubes[1].five_orientation_delta(3, 0) == ["I"]
    assert cubes[1].five_orientation_delta(3, 1) == ["U"]
    assert cubes[1].five_orientation_delta(3, 2) == ["Up"]


def test_bottum_orientation_delta():
    scrambles = [
        ["F2", "R2", "Up", "R2", "U2", "F2", "D"],  # bottum/bottum/bottum/bottum
        ["D"],  # bottum/bottum/bottum/bottum
        ["D2"],  # bottum/bottum/bottum/bottum
        ["Dp"],  # bottum/bottum/bottum/bottum
        ["F", "B", "D2", "Fp", "Bp"],  # bottum/bottum/bottum/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].bottum_orientation_delta() is None
    assert cubes[1].bottum_orientation_delta() == ["Dp"]
    assert cubes[2].bottum_orientation_delta() == ["D2"]
    assert cubes[3].bottum_orientation_delta() == ["D"]
    assert cubes[4].bottum_orientation_delta() is None
