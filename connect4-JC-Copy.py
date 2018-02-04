# game is created with:
# board, player
# board is 2d list
# player is 0 or 1
# player is whose move it currently is
# either 'x' or 'o'

import copy

# game implementation
rows = 6
cols = 7

# prints the current board state
def print_board(board):
    col_labels = [str(i) for i in range(cols)]
    col_labels.insert(0, ' ')
    col_labels.insert(cols + 1, ' ')
    print(col_labels)
    for i in range(rows):
        row_new = copy.copy(board[i])
        row_new.insert(0, str(i))
        row_new.insert(cols + 1, str(i))
        print(row_new)
    print(col_labels)

# counts the number of occurences of x on the board
def board_count(board, x):
    count = 0
    for row in board:
        for square in row:
            if square == x: count += 1
    return count

# used for checking to see if any player has four in a row
def word_search(board, word):
    for i in range(rows):
        for j in range(cols):
            if(word_search_from_square(board, word, i, j)):
                return True
    return False

def word_search_from_square(board, word, i, j):
    directions = [(-1, 1), (-1, 0), (-1, 1),
                  (0, -1),          ( 0, 1),
                  (1, -1), ( 1, 0), ( 1, 1)]
    for direction in directions:
        if word_search_in_direction(board, word, i, j, direction):
            return True
    return False

def word_search_in_direction(board, word, i, j, direction):
    (x_dir, y_dir) = direction
    for idx in range(len(word)):
        if(i < 0 or i >= rows or j < 0 or
           j >= cols or board[i][j] != word[idx]):
            return False
        i += x_dir
        j += y_dir
    return True

def status(game):
    (board, player) = game
    if(board_count(board, "-") == 0):
        if(word_search(board, 'o' * 4)):
            return "Winner: o"
        elif(word_search(board, 'x' * 4)):
            return "Winner: x"
        else:
            return "Draw"
    elif word_search(board, 'o' * 4):
        return "Winner: o"
    elif word_search(board, 'x' * 4):
        return "Winner: x"
    else:
        return "Playing"

# if a suggested column is a legal column to drop a piece,
# this function returns (x, y), where x and y are the row
# and column, respectively, where the piece is actually dropped
def is_legal_move(game, col):
    (board, player) = game
    if col < 0 or col >= cols:
        return None
    for i in range(rows)[::-1]:
        if board[i][col] == "-":
            return (i, col)
    return None

# determines what character to place on square, based on current player
def move(player):
    return 'o' if player == 0 else 'x'

# returns (board, player) as a new state
# after prompting the user for a valid column
# or instructions to quit the game
def make_move(game):
    (board, player) = game
    while True:
        ipt = input("Input a move: ")
        try:
            ipt = int(ipt)
            square = is_legal_move(game, ipt)
            (i, j) = square
            if square is not None:
                board[i][j] = move(player)
                player = (player + 1) % 2
                return (board, player)
            else:
                print("Not a valid move. Try again!")
        except:
            if(ipt == "quit"):
                return (ipt, player)
            print("Not a valid move. Try again!")

# creates starting board
def make_board():
    board = []
    for i in range(rows):
        board.append(["-" for i in range(cols)])
    return board

#####################

# run this function to player two player, human vs human
def play_game():
    board = make_board()
    player = 0
    print("Here is the starting board:")
    print_board(board)
    while(status((board, player)) == "Playing"):
        print("It's Player %i's move!" % player)
        (board, player) = make_move((board, player))
        if board == "quit":
            print("Game exited")
            return
        print("Here is the board now:")
        print_board(board)
    print(status((board, player)))
    print("Thanks for playing!!")
    return None


#####################
# put AI work here!
#####################

# delete the function body / add helper functions
# this currently just drops a piece into the first open column
# (returns the new board and player after doing this)
def AI_move(game):
    (board, player) = game
    for i in range(cols):
        new = is_legal_move(game, i)
        if new is not None:
            (x, y) = new
            board[x][y] = 'x'
            return (board, (player + 1) % 2)

#####################

# run this function if you want to play against your AI
def against_AI():
    player_list = ['o','x']
    board = make_board()
    player = 0
    print("Here is the starting board:")
    print_board(board)
    while(status((board, player)) == "Playing"):
        if player == 0:
            (board, player) = make_move((board, player))
            if board == "quit":
                print("Game exited")
                return
        else:
            (board, player) = AI_move((board, player))
            print("Here is the board now:")
            print_board(board)
            
        print(estimator([board,0]), 'o')
        print(estimator([board,1]), 'x')

    print(status((board, player)))
    print("Thanks for playing!!")
    return None

def est_check(board, ps, player):
    if (board[ps[0]][ps[1]] == player and 
        board[ps[0]][ps[1]+1] == player):
        return 1
    else: return 0


def estimator(game):
    player_list = ['o','x']
    player = player_list[game[1]]
    total = 0
    for x in range(rows):
        for y in range(cols-1):
            total += est_check(game[0], [x,y], player)
    return total
   


against_AI()