import random
import numpy as np
from cubeai.cube.moves import Cube, CrossSolver
from cubeai.test.helper_functions import ( 
    do_scramble, 
    iterate_through_scrambles_for_testing, 
    cross_solver
)

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


def test_identify_cross_edge_type():
    scrambles = [
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'L', 'L'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'L', 'L', 'Rp'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'Lp', 'Up', 'B'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B', 'Rp', 'D', 'Rp', 'D', 'R2']
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)
        
    assert cubes[0].identify_cross_edge_type() == [
        {'_seven_type': {'orange': ['g', 'r']}},
        {'_three_type': {'orange': ['b', 'g']}},
        {'_one_type': {'orange': ['y', 'b']}},
        {'_top_type': {}},
        {'_five_type': {}},
        {'bottum_type': {'white_r': ['r', 'o']}}
    ]
        
    assert cubes[1].identify_cross_edge_type() == [
        {'_seven_type': {'orange': ['g', 'r']}},
        {'_three_type': {'orange': ['b', 'g']}},
        {'_one_type': {'orange': ['y', 'b']}},
        {'_top_type': {'yellow_r': ['r', 'o']}},
        {'_five_type': {}},
        {'bottum_type': {}}
    ]
        
        
    assert cubes[2].identify_cross_edge_type() == [
        {'_seven_type': {'orange': ['g', 'b']}},
        {'_three_type': {}},
        {'_one_type': {'orange': ['y', 'g']}},
        {'_top_type': {'yellow_r': ['r', 'o']}},
        {'_five_type': {'orange': ['w', 'r']}},
        {'bottum_type': {}}
    ]
    
    assert cubes[3].identify_cross_edge_type() == [
        {'_seven_type': {'green': ['r', 'o'], 'orange': ['g', 'r']}},
        {'_three_type': {'blue': ['r', 'b']}},
        {'_one_type': {}},
        {'_top_type': {'yellow_b': ['b', 'g']}},
        {'_five_type': {}},
        {'bottum_type': {}}
    ]

    assert cubes[4].identify_cross_edge_type() == [
        {'_seven_type': {}},
        {'_three_type': {'green': ['o', 'o']}},
        {'_one_type': {}},
        {'_top_type': {'yellow_b': ['b', 'g']}},
        {'_five_type': {'red': ['w', 'r'], 'blue': ['w', 'b']}},
        {'bottum_type': {}}
    ]

def test_combo():
    scrambles = [
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'B2', 'Rp', 'F','R'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'Bp'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'B2'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'B'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'F2'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'Fp'],
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B', 'Rp', 'D', 'Rp', 'D', 'R2']

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

    assert cubes[7].combo() == [
        ['_three_type', 'green', 'o', 'o'],
        ['_top_type', 'yellow_b', 'b', 'g'],
        ['_five_type', 'red', 'w', 'r'],
        ['_five_type', 'blue', 'w', 'b']
        ]
    
def test_seven_three_orientation_delta():
    many_scrambles = [
            ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2'], # seven/three/one/bottum
            ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B'], # seven/one/top/bottum
            ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B', 'Rp', 'D'] # seven/top/five/bottum
        ]
    
    cubes = iterate_through_scrambles_for_testing(many_scrambles)
    
    assert cubes[0].seven_three_orientation_delta(0, 3) == ['Dp']
    assert cubes[0].seven_three_orientation_delta(0, 2) == ['U']
    assert cubes[0].seven_three_orientation_delta(1, 3) == ['I']
    assert cubes[0].seven_three_orientation_delta(1, 2) == ['Up']

    assert cubes[1].seven_three_orientation_delta(0, 3) == ['D2']
    assert cubes[1].seven_three_orientation_delta(0, 1) == ['U']
    assert cubes[1].seven_three_orientation_delta(0, 2) == ['U2']

    assert cubes[2].seven_three_orientation_delta(0, 3) == ['D2']
    assert cubes[2].seven_three_orientation_delta(0, 1) == ['U2']
    assert cubes[2].seven_three_orientation_delta(0, 2) == ['D2']

