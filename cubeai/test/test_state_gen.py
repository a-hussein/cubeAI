import random
from cubeai.cube.moves import Cube


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
    