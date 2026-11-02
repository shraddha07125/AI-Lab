
# Tic-Tac-Toe using Minimax

board = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")


def winner():
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def minimax(is_max):
    result = winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if " " not in board:
        return 0

    if is_max:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best


def computer_move():
    best = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"


# Main game
while True:
    display()

    if winner():
        print(winner(), "wins!")
        break

    if " " not in board:
        print("Game Draw!")
        break

    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = "X"

    if winner():
        display()
        print("You win!")
        break

    if " " not in board:
        display()
        print("Game Draw!")
        break

    computer_move()

    if winner():
        display()
        print("Computer wins!")
        break

    if " " not in board:
        display()
        print("Game Draw!")
        break
      
