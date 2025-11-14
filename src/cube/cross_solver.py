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
