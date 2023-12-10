from cubeai.cube.moves import Cube


def solved_cube():
    solved = {
        'white': ['w']*9,
        'yellow': ['y']*9,
        'green': ['g']*9,
        'blue': ['b']*9,
        'red': ['r']*9,
        'orange': ['o']*9
    }

    solved_cube = Cube(solved)
    
    return solved_cube

def do_scramble(moves):
    cubes = []

    cube = solved_cube()
        
    for move in range(len(moves)):
        if move == '':
            pass
        getattr(cube, moves[move])()

    return cube

def iterate_through_scrambles_for_testing(many_scrambles):
    cubes = []
    for scramble in range(len(many_scrambles)):
        cube = do_scramble(many_scrambles[scramble])
        cubes.append(cube)
    return cubes
