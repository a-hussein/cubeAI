from copy import deepcopy
from cubeai.cube.moves import Cube, CrossSolver
import random


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
    if moves is not None:
        for sublist in moves:
            cleaned_sublist = [item for item in sublist if item != 'I']
            cleaned_tuple = tuple(cleaned_sublist)
            if cleaned_tuple not in seen:
                unique_list.append(cleaned_sublist)
                seen.add(cleaned_tuple)
    else:
        pass
    return unique_list

def generate_random_scramble(num_moves=10):
    moves = ['R', 'U', 'F', 'D', 'L', 'B', 'Rp', 'Up', 'Fp', 'Dp', 'Lp', 'Bp', 'R2', 'U2', 'F2', 'D2', 'L2', 'B2']
    scramble = []
    while len(scramble) < num_moves:
        mv = random.choice(moves)
        if len(scramble) == 0:
            scramble.append(mv)
        elif len(scramble) > 0 and mv[0] != scramble[-1][0]: # check if first subletter of the moveset (F2 is a move set) is same as prior (you dont want F2 followed by F for example)
            scramble.append(mv)
        else:
            continue
    return scramble

def cross_solver(cube, min_move_only=True, max_num_of_moves_in_solution=10):
    """
    An easier way to streamline the cross_solver. Usefulwith testing.
    If min_move_only = True, then the next param doesn't matter.
    Outputs a list of potential solution(s) with repeats removed and sorted.
    """
    solver = CrossSolver()
    solver.treeify(cube, [])
    _solutions = solver.solutions
    
    unique_solutions = [list(t) for t in set(tuple(inner_list) for inner_list in _solutions)]
    solns = [[len(solution), solution] for solution in unique_solutions]
    sorted_solns = sorted(solns, key=lambda x: x[0])
    
    k=[]
    for i in sorted_solns:
        if i[0] <= max_num_of_moves_in_solution:
            k.append(i)
            
    min_k = min([i[0] for i in k])
    if min_move_only == True:
        min_move_only = min_k
        k = [i for i in k if i[0] == min_k]
    else:
        k = [i for i in k if i[0]]
        
    return k
