import math
# Create board
board = [" " for _ in range(9)]
def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def board_full():
    return " " not in board


# Minimax Algorithm
def minimax(is_max):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(score, best)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(score, best)

        return best


# AI Move
def ai_move():

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


# Human Move
def human_move():

    while True:

        try:
            move = int(input("Choose position (1-9): ")) - 1

            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break

            else:
                print("Invalid move")

        except:
            print("Enter a number")


# Game Loop
print("You = X")
print("AI = O")

while True:

    print_board()

    human_move()

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if board_full():
        print_board()
        print("Draw")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if board_full():
        print_board()
        print("Draw")
        break