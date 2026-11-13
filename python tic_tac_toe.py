                             #Python Project
WRITING_LINES = [
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6),
]

def display_board(board):
    "Display the current 3x3 board."
print()
for row in range(3):
    cells =[]
    for col in range(3):
        value = board[row * 3 + col]
        cells.append(value if value != "" else str(row * 3 + col +1))
        print(" "+"/".join(cells))
        if row < 2:
            print("---+----+---")
    print()

def check_winner(board):
    "check if a player has won the game."

    for line in WRITING_LINES:
        a, b, c = line
        if board[a] != "" and board[a] == board[b] == board[c]:
            winning_line = "-". join(str(index + 1) for index in line)
            return board[a], winning_line
        
    return None, None

def get_move(board,player):
    "get a valid move from the player."
    while True:
        raw_position = input(
            f"Player {player}, enter a position(1-9): "
        ).strip()

        try:
            position = int(raw_position)
        except ValueError :
            print("Invalid position. Enter a number between 1 and 9.")
            continue

        if position <1 or position > 9:
            print("Invalid position.Enter a number between 1 and 9.")
            continue
        if board[position - 1] != "":
            print("Position already taken.")
            continue
        return position - 1

def play_game():
    """Run one complete game of tic-tac-toe."""
board = [""] * 9
current_player = "X"
move_count = 0
display_board(board)

while move_count < 9:
    position = get_move(board, current_player)
    board[position] = current_player
    move_count +=1

    display_board(board)
    winner, winning_line = check_winner(board)

    if winner:
        print(f"Player {winner} wins!")
        print(f"Winning line: {winning_line}")
    break

    if move_count == 9:
        print("Board is full after 9 moves.")
        print("it's a draw! No moves left.")
    break

player = "0" if current_player == "X" else "X"


def main():
    """Allow the players to play multiple games."""
    while true:
        play_game()

        play_again = input("play gain? (y/n): ").strip().lower()

        while play_again not in ("y", "n"):
            print("please enter 'y' or 'n'.")
            play_again = input("play again? (y/n)").strip().lower()

        if play_again == "n":
            print("thanks for playing!")
            break

if __name__ == "__main__":
    main()


        
    