def test_combine_seven_three_orientation_delta():
    many_scrambles = [
            ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2'], # seven/three/one/bottum
            ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B'], # seven/one/top/bottum
            ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B', 'Rp', 'D'], # seven/top/five/bottum
            ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B', 'Rp', 'D', 'Rp', 'D', 'R2'] # three/top/five/five

        ]
    
    cubes = iterate_through_scrambles_for_testing(many_scrambles)
    
    assert cubes[0].combine_seven_three_orientation_delta(0, 3, 2) == ['Dp', 'U']
    assert cubes[0].combine_seven_three_orientation_delta(1, 3, 2) == ['I', 'Up']

    assert cubes[1].combine_seven_three_orientation_delta(0, 3, 1) == ['D2', 'U']
    assert cubes[1].combine_seven_three_orientation_delta(0, 3, 2) == ['D2', 'U2']

    assert cubes[2].combine_seven_three_orientation_delta(0, 1, 2) == ['U2', 'D2']
    assert cubes[2].combine_seven_three_orientation_delta(0, 1, 3) == ['U2', 'D2']

    assert cubes[3].combine_seven_three_orientation_delta(0, 1, 2) == ['U', 'D2']
    assert cubes[3].combine_seven_three_orientation_delta(0, 1, 3) == ['U', 'Dp']

def test_seven_type_cross_solver():
    scrambles = [
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'B2', 'Rp', 'F','R'], # seven/seven/bottum/bottum
        ['Rp', 'Fp', 'Lp', 'R', 'Bp', 'Rp', 'F', 'R', 'Fp'], # seven/seven/seven/bottum
        ['Rp', 'Fp', 'Lp', 'R', 'Bp', 'Rp'], # seven/seven/seven/seven
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'Bp'], # seven/one/bottum/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2'], # seven/three/one/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'B'], # seven/one/top/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'B2'], # seven/seven/one/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B', 'Rp', 'D'] # seven/top/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].seven_type_cross_solver() == [['I', 'B'], ['I', 'B'], ['Dp', 'F'], ['Dp', 'F']]
    assert cubes[1].seven_type_cross_solver() == [['I', 'L'], ['I', 'B'], ['I', 'F']]
    assert cubes[2].seven_type_cross_solver() == [['I', 'L'], ['I', 'B'], ['I', 'R'], ['I', 'F']]
    assert cubes[3].seven_type_cross_solver() == [['U', 'Dp', 'F'], ['U', 'Dp', 'F']]
    assert cubes[4].seven_type_cross_solver() == [['U', 'Dp', 'F']]
    assert cubes[5].seven_type_cross_solver() == [['U', 'Dp', 'F'], ['U2', 'Dp', 'F']]
    assert cubes[6].seven_type_cross_solver() == [['Up', 'I', 'B'], ['U', 'Dp', 'F']]
    assert cubes[7].seven_type_cross_solver() == [['U2', 'D2', 'F'], ['U2', 'D2', 'F']]



def test_three_type_cross_solver():
    scrambles = [
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'F2'], # three/three/one/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'Fp'], # three/one/top/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2'], # seven/three/one/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'U', 'Fp', 'L', 'F', 'Lp'], # seven/seven/three/bottum
        ['Fp', 'R', 'Fp', 'Bp', 'L', 'Bp'], # one/one/one/one
        ['Fp', 'R', 'Fp', 'Bp', 'L', 'Bp', 'Fp', 'Rp', 'Bp', 'Fp', 'Lp', 'F2', 'F', 'B2'], # three/three/three/three
        ['D', 'Fp', 'Lp', 'B', 'D2', 'L', 'B', 'Lp', 'Bp'], # seven/seven/seven/three
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'D', 'B', 'Rp', 'D', 'Rp', 'D', 'R2'] # three/top/five/five
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].three_type_cross_solver() == [['U', 'Dp', 'Fp'], ['Up', 'I', 'Bp']]
    assert cubes[1].three_type_cross_solver() == [['Up', 'I', 'Bp'], ['U2', 'I', 'Bp']]
    assert cubes[2].three_type_cross_solver() == [['Up', 'I', 'Bp']]
    assert cubes[3].three_type_cross_solver() == [['I', 'Bp']]
    assert cubes[4].three_type_cross_solver() == None
    assert cubes[5].three_type_cross_solver() == [['I', 'Rp'], ['I', 'Fp'], ['I', 'Lp'], ['I', 'Bp']]
    assert cubes[6].three_type_cross_solver() == [['I', 'Lp'], ['I', 'Bp']]
    assert cubes[7].three_type_cross_solver() == [['U', 'D2', 'Rp'], ['U', 'Dp', 'Rp']]

