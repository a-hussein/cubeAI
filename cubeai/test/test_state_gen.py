import random
from cubeai.cube.moves import Cube
from cubeai.test.testing_functions import iterate_through_scrambles_for_testing


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
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'L', 'L'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'L', 'L', 'Rp'],
        ['R', 'R', 'Fp', 'Dp', 'B', 'D', 'D', 'Lp', 'Fp', 'D', 'F', 'R', 'R', 'D', 'D', 'Lp', 'Up', 'B']
    ]
    
    cubes = iterate_through_scrambles_for_testing(scrambles)
    
    test_set = []
    for cube in cubes:
        test_set.append(cube.identify_cross_edge_type('white'))
    #return test_set
        
    assert test_set[0] == [
        {'_seven_type': {'orange': ['g', 'r']}},
        {'_three_type': {'orange': ['b', 'g']}},
        {'_one_type': {'orange': ['y', 'b']}},
        {'_five_type': {}},
        {'_top_type': {}},
        {'bottum_type': {'white_r': ['r', 'o']}}
    ]
        
    assert test_set[1] == [
        {'_seven_type': {'orange': ['g', 'r']}},
        {'_three_type': {'orange': ['b', 'g']}},
        {'_one_type': {'orange': ['y', 'b']}},
        {'_five_type': {}},
        {'_top_type': {'yellow_r': ['r', 'o']}},
        {'bottum_type': {}}
    ]
        
        
    assert test_set[2] == [
        {'_seven_type': {'orange': ['g', 'b']}},
        {'_three_type': {}},
        {'_one_type': {'orange': ['y', 'g']}},
        {'_five_type': {'orange': ['w', 'r']}},
        {'_top_type': {'yellow_r': ['r', 'o']}},
        {'bottum_type': {}}
    ]
    
    assert test_set[3] == [
        {'_seven_type': {'green': ['r', 'o'], 'orange': ['g', 'r']}},
        {'_three_type': {'blue': ['r', 'b']}},
        {'_one_type': {}},
        {'_five_type': {}},
        {'_top_type': {'yellow_b': ['b', 'g']}},
        {'bottum_type': {}}
    ]

    
    
