# TWO Player Game - Tic-Tac-Toe
# Using Heuristic Function

# Display the board
def display(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Heuristic function: checks who wins
def heuristic(board):
    win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == "X":
            return 10
        elif board[a] == board[b] == board[c] == "O":
            return -10

    return 0


# Create an empty board
board = [" "] * 9
player = "X"

# Play the game
for turn in range(9):
    display(board)
    print("Player", player)

    try:
        position = int(input("Enter position (1-9): ")) - 1
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    # Check whether the position is valid
    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid position! Try again.")
        continue

    # Place X or O on the board
    board[position] = player

    # Check who won
    score = heuristic(board)

    if score == 10:
        display(board)
        print("Player X wins!")
        break

    elif score == -10:
        display(board)
        print("Player O wins!")
        break

    # Switch players
    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    display(board)
    print("Game Draw!")