def test_one_orientation_delta():
    scrambles = [
        ['F2', 'Rp', 'D', 'Bp', 'Fp', 'Rp', 'L', 'L', 'R', 'B2', 'F', 'D2', 'R'], # one/top/five/bottum
        ['R', 'F', 'L', 'Bp', 'U', 'B'], # one/five/five/bottum
        ['R', 'F', 'L', 'Bp', 'U', 'B', 'Dp'], # one/five/five/bottum
        ['R', 'F', 'L', 'Bp', 'U', 'B', 'Dp', 'Dp'] # one/five/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].one_orientation_delta(0,1) == ['I']
    assert cubes[0].one_orientation_delta(0,2) == ['D']
    assert cubes[0].one_orientation_delta(0,3) == ['D', 'Dp']

    assert cubes[1].one_orientation_delta(0,1) == ['D']
    assert cubes[1].one_orientation_delta(0,2) == ['D2']
    assert cubes[1].one_orientation_delta(0,3) == ['I']


    assert cubes[2].one_orientation_delta(0,1) == ['D2']
    assert cubes[2].one_orientation_delta(0,2) == ['Dp']
    assert cubes[2].one_orientation_delta(0,3) == ['D', 'Dp']

    assert cubes[3].one_orientation_delta(0,1) == ['Dp']
    assert cubes[3].one_orientation_delta(0,2) == ['I']
    assert cubes[3].one_orientation_delta(0,3) == ['I']

def test_top_orientation_delta():
    scrambles = [
        ['L', 'D', 'L', 'Dp', 'B', 'Dp'], # top/five/bottum/bottum
        ['F2', 'Rp', 'D', 'Bp', 'Fp', 'Rp', 'L', 'L'], # seven/top/five/five
        ['F2', 'Rp', 'D', 'Bp', 'Fp', 'Rp', 'L', 'L', 'R', 'B2'], #seven/three/one/top
        ['L', 'D', 'L', 'Dp', 'B'], # top/five/bottum/bottum
        ['L', 'D', 'L', 'Dp', 'B', 'D'] # top/five/bottum/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].top_orientation_delta(0,1) == ['D2']
    assert cubes[0].top_orientation_delta(0,2) == ['D']
    assert cubes[0].top_orientation_delta(0,3) == ['D']

    assert cubes[1].top_orientation_delta(1,2) == ['D']
    assert cubes[1].top_orientation_delta(1,3) == ['D2']

    assert cubes[2].top_orientation_delta(3,0) == ['I']
    assert cubes[2].top_orientation_delta(3,1) == ['I']
    assert cubes[2].top_orientation_delta(3,2) == ['I']

    assert cubes[3].top_orientation_delta(0,1) == ['D']
    assert cubes[3].top_orientation_delta(0,2) == ['I']
    assert cubes[3].top_orientation_delta(0,3) == ['I']

    assert cubes[4].top_orientation_delta(0,1) == ['I']
    assert cubes[4].top_orientation_delta(0,2) == ['Dp']
    assert cubes[4].top_orientation_delta(0,3) == ['Dp']

def test_one_type_cross_solver():
    scrambles = [
        ['L', 'D', 'L', 'Dp', 'B', 'Dp', 'R2', 'D'], # one/top/bottum/bottum
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'D2', 'F2'], # three/three/one/bottum
        ['L', 'D', 'L', 'Dp', 'B', 'Dp', 'R2', 'D2', 'L'], # seven/one/bottum/bottum
        ['Fp', 'R', 'Fp', 'Bp', 'L', 'Bp'], # one/one/one/one
        ['Fp', 'R', 'Fp', 'Bp', 'L', 'Bp', 'F', 'Lp', 'Bp'], # seven/three/top/one
        ['F', 'Lp', 'B', 'R', 'Dp', 'Rp', 'Dp'] # seven/one/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].one_type_cross_solver() == [['I', 'R'], ['I', 'Rp'], ['D', 'R'], ['D', 'Rp'], ['Dp', 'R'], ['Dp', 'Rp']]
    assert cubes[1].one_type_cross_solver() == [['I', 'R'], ['I', 'Rp']]
    assert cubes[2].one_type_cross_solver() == [['D', 'R'], ['D', 'Rp'], ['Dp', 'R'], ['Dp', 'Rp'], ['I', 'R'], ['I', 'Rp']]
    assert cubes[3].one_type_cross_solver() == [['I', 'F'], ['I', 'Fp'], ['I', 'L'], ['I', 'Lp'], ['I', 'B'], ['I', 'Bp'], ['I', 'R'], ['I', 'Rp']]
    assert cubes[4].one_type_cross_solver() == [['I', 'R'], ['I', 'Rp']]
    assert cubes[5].one_type_cross_solver() == [['I', 'L'], ['I', 'Lp'], ['I', 'L'], ['I', 'Lp']]

def test_top_type_cross_solver():
    scrambles = [
        ['L', 'D', 'L', 'Dp', 'B', 'Dp', 'R2', 'D'], # one/top/bottum/bottum
        ['Fp', 'R', 'Fp', 'Bp', 'L', 'Bp', 'F', 'Lp', 'Bp'], # seven/three/one/top
        ['R', 'F', 'Dp', 'F', 'R2', 'Dp'], # top/top/five/bottum
        ['R', 'F', 'Dp', 'F', 'R2'] # top/top/five/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].top_type_cross_solver() == [['I', 'L'], ['I', 'Lp'], ['I', 'L'], ['I', 'Lp']]
    assert cubes[1].top_type_cross_solver() == [['I', 'B'], ['I', 'Bp']]
    assert cubes[2].top_type_cross_solver() == [['Dp', 'R'], ['Dp', 'Rp'], ['D', 'R'], ['D', 'Rp'], ['D2', 'F'], ['D2', 'Fp'], ['D2', 'F'], ['D2', 'Fp']]
    assert cubes[3].top_type_cross_solver() == [['D2', 'R'], ['D2', 'Rp'], ['I', 'R'], ['I', 'Rp'], ['D', 'F'], ['D', 'Fp'], ['D', 'F'], ['D', 'Fp']]

def test_five_orientation_delta():
    scrambles = [
        ['R', 'F', 'Dp', 'F', 'R2'], # top/top/five/bottum
        ['R', 'F', 'Bp', 'L', 'U2', 'L'] # seven/one/top/five
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].five_orientation_delta(2,0) == ['U2']
    assert cubes[0].five_orientation_delta(2,1) == ['U']
    assert cubes[0].five_orientation_delta(2,3) == ['I']

    assert cubes[1].five_orientation_delta(3,0) == ['I']
    assert cubes[1].five_orientation_delta(3,1) == ['U']
    assert cubes[1].five_orientation_delta(3,2) == ['Up']

def test_five_type_cross_solver():
    scrambles = [
        ['R', 'F', 'Dp', 'F', 'R2'], # top/top/five/bottum
        ['R', 'F', 'Bp', 'L', 'U2', 'L'], # seven/one/top/five
        ['R2', 'Fp', 'Dp', 'B', 'D2', 'Lp', 'Fp', 'D', 'F', 'R2', 'Dp', 'B', 'Rp', 'D'], # seven/top/five/bottum
        ['F2', 'Rp', 'D', 'Bp', 'Fp', 'Rp', 'L', 'L', 'R', 'B2', 'F', 'D2', 'R'], # one/top/five/bottum
        ['R', 'F', 'L', 'Bp', 'U', 'B'], # one/five/five/bottum
        ['L', 'D', 'L', 'Dp', 'B', 'Dp'], # top/five/bottum/bottum
        ['F2', 'Rp', 'D', 'Bp', 'Fp', 'Rp', 'L', 'L'] # seven/top/five/five
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].five_type_cross_solver() == [['U2', 'L'], ['U2', 'Lp'], ['U', 'L'], ['U', 'Lp']]
    assert cubes[1].five_type_cross_solver() == [['U', 'F'], ['U', 'Fp'], ['Up', 'F'], ['Up', 'Fp']]
    assert cubes[2].five_type_cross_solver() == [['I', 'B'], ['I', 'Bp']]
    assert cubes[3].five_type_cross_solver() == [['U', 'R'], ['U', 'Rp'], ['U2', 'R'], ['U2', 'Rp']]
    assert cubes[4].five_type_cross_solver() == [['U', 'F'], ['U', 'Fp'], ['U2', 'L'], ['U2', 'Lp']]
    assert cubes[5].five_type_cross_solver() == [['U2', 'R'], ['U2', 'Rp']]
    assert cubes[6].five_type_cross_solver() == [['U', 'B'], ['U', 'Bp'], ['U2', 'R'], ['U2', 'Rp']]

def test_bottum_orientation_delta():
    scrambles = [
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'D'], # bottum/bottum/bottum/bottum
        ['D'], # bottum/bottum/bottum/bottum
        ['D2'], # bottum/bottum/bottum/bottum
        ['Dp'], # bottum/bottum/bottum/bottum
        ['F', 'B', 'D2', 'Fp', 'Bp'] # bottum/bottum/bottum/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].bottum_orientation_delta() == None
    assert cubes[1].bottum_orientation_delta() == ['Dp']
    assert cubes[2].bottum_orientation_delta() == ['D2']
    assert cubes[3].bottum_orientation_delta() == ['D']
    assert cubes[4].bottum_orientation_delta() == None

def test_cross_permuted():
    scrambles = [
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2'], # bottum/bottum/bottum/bottum
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'D'], # bottum/bottum/bottum/bottum
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'D2'], # bottum/bottum/bottum/bottum
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'Dp'], # bottum/bottum/bottum/bottum
        ['D'], # bottum/bottum/bottum/bottum
        ['D2'], # bottum/bottum/bottum/bottum
        ['Dp'], # bottum/bottum/bottum/bottum
        ['F', 'B', 'D2', 'Fp', 'Bp'], # bottum/bottum/bottum/bottum
        ['F', 'B', 'D2', 'Fp', 'Bp', 'D'], # bottum/bottum/bottum/bottum
        ['F', 'B', 'D2', 'Fp', 'Bp', 'D2'] # bottum/bottum/bottum/bottum
    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].cross_permuted() == [2, 3] # blue and red
    assert cubes[1].cross_permuted() == [1] # orange
    assert cubes[2].cross_permuted() == [] # none
    assert cubes[3].cross_permuted() == [0] # green
    assert cubes[4].cross_permuted() == [] # none
    assert cubes[5].cross_permuted() == [] # none
    assert cubes[6].cross_permuted() == [] # none
    assert cubes[7].cross_permuted() == [0, 2] # green and blue
    assert cubes[8].cross_permuted() == [] # none
    assert cubes[9].cross_permuted() == [1, 3] # red and orange

