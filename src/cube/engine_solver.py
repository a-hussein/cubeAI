# from collections import deque
# from dataclasses import dataclass
# from typing import Callable, Deque, Dict, List, Optional, Tuple

# from .cube_state import Cube, Move


# @dataclass
# class SearchResult:
#     solution: List[Move]
#     expanded_nodes: int
#     depth: int


# def bfs_shortest_path(
#     start: Cube,
#     is_goal: Callable[[Cube], bool],
#     expand_moves: Callable[[Cube], List[Move]],
#     max_depth: int = 8,
# ) -> Optional[SearchResult]:
#     """
#     BFS from the start cube to any goal state, returning the shortest sequence of moves.

#     - is_goal: checks if cross is solved, using your existing 'is_cross_solved' logic.
#     - expand_moves: returns legal moves from a given cube (e.g., limited face set).
#     """
#     start_key = cube_key(start)
#     queue: Deque[Tuple[Cube, List[Move]]] = deque([(start.copy(), [])])
#     visited: Dict[str, int] = {start_key: 0}
#     expanded = 0

#     while queue:
#         cube, path = queue.popleft()
#         depth = len(path)

#         if depth > max_depth:
#             continue

#         if is_goal(cube):
#             return SearchResult(solution=path, expanded_nodes=expanded, depth=depth)

#         expanded += 1

#         for move in expand_moves(cube):
#             new_cube = cube.copy()
#             new_cube.apply_move(move)
#             key = cube_key(new_cube)

#             if key in visited and visited[key] <= depth + 1:
#                 continue

#             visited[key] = depth + 1
#             queue.append((new_cube, path + [move]))

#     return None


# def cube_key(cube: Cube) -> str:
#     """Convert a cube to a hashable key. Reuse your existing encoding."""
#     # e.g., ''.join(cube.state)
#     return "".join(cube.state)
