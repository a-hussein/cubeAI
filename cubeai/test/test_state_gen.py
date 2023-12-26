import random
from cubeai.cube.moves import Cube
from cubeai.test.testing_functions import solved_cube, do_scramble, iterate_through_scrambles_for_testing


def test_generate_states():
    r"""
    
    """
    random.seed(0)

    moves = ['R', 'U', 'F', 'D', 'L', 'B', 'Rp', 'Up', 'Fp', 'Dp', 'Lp', 'Bp']
    cube_states = []
    cube_moves = []
    for state in range(3):
        solved = {
            'white': ['w']*9,
            'yellow': ['y']*9,
            'green': ['g']*9,
            'blue': ['b']*9,
            'red': ['r']*9,
            'orange': ['o']*9
        }
        cube = Cube(solved)
        _cube_moves = []
        
        for move in range(3):
            mv = random.choice(moves)
            _cube_moves.append(mv)
            getattr(cube, mv)()
            
        cube_moves.append(_cube_moves)
        cube_states.append(cube.cube_state)
    assert cube_states[0] == {'white': ['w', 'w', 'g', 'g', 'g', 'w', 'w', 'w', 'w'], 'yellow': ['y', 'y', 'b', 'b', 'b', 'y', 'y', 'y', 'y'], 'green': ['g', 'g', 'y', 'y', 'y', 'g', 'g', 'g', 'g'], 'blue': ['w', 'b', 'b', 'b', 'b', 'b', 'w', 'w', 'b'], 'red': ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], 'orange': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']}
    assert cube_states[1] == {'white': ['r', 'r', 'r', 'w', 'w', 'w', 'g', 'g', 'w'], 'yellow': ['y', 'y', 'o', 'o', 'o', 'b', 'b', 'y', 'y'], 'green': ['r', 'r', 'y', 'g', 'y', 'y', 'y', 'g', 'g'], 'blue': ['w', 'o', 'o', 'w', 'w', 'b', 'b', 'b', 'b'], 'red': ['b', 'b', 'w', 'y', 'b', 'r', 'r', 'r', 'r'], 'orange': ['g', 'g', 'g', 'o', 'o', 'o', 'g', 'w', 'o']}
    assert cube_states[2] == {'white': ['g', 'w', 'g', 'g', 'g', 'w', 'g', 'g', 'w'], 'yellow': ['b', 'b', 'b', 'y', 'b', 'b', 'b', 'y', 'y'], 'green': ['r', 'r', 'r', 'y', 'y', 'g', 'y', 'y', 'g'], 'blue': ['o', 'o', 'o', 'w', 'w', 'b', 'w', 'w', 'b'], 'red': ['w', 'b', 'w', 'r', 'r', 'r', 'r', 'r', 'r'], 'orange': ['y', 'g', 'y', 'o', 'o', 'o', 'o', 'o', 'o']}

def test_edge_count():
    solved = {
        'white': ['w']*9,
        'yellow': ['y']*9,
        'green': ['g']*9,
        'blue': ['b']*9,
        'red': ['r']*9,
        'orange': ['o']*9
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

    assert cube.get_edge_count() == {'white': 1, 'yellow': 0, 'green': 2, 'blue': 0, 'red': 0, 'orange': 1}
    
def test_cross_orientation():
    moves = [
        ['R', 'Dp', 'Rp', 'D', 'R'], # False
        ['D'], # True
        ['R', 'D', 'Lp', 'Dp', 'Rp', 'D', 'L'] # True
    ]
    
    cubes = []
    
    for state in range(3):
        solved = {
            'white': ['w']*9,
            'yellow': ['y']*9,
            'green': ['g']*9,
            'blue': ['b']*9,
            'red': ['r']*9,
            'orange': ['o']*9
        }
        cube = Cube(solved)
        
        for move in range(len(moves[state])):
            getattr(cube, moves[state][move])()
        
        cubes.append(cube)
    
    assert cubes[0].cross_oriented() == False
    assert cubes[1].cross_oriented() == True
    assert cubes[2].cross_oriented() == True


def test_do_scramble():
    scramble = ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R']
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
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'L', 'L']
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

    assert do_scramble(['L', 'L'], iterate_through_scrambles_for_testing(scrambles)[0]).cube_state == iterate_through_scrambles_for_testing(scrambles)[1].cube_state