def test_bottum_type_cross_solver():
    random.seed(0)
    scrambles = [
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2'], # bottum/bottum/bottum/bottum
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'D'], # bottum/bottum/bottum/bottum
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'D2'], # bottum/bottum/bottum/bottum
        ['F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'Dp'], # bottum/bottum/bottum/bottum
        ['D','F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'Dp'], # bottum/bottum/bottum/bottum
        ['D','F2', 'R2', 'Up', 'R2', 'U2', 'F2', 'D2'], # bottum/bottum/bottum/bottum
        ['D'], # bottum/bottum/bottum/bottum
        ['D2'], # bottum/bottum/bottum/bottum
        ['Dp'], # bottum/bottum/bottum/bottum
        ['F2', 'B2', 'U2', 'F2', 'B2'], # bottum/bottum/bottum/bottum
        ['F2', 'B2', 'U2', 'F2', 'B2', 'D2'], # bottum/bottum/bottum/bottum
        ['F2', 'B2', 'U2', 'F2', 'B2', 'Dp'], # bottum/bottum/bottum/bottum
        ['F2', 'B2', 'U2', 'F2', 'B2', 'D'] # bottum/bottum/bottum/bottum

    ]

    cubes = iterate_through_scrambles_for_testing(scrambles)

    assert cubes[0].bottum_type_cross_solver() == [['R', 'D', 'Rp', 'Dp', 'R']] # alpha green
    assert cubes[1].bottum_type_cross_solver() == [['Dp', 'R', 'D', 'Rp', 'Dp', 'R']] # alpha green
    assert cubes[2].bottum_type_cross_solver() == [['D2', 'R', 'D', 'Rp', 'Dp', 'R']] # alpha green
    assert cubes[3].bottum_type_cross_solver() == [['D', 'R', 'D', 'Rp', 'Dp', 'R']] # alpha green
    assert cubes[4].bottum_type_cross_solver() == [['F', 'D', 'Fp', 'Dp', 'F']] # alpha red
    assert cubes[5].bottum_type_cross_solver() == [['D', 'F', 'D', 'Fp', 'Dp', 'F']] # alpha red
    assert cubes[6].bottum_type_cross_solver() == [['Dp']]
    assert cubes[7].bottum_type_cross_solver() == [['D2']]
    assert cubes[8].bottum_type_cross_solver() == [['D']]
    assert cubes[9].bottum_type_cross_solver() == [['L', 'R', 'D2', 'Lp', 'Rp']] # beta
    assert cubes[10].bottum_type_cross_solver() == [['F', 'B', 'D2', 'Fp', 'Bp']] # beta
    assert cubes[11].bottum_type_cross_solver() == [['Dp', 'F', 'B', 'D2', 'Fp', 'Bp']] # gamma
    assert cubes[12].bottum_type_cross_solver() == [['D', 'F', 'B', 'D2', 'Fp', 'Bp']] # gamma

def test_treeify():
    # 8 moves with len(all_moves) <=5
    _cube = do_scramble(['F2', 'L', 'D2', 'Lp', 'R2', 'U2', 'B2', 'Rp', 'U2', 'F2', 'Rp', 'D', 'B2', 'R', 'F2', 'Bp', 'L', 'F', 'U', 'Dp'])
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
    assert len(k) == int(len(k[0] + k[1] + k[2] + k[3] + k[4] + k[5] + k[6])/2)

 
    # 7 moves with len(all_moves) <=5 (alhtough, this could be done in 5, but i think it will change once i fix the set up move)
    _cube = do_scramble(['R2', 'U2', 'Fp', 'L2', 'D2', 'R2', 'Dp', 'Bp', 'Rp', 'L2'])
    k = cross_solver(_cube, min_move_only=True)
    assert k == [
        [7, ['U2', 'Rp', 'Dp', 'Rp', 'D2', 'R', 'Dp']]
    ]

    # 2 moves with len(all_moves) <=5
    _cube = do_scramble(['R','F'])
    k = cross_solver(_cube, min_move_only=True)
    assert k == [
        [2, ['Fp', 'Rp']]
    ]

    # 1 move with len(all_moves) <=5
    _cube = do_scramble(['D'])
    k = cross_solver(_cube, min_move_only=True)
    assert k == [
        [1, ['Dp']]
    ]
        



    