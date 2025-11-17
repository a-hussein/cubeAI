# # src/rubik_cross_solver/cross_solver.py
# from dataclasses import dataclass
# from typing import List

# from .cube_state import Cube, Move


# @dataclass
# class CrossSolution:
#     moves: List[Move]
#     length: int


# @dataclass
# class CrossSolver:
#     """
#     Implements your current 'how Ayman solves the cross' logic.
#     """
#     # You can add config here later if needed (e.g., preferred color, heuristic toggles)

#     def solve(self, cube: Cube) -> CrossSolution:
#         """
#         Return a solution for the cross starting from the given cube state.

#         This function should reuse your existing logic.
#         """
#         # 🔁 Call your current functions / scripts here,
#         # refactored into smaller helper functions as needed.
#         solution_moves: List[Move] = []

#         # e.g., pseudo:
#         # solution_moves = plan_cross(cube)

#         return CrossSolution(moves=solution_moves, length=len(solution_moves))

from .engine_solver import TreeNode


class CrossSolver:
    def __init__(self):
        self.solutions = []

    def treeify(self, cube, cur_moves):
        from .helpers import do_scramble, sanitize

        _combo_dict = {
            "_seven_type": "seven_type_cross_solver",
            "_three_type": "three_type_cross_solver",
            "_one_type": "one_type_cross_solver",
            "_top_type": "top_type_cross_solver",
            "_five_type": "five_type_cross_solver",
        }

        _combo = cube.combo()
        _combo_list = []
        for i in _combo:
            _combo_list.append(i[0])

        level = []
        for _combo_type in _combo_list:
            if _combo_type != "bottum_type":
                level.append(TreeNode(_combo_type))

        # print('combo types:', [[l.val, l.children] for l in level])
        for node in level:
            node.children = getattr(cube, _combo_dict[node.val])()
            node.children = sanitize(node.children)
            node.children = [TreeNode(tuple(c)) for c in node.children]

        _new_cubes = []
        for node in level:
            for c in node.children:
                _new_cube = do_scramble(c.val, cube)
                c.children = [TreeNode(_new_cube)]
                _new_cube_combo = _new_cube.combo()
                _new_cube_combo_list = []
                for i in _new_cube_combo:
                    _new_cube_combo_list.append(i[0])
                if _new_cube_combo_list.count("bottum_type") == 4:
                    _all_moves = []
                    for move_set in cur_moves + [c.val]:
                        for sub_move in move_set:
                            _all_moves.append(sub_move)
                    final_set_of_moves = _new_cube.bottum_type_cross_solver()
                    if final_set_of_moves is None:  # invesitage this
                        final_set_of_moves = [["I"]]
                        pass
                    self.solutions.append(_all_moves + final_set_of_moves[0])
                    self.solutions = sanitize(self.solutions)
                else:
                    _all_moves = []
                    for move_set in cur_moves + [c.val]:
                        for sub_move in move_set:
                            _all_moves.append(sub_move)
                    if len(_all_moves) <= 6:
                        self.treeify(
                            _new_cube, cur_moves + [c.val]
                        )  # should we return solutions?

        # case for just cross solver only
        if _combo_list.count("bottum_type") == 4:
            final_set_of_moves = cube.bottum_type_cross_solver()
            if final_set_of_moves is None:  # invesitage this
                final_set_of_moves = [["I"]]
                pass
            self.solutions.append(final_set_of_moves[0])  # should we return solutions?
            self.solutions = sanitize(self.solutions)
