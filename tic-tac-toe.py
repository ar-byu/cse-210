# Tic Tac Toe, by Anna Rector

def print_board(values):
    print(f"{values[0]} | {values[1]} | {values[2]}")
    print('- + - + -')
    print(f"{values[3]} | {values[4]} | {values[5]}")
    print('- + - + -')
    print(f"{values[6]} | {values[7]} | {values[8]}")

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

def main():
    player = next_player("")
    board = get_board()
    while not (win(board)) or (draw(board)):
        print_board(board)
        make_move(player, board)
        player = next_player(player)
    print_board(board)
    print("Thanks for playing!")
        

        
        

main()