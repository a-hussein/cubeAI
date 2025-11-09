import random

from cubeai.test.helper_functions import ( 
    solved_cube, 
    do_scramble, 
    iterate_through_scrambles_for_testing, 
    sanitize, 
    generate_random_scramble
)

def test_do_scramble():
    scramble = ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2']
    cube_with_R_move = do_scramble(['R'])

    assert do_scramble(scramble).cube_state == {
        'white': ['g', 'r', 'b', 'w', 'o', 'r', 'r', 'y', 'w'],
        'yellow': ['b', 'o', 'r', 'b', 'g', 'o', 'o', 'g', 'y'],
        'green': ['w', 'b', 'o', 'r', 'r', 'b', 'y', 'y', 'g'],
        'blue': ['b', 'g', 'o', 'y', 'g', 'g', 'b', 'g', 'b'],
        'red': ['w', 'y', 'g', 'b', 'r', 'o', 'w', 'r', 'r'],
        'orange': ['y', 'w', 'y', 'w', 'y', 'o', 'w', 'w', 'o']
        }

    assert do_scramble(scramble, solved_cube()).cube_state == {
        'white': ['g', 'r', 'b', 'w', 'o', 'r', 'r', 'y', 'w'],
        'yellow': ['b', 'o', 'r', 'b', 'g', 'o', 'o', 'g', 'y'],
        'green': ['w', 'b', 'o', 'r', 'r', 'b', 'y', 'y', 'g'],
        'blue': ['b', 'g', 'o', 'y', 'g', 'g', 'b', 'g', 'b'],
        'red': ['w', 'y', 'g', 'b', 'r', 'o', 'w', 'r', 'r'],
        'orange': ['y', 'w', 'y', 'w', 'y', 'o', 'w', 'w', 'o']
        }

    assert do_scramble(scramble, cube_with_R_move).cube_state == {
        'white': ['g', 'r', 'b', 'b', 'o', 'r', 'r', 'g', 'w'],
        'yellow': ['y', 'o', 'r', 'b', 'w', 'o', 'o', 'g', 'y'],
        'green': ['b', 'y', 'o', 'r', 'r', 'b', 'y', 'y', 'g'],
        'blue': ['b', 'w', 'o', 'y', 'g', 'g', 'y', 'g', 'b'],
        'red': ['b', 'y', 'w', 'b', 'r', 'o', 'w', 'r', 'r'],
        'orange': ['g', 'w', 'y', 'w', 'g', 'o', 'w', 'w', 'o']
        }

    assert do_scramble(['I']).cube_state == {
        'white': ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        'yellow': ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
        'green': ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
        'blue': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
        'red': ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
        'orange': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        }

    assert do_scramble(['R'], cube_with_R_move, in_place=True).cube_state == {
        'white': ['w', 'w', 'y', 'y', 'y', 'w', 'w', 'w', 'w'],
        'yellow': ['y', 'y', 'w', 'w', 'w', 'y', 'y', 'y', 'y'],
        'green': ['g', 'g', 'b', 'b', 'b', 'g', 'g', 'g', 'g'],
        'blue': ['g', 'b', 'b', 'b', 'b', 'b', 'g', 'g', 'b'],
        'red': ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
        'orange': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        }

def test_iterate_through_scrambles_for_testing():
    scrambles = [
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'L2']
    ]


    assert iterate_through_scrambles_for_testing(scrambles)[0].cube_state == {
        'white': ['o', 'r', 'r', 'y', 'g', 'r', 'b', 'w', 'w'],
        'yellow': ['b', 'o', 'r', 'b', 'g', 'o', 'o', 'g', 'y'],
        'green': ['w', 'b', 'o', 'r', 'g', 'g', 'b', 'y', 'g'],
        'blue': ['b', 'g', 'o', 'y', 'r', 'b', 'y', 'g', 'b'],
        'red': ['w', 'y', 'g', 'b', 'y', 'o', 'w', 'r', 'r'],
        'orange': ['y', 'w', 'y', 'w', 'r', 'o', 'w', 'w', 'o']
        }

    assert iterate_through_scrambles_for_testing(scrambles)[1].cube_state == {
        'white': ['b', 'r', 'r', 'y', 'g', 'r', 'o', 'g', 'w'],
        'yellow': ['o', 'o', 'r', 'b', 'g', 'o', 'b', 'w', 'y'],
        'green': ['r', 'b', 'o', 'r', 'g', 'g', 'o', 'y', 'g'],
        'blue': ['b', 'g', 'b', 'y', 'w', 'b', 'y', 'g', 'b'],
        'red': ['y', 'o', 'w', 'r', 'w', 'y', 'g', 'b', 'r'],
        'orange': ['y', 'w', 'y', 'w', 'r', 'o', 'w', 'w', 'o']
        }

    assert do_scramble(['L2'], iterate_through_scrambles_for_testing(scrambles)[0]).cube_state == iterate_through_scrambles_for_testing(scrambles)[1].cube_state


def test_sanitize():
    moves = [
        [['Dp', 'I'], ['Dp'], ['D', 'R'], ['D', 'Rp'], ['D2', 'F'], ['D2', 'Fp'], ['D2', 'F'], ['D2', 'Fp']],
        [['Dp'], ['D']]
    ]

    assert sanitize(moves[0]) == [['Dp'], ['D', 'R'], ['D', 'Rp'], ['D2', 'F'], ['D2', 'Fp']]
    assert sanitize(moves[1]) == [['Dp'], ['D']]

def test_generate_random_scramble():
    random.seed(0)
    random_scrambles = []
    for i in range(5):
        random_scrambles.append(generate_random_scramble())

    assert random_scrambles[0] == ['R2', 'U2', 'Fp', 'L2', 'D2', 'R2', 'Dp', 'Bp', 'Rp', 'L2'] 
    assert random_scrambles[1] == ['L', 'Dp', 'L', 'D', 'Fp', 'B2', 'L', 'Dp', 'F', 'Lp']
    assert random_scrambles[2] == ['D2', 'B2', 'D', 'Bp', 'U2', 'Lp', 'Rp', 'B2', 'D2', 'F2']
    assert random_scrambles[3] == ['L2', 'Fp', 'U', 'B2', 'R', 'F', 'R2', 'D2', 'Lp', 'Up']
    assert random_scrambles[4] == ['Lp', 'F', 'Rp', 'Up', 'L', 'B2', 'F2', 'Lp', 'D2', 'B2']
