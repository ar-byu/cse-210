# Tic Tac Toe by Anna Rector

def print_board(values):
    print()
    print(f"{values[0]} | {values[1]} | {values[2]}")
    print('- + - + -')
    print(f"{values[3]} | {values[4]} | {values[5]}")
    print('- + - + -')
    print(f"{values[6]} | {values[7]} | {values[8]}")
    print()

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def get_board():
    board = []
    for position in range(9):
        board.append(position + 1)
    return board

def make_move(player, board):
    turn = True
    while turn:
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        if board[square - 1] == "x" or board[square - 1] == "o":    
            print("That square is already full. Please pick a different one.")
        else:
            turn = False
            board[square - 1] = player

def win_condition(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def draw_condition(board):
    for square in board:
        if board[square] != "x" and board[square] != "o":
            return False
        else:
            return True

def main():
    player = next_player("")
    board = get_board()
    while not (win_condition(board)) or not (draw_condition(board)):
        print_board(board)
        make_move(player, board)
        player = next_player(player)
    print_board(board)
    print(f"{next_player(player)} wins! Thanks for playing!")
           

main()