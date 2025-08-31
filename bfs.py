from typing import Tuple
from collections import deque
from puzzle_moves import moves, is_valid_move, is_solvable

def bfs(start_state:Tuple[int, ...], goal_state:Tuple[int, ...]) -> str:
    "Breadth First Search"
    if (is_solvable(start_state, goal_state) == False):
       return ""
    
    queue = deque([(start_state, "")])  # (state, path)
    visited = set([start_state])

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path

        zero_index = state.index(0)

        for move, shift in moves.items():
            if is_valid_move(zero_index, move):
                new_index = zero_index + shift
                state_list = list(state)

                # Swap blank with neighbor
                state_list[zero_index], state_list[new_index] = state_list[new_index], state_list[zero_index]

                new_state = tuple(state_list)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + move))

    return ""


# -------------------- RUN EXAMPLE --------------------
if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)
    goal_state = (1, 2, 3, 
                  4, 5, 6, 
                  7, 8, 0)
    
    path = bfs(start_state, goal_state)
    if path:
        print("Solution found in",len(path),"moves:",path)
    else:
        print("No solution found.")