def test_identify_cross_edge_type():
    scrambles = [
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'L', 'L'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'L', 'L', 'Rp'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'Lp', 'Up', 'B']
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)
        
    assert cubes[0].identify_cross_edge_type() == [
        {'_seven_type': {'orange': ['g', 'r']}},
        {'_three_type': {'orange': ['b', 'g']}},
        {'_one_type': {'orange': ['y', 'b']}},
        {'_five_type': {}},
        {'_top_type': {}},
        {'bottum_type': {'white_r': ['r', 'o']}}
    ]
        
    assert cubes[1].identify_cross_edge_type() == [
        {'_seven_type': {'orange': ['g', 'r']}},
        {'_three_type': {'orange': ['b', 'g']}},
        {'_one_type': {'orange': ['y', 'b']}},
        {'_five_type': {}},
        {'_top_type': {'yellow_r': ['r', 'o']}},
        {'bottum_type': {}}
    ]
        
        
    assert cubes[2].identify_cross_edge_type() == [
        {'_seven_type': {'orange': ['g', 'b']}},
        {'_three_type': {}},
        {'_one_type': {'orange': ['y', 'g']}},
        {'_five_type': {'orange': ['w', 'r']}},
        {'_top_type': {'yellow_r': ['r', 'o']}},
        {'bottum_type': {}}
    ]
    
    assert cubes[3].identify_cross_edge_type() == [
        {'_seven_type': {'green': ['r', 'o'], 'orange': ['g', 'r']}},
        {'_three_type': {'blue': ['r', 'b']}},
        {'_one_type': {}},
        {'_five_type': {}},
        {'_top_type': {'yellow_b': ['b', 'g']}},
        {'bottum_type': {}}
    ]

def test_combo():
    scrambles = [
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B', 'B', 'Rp', 'F','R'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'Bp'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B', 'B'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'F', 'F'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'Fp']
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)
        
    assert cubes[0].combo() == [
        ['_seven_type', 'orange', 'g', 'r'],
        ['_three_type', 'orange', 'b', 'g'],
        ['_one_type', 'orange', 'y', 'b'],
        ['bottum_type', 'white_r', 'r', 'o']
        ]
        
    assert cubes[1].combo() == [
        ['_seven_type', 'red', 'b', 'g'],
        ['_seven_type', 'orange', 'g', 'r'],
        ['bottum_type', 'white_g', 'g', 'b'],
        ['bottum_type', 'white_r', 'r', 'o']
        ]
        
    assert cubes[2].combo() == [
        ['_seven_type', 'orange', 'g', 'r'],
        ['_one_type', 'orange', 'y', 'b'],
        ['bottum_type', 'white_b', 'b', 'g'],
        ['bottum_type', 'white_r', 'r', 'o']
        ]

    assert cubes[3].combo() == [
        ['_seven_type', 'red', 'b', 'g'],
        ['_seven_type', 'orange', 'g', 'r'],
        ['_one_type', 'orange', 'y', 'b'],
        ['bottum_type', 'white_r', 'r', 'o']
        ]
    
    assert cubes[4].combo() == [
        ['_seven_type', 'orange', 'g', 'r'],
        ['_one_type', 'orange', 'y', 'b'],
        ['_top_type', 'yellow_b', 'b', 'g'],
        ['bottum_type', 'white_r', 'r', 'o']
        ]
    assert cubes[5].combo() == [
        ['_three_type', 'red', 'g', 'r'],
        ['_three_type', 'orange', 'b', 'g'],
        ['_one_type', 'orange', 'y', 'b'],
        ['bottum_type', 'white_r', 'r', 'o']
        ]
    assert cubes[6].combo() == [
        ['_three_type', 'orange', 'b', 'g'],
        ['_one_type', 'orange', 'y', 'b'],
        ['_top_type', 'yellow_g', 'g', 'r'],
        ['bottum_type', 'white_r', 'r', 'o']
        ]

