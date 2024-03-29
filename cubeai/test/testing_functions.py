from copy import deepcopy
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

def do_scramble(moves, cube=solved_cube(), in_place=False):
 
    if in_place == False:
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

    for sublist in moves:
        cleaned_sublist = [item for item in sublist if item != 'I']
        cleaned_tuple = tuple(cleaned_sublist)
        if cleaned_tuple not in seen:
            unique_list.append(cleaned_sublist)
            seen.add(cleaned_tuple)

    return unique_list
