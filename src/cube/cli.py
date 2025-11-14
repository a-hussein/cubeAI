# cli entry point

# import argparse
# from typing import Optional

# from .cube_state import Cube
# from .cross_solver import CrossSolver
# from .search import bfs_shortest_path


# def parse_args() -> argparse.Namespace:
#     parser = argparse.ArgumentParser(description="Rubik's Cube cross solver CLI")
#     parser.add_argument(
#         "--scramble",
#         type=str,
#         help="Scramble moves, e.g. 'R U F' (space-separated). If omitted, use a default or random.",
#     )
#     parser.add_argument(
#         "--method",
#         choices=["heuristic", "bfs"],
#         default="heuristic",
#         help="Which solver to use for cross.",
#     )
#     return parser.parse_args()


# def main() -> None:
#     args = parse_args()

#     # Here you should:
#     # 1. Create a Cube in the solved state
#     # 2. Apply scramble if provided
#     cube = Cube(state=...)  # use your existing solved state
#     if args.scramble:
#         # convert scramble string to moves and apply


#     if args.method == "heuristic":
#         solver = CrossSolver()
#         solution = solver.solve(cube)
#         print(f"Heuristic solution ({solution.length} moves): {' '.join(solution.moves)}")
#     else:
#         # BFS method: you plug in your existing goal and move generator
#         result = bfs_shortest_path(
#             cube,
#             is_goal=...,        # your is_cross_solved
#             expand_moves=...,   # your allowed moves
#             max_depth=8,
#         )
#         if result is None:
#             print("No solution found within depth limit.")
#         else:
#             print(f"BFS solution ({result.depth} moves): {' '.join(result.solution)}")


# if __name__ == "__main__":
#     main()


# make
# run:
# 	uv run python -m rubik_cross_solver.cli --method heuristic --scramble "R U F'"
