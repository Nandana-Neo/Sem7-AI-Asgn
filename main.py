from bfs import bfs
from dfs import dfs
from idfs import idfs

# Example
initial_state = (1, 2, 0,
                 4, 5, 3,
                 7, 8, 6)


print("---------------------BFS SOLUTION---------------------")

solution_bfs = bfs(initial_state)
if solution_bfs:
    print("Solution found in", len(solution_bfs), "moves:", solution_bfs)
else:
    print("No solution exists")


print("---------------------DFS SOLUTION---------------------")

solution_dfs = dfs(initial_state)
if solution_dfs:
    print("Solution found in", len(solution_dfs), "moves:", solution_dfs)
else:
    print("No solution exists")

print("---------------------IDFS SOLUTION---------------------")

solution_idfs = idfs(initial_state)
if solution_idfs:
    print("Solution found in", len(solution_idfs), "moves:", solution_idfs)
else:
    print("No solution exists")