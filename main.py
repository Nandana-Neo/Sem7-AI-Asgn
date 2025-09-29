from bfs import bfs
from dfs import dfs
from idfs import idfs
from a_star import a_star_search
import sys

def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    initial_state = tuple(int(num) for i in range(3) for num in lines[i].split())
    goal_state  = tuple(int(num) for i in range(3, 6) for num in lines[i].split())
    return initial_state, goal_state

if len(sys.argv) < 2:
    print("Format: python3 main.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
initial_state, goal_state = read_input(input_file)

print("---------------------BFS SOLUTION---------------------")

solution_bfs = bfs(initial_state, goal_state)
if solution_bfs:
    print("Solution found in", len(solution_bfs), "moves:", solution_bfs)
else:
    print("No solution exists")


print("---------------------DFS SOLUTION---------------------")

solution_dfs = dfs(initial_state, goal_state)
if solution_dfs:
    print("Solution found in", len(solution_dfs), "moves:", solution_dfs)
else:
    print("No solution exists")

print("---------------------IDFS SOLUTION---------------------")

solution_idfs = idfs(initial_state, goal_state)
if solution_idfs:
    print("Solution found in", len(solution_idfs), "moves:", solution_idfs)
else:
    print("No solution exists")

print("---------------A STAR SEARCH SOLUTION--------------")

initial_state_list = [list(initial_state[i*3:(i+1)*3]) for i in range(3)]
goal_state_list = [list(goal_state[i*3:(i+1)*3]) for i in range(3)]
solution_a_star = a_star_search(initial_state_list, goal_state_list)

if solution_a_star:
    moves_str = "".join(solution_a_star)
    print(f"Solution found in {len(solution_a_star)} moves: {moves_str}")
else:
    print("No solution exists")