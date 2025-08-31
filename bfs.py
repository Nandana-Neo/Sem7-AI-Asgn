from collections import deque
from puzzle_moves import goal_state, moves, is_valid_move

def bfs(start_state:tuple):
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

    return None

