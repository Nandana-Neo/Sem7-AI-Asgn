import heapq
import sys

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gx, gy = [(x, y) for x in range(3) for y in range(3) if goal[x][y] == val][0]
                distance += abs(i - gx) + abs(j - gy)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_successors(state):
    moves = [(-1,0,"U"), (1,0,"D"), (0,-1,"L"), (0,1,"R")]
    x, y = find_blank(state)
    successors = []
    for dx, dy, direction in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            successors.append((new_state, direction))
    return successors

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def a_star_search(start_state, goal_state):
    open_list = []
    start_h = manhattan_distance(start_state, goal_state)
    heapq.heappush(open_list, (start_h, 0, start_state, []))
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        state_tuple = state_to_tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if state == goal_state:
            return path

        for succ, direction in get_successors(state):
            succ_tuple = state_to_tuple(succ)
            if succ_tuple not in visited:
                h = manhattan_distance(succ, goal_state)
                heapq.heappush(open_list, (g+1+h, g+1, succ, path + [direction]))
                # Printing the move and heuristic at each level
                # print(f"Considering move: {direction}, h(n)={h}, g(n)={g+1}, f(n)={g+1+h}")

    return None

def read_input(filename): 
    with open(filename, "r") as f: 
        lines = [line.strip() for line in f if line.strip()] 
        start_state = [list(map(int, lines[i].split())) for i in range(3)] 
        goal_state = [list(map(int, lines[i+3].split())) for i in range(3)] 
    
    return start_state, goal_state

# -------------------- RUN EXAMPLE --------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Format: python3 main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    start_state, goal_state = read_input(input_file)
    solution = a_star_search(start_state, goal_state)

    if solution:
        moves_str = "".join(solution)
        print(f"Solution found in {len(solution)} moves: {moves_str}")
    else:
        print("No solution found.")
