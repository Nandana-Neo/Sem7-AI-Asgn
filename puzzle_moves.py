goal_state = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0)  # 0 = blank

moves = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}

def is_valid_move(index, move):
    if move == 'L' and index % 3 == 0:
        return False
    if move == 'R' and index % 3 == 2:
        return False
    if move == 'U' and index < 3:
        return False
    if move == 'D' and index > 5:
        return False
    return True

