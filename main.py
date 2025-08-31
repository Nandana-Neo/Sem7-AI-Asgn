from bfs import bfs

# Example
initial_state = (2, 1, 5,
                 3, 4, 0,
                 6, 7, 8)

solution = bfs(initial_state)

if solution:
    print("Solution found in", len(solution), "moves:", solution)
else:
    print("No solution exists")