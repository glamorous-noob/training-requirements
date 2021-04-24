import random
import time

def quit_game():
    print("It was good while it lasted. Sad. You lose by default though.")
    exit()

def get_user_input(s=""):
    print(s, end="")
    return input("> ")


def create_board():
    return [[" " for i in range(3)] for j in range(3)]

def print_board(board):
    print("    "+"   ".join([str(i+1) for i in range(len(board))]))
    for i in range(len(board)):
        row = board[i]
        print(str(i+1)+" |", end="")
        for cell in row:
            print(" "+cell+" |", end="")
        print("\n  -"+"-"*4*len(row))

def return_true():
    return True

def get_token_choice():
    valid = False
    user_input =""
    remark =""
    while not valid:
        user_input = get_user_input(remark + "Please choose X or O (or Q to quit).").strip().upper()
        valid = len(user_input)==1 and user_input in "XOQ"
        remark = "I hear typos are all the rage these days.\n"
    if user_input == "Q":
        quit_game()
    return user_input

def get_human_int(prompt, min_int, max_int):
    valid = False
    number = None
    while not valid:
        try:
            user_in = input(prompt).strip().upper()
            if user_in == "Q":
                quit_game()
            number = int(user_in)-1
            valid = min_int<=number<=max_int
            if not valid:
                raise ValueError()
        except ValueError:
            print("That was definitely neither Q nor a number between", min_int,"and", max_int,"included...\nTry again.")
    return number

def is_empty_cell(board, row, column):
    return board[row][column]==" "

def get_cell(board, row, column):
    return board[row][column]


def set_cell(board, row, column, token):
    board[row][column] = token

def human_turn(board, human_token, pc_token):
    print_board(board)
    print("Your turn, player", human_token)
    valid = False
    while not valid:
        row = get_human_int("Which row ? (Q to quit) : ", 0, len(board)-1)
        column = get_human_int("Which column ? (Q to quit) : ", 0, len(board)-1)
        if is_empty_cell(board, row, column):
            valid = True
        else:
            print("The cell at row", row+1, "and colmun", column+1,"already contains", get_cell(board, row, column))
            print("Try again.")
    set_cell(board, row, column, human_token)
    print_board(board)


def get_all_empty_cells_indexes(board):
    n = len(board)
    return [(row, column) for row in range(n) for column in range(n) if is_empty_cell(board, row, column)]


def pc_turn(board, human_token, pc_token):
    # stupid version where the pc makes random moves
    print("Now it's my turn. Let me think.")
    time.sleep(1)
    row, column = random.choice(get_all_empty_cells_indexes(board))
    set_cell(board, row, column, pc_token)
    print("Made my choice. Voilaa")
    print_board(board)


def check_diagonal_win(board, token):
    n = len(board)
    return all(board[i][i]==token for i in range(n)) or all(board[i][n-i-1] == token for i in range(n))


def check_horizontal_win(board, token):
    for row in board:
        if row.count(token)==len(row):
            return True
    return False

def check_vertical_win(board, token):
    n = len(board)
    for column in range(n):
        if all(board[i][column]==token for i in range(n)):
            return True
    return False

def has_game_ended(board, tokens):
    for t in tokens:
        if check_diagonal_win(board, t) or check_horizontal_win(board, t) or check_vertical_win(board, t):
            return True, t
    return False, None

def run_game():
    tokens = "XO"
    token_to_player = dict()
    human_token = get_token_choice()
    pc_token = tokens.replace(human_token, "")
    board = create_board()
    token_to_player[human_token] = human_turn
    token_to_player[pc_token] = pc_turn

    game_ended = False
    winner = None
    i=0
    while not game_ended:
        print("Round", i)
        print("=======")
        token_to_player[tokens[i%len(tokens)]](board, human_token, pc_token)
        game_ended, winner = has_game_ended(board, tokens)
        i+=1
    print("We have a winner! Player", winner)

if __name__ == "__main__":
    run_game()