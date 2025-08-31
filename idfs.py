from typing import Tuple
from puzzle_moves import moves, is_valid_move, is_solvable


def depth_limited_dfs(start_state: Tuple[int, ...], goal_state: Tuple[int, ...], limit: int):
    """Non-recursive Depth Limited DFS using a stack"""
    stack = [(start_state, "", 0)]
    # (state, path_so_far, depth)

    visited = set([start_state]) 

    while stack:
        state, path, depth = stack.pop()

        if state == goal_state:
            return path

        if depth < limit:
            zero_index = state.index(0)

            for move, shift in moves.items():
                if is_valid_move(zero_index, move):
                    new_index = zero_index + shift
                    state_list = list(state)

                    # Swap blank
                    state_list[zero_index], state_list[new_index] = state_list[new_index], state_list[zero_index]
                    new_state = tuple(state_list)

                    if new_state not in visited:
                        visited.add(new_state)
                        stack.append((new_state, path + move, depth + 1))

    return None


def idfs(start_state: Tuple[int, ...], goal_state: Tuple[int, ...], max_depth: int = 50) -> str:
    """Iterative Deepening DFS"""

    if (is_solvable(start_state, goal_state) == False):
       return ""
    
    for depth in range(max_depth + 1):
        result = depth_limited_dfs(start_state, goal_state, depth)
        if result:
            return result
    return ""

# -------------------- RUN EXAMPLE --------------------
if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)
    goal_state = (1, 2, 3, 
                  4, 5, 6, 
                  7, 8, 0)

    path = idfs(start_state, goal_state)
    if path:
        print("Solution found in",len(path),"moves:",path)
    else:
        print("No solution found.")

