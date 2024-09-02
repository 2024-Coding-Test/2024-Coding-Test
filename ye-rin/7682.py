def check_winner(board, player):
    # 가로, 세로, 대각선으로 연속된 3개의 말이 있는지 확인
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로
        [0, 4, 8], [2, 4, 6]             # 대각선
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_valid_tictactoe(board):
    x_count = board.count('X')
    o_count = board.count('O')
    
    if not (x_count == o_count or x_count == o_count + 1):
        return "invalid"
    
    x_win = check_winner(board, 'X')
    o_win = check_winner(board, 'O')
    
    if x_win and o_win:
        return "invalid"
    if x_win and x_count != o_count + 1:
        return "invalid"
    if o_win and x_count != o_count:
        return "invalid"
    
    if not x_win and not o_win and x_count + o_count < 9:
        return "invalid"
    
    return "valid"

while True:
    board = input().strip()
    if board == "end":
        break
    print(is_valid_tictactoe(board))