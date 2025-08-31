from typing import Tuple

moves = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}

def is_valid_move(index:int, move:str):
    if move == 'L' and index % 3 == 0:
        return False
    if move == 'R' and index % 3 == 2:
        return False
    if move == 'U' and index < 3:
        return False
    if move == 'D' and index > 5:
        return False
    return True

def inversion_count(state: Tuple[int, ...]) -> int:
    arr = [x for x in state if x != 0]
    inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2

def is_solvable(start_state: Tuple[int, ...], goal_state: Tuple[int, ...]) -> bool:
    """8-puzzle on 3x3 is solvable iff inversion count is even (ignoring 0) according to the goal state"""
    s = inversion_count(start_state)
    g = inversion_count(goal_state)
    return s == g
