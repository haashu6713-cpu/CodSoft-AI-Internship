import random

board = [" "] * 9

def show_board():

 print("\n")
print("     |     |     ")
print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
print("_____|_____|_____")

print("     |     |     ")
print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
print("_____|_____|_____")

print("     |     |     ")
print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
print("     |     |     ")

print()

def check_winner(player):


    winning_places = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

    for place in winning_places:

     if (
        board[place[0]] == player and
        board[place[1]] == player and
        board[place[2]] == player
    ):
        return True

    return False


def check_draw():
 return " " not in board

def minimax(is_maximizing):

 if check_winner(computer_symbol):
    return 1

if check_winner(user_symbol):
    return -1

if check_draw():
    return 0

if is_maximizing:

    best_score = -100

    for i in range(9):

        if board[i] == " ":

            board[i] = computer_symbol

            score = minimax(False)

            board[i] = " "

            best_score = max(score, best_score)

    return best_score

else:

    best_score = 100

    for i in range(9):

        if board[i] == " ":

            board[i] = user_symbol

            score = minimax(True)

            board[i] = " "

            best_score = min(score, best_score)

    return best_score


def computer_move():


best_score = -100
move = -1

for i in range(9):

    if board[i] == " ":

        board[i] = computer_symbol

        score = minimax(False)

        board[i] = " "

        if score > best_score:

            best_score = score
            move = i

board[move] = computer_symbol


print("=" * 45)
print("         TIC TAC TOE GAME")
print("=" * 45)

print("""
Board positions:

1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
""")

while True:


user_symbol = input("Choose X or O: ").upper()

if user_symbol == "X":
    computer_symbol = "O"
    break

elif user_symbol == "O":
    computer_symbol = "X"
    break

else:
    print("Please choose only X or O")


print(f"\nYou are {user_symbol}")
print(f"Computer is {computer_symbol}")

turn = "X"

while True:

show_board()

if turn == user_symbol:

    try:
        move = int(input("Choose position (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Choose between 1 and 9.")
            continue

    except ValueError:
        print("Enter numbers only.")
        continue

    if board[move] != " ":
        print("Already filled! Try again.")
        continue

    board[move] = user_symbol

    if check_winner(user_symbol):
        show_board()
        print("You won!")
        break

    turn = computer_symbol

else:

    print("\nComputer is thinking...\n")

    computer_move()

    if check_winner(computer_symbol):
        show_board()
        print("Computer won!")
        break

    turn = user_symbol

if check_draw():
    show_board()
    print("It's a draw!")
    break