def test_seven_three_orientation_delta():
    many_scrambles = [
            ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D'], # seven/three/one/bottum
            ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'D', 'B'], # seven/one/top/bottum
            ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'D', 'B', 'Rp', 'D'] # seven/five/top/bottum
        ]
    
    cubes = iterate_through_scrambles_for_testing(many_scrambles)
    
    assert cubes[0].seven_three_orientation_delta(0, 3, 'bottum') == ['Dp']
    assert cubes[0].seven_three_orientation_delta(0, 2, 'top') == ['U']
    assert cubes[0].seven_three_orientation_delta(1, 3, 'bottum') == ['I']
    assert cubes[0].seven_three_orientation_delta(1, 2, 'top') == ['Up']

    assert cubes[1].seven_three_orientation_delta(0, 3, 'bottum') == ['D', 'D']
    assert cubes[1].seven_three_orientation_delta(0, 1, 'top') == ['U']
    assert cubes[1].seven_three_orientation_delta(0, 2, 'top') == ['U', 'U']

    assert cubes[2].seven_three_orientation_delta(0, 3, 'bottum') == ['D', 'D']
    assert cubes[2].seven_three_orientation_delta(0, 1, 'bottum') == ['D', 'D']
    assert cubes[2].seven_three_orientation_delta(0, 2, 'top') == ['U', 'U']


def test_seven_type_cross_solver():
    scrambles = [
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B', 'B', 'Rp', 'F','R'], # seven/seven/bottum/bottum
        ['Rp', 'Fp', 'Lp', 'R', 'Bp', 'Rp', 'F', 'R', 'Fp'], # seven/seven/seven/bottum
        ['Rp', 'Fp', 'Lp', 'R', 'Bp', 'Rp'], # seven/seven/seven/seven
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'Bp'], # seven/one/bottum/bottum
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D'], # seven/three/one/bottum
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B'], # seven/one/top/bottum
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B', 'B'] # seven/seven/one/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].seven_type_cross_solver() == [['I', 'B'], ['I', 'B'], ['Dp', 'F'], ['Dp', 'F']]
    assert cubes[1].seven_type_cross_solver() == [['I', 'L'], ['I', 'B'], ['I', 'F']]
    assert cubes[2].seven_type_cross_solver() == [['L'], ['B'], ['R'], ['F']]
    assert cubes[3].seven_type_cross_solver() == [['U', 'Dp', 'F'], ['U', 'Dp', 'F']]
    assert cubes[4].seven_type_cross_solver() == [['U', 'Dp', 'F']]
    assert cubes[5].seven_type_cross_solver() == [['U', 'Dp', 'F'], ['U', 'U', 'Dp', 'F']]
    assert cubes[6].seven_type_cross_solver() == [['Up', 'I', 'B'], ['U', 'Dp', 'F']]


def test_three_type_cross_solver():
    scrambles = [
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B', 'B', 'Rp', 'F','R'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'Bp'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B', 'B'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'B'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'F', 'F'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'Fp']
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].three_type_cross_solver() == [['I', 'Bp']]
    assert cubes[1].three_type_cross_solver() == None
    assert cubes[2].three_type_cross_solver() == None
    assert cubes[3].three_type_cross_solver() == None
    assert cubes[4].three_type_cross_solver() == None
    assert cubes[5].three_type_cross_solver() == [['Dp', 'Fp'], ['I', 'Bp']]
    assert cubes[6].three_type_cross_solver() == [['I', 'Bp']]
