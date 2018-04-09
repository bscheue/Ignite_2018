import copy
import ab_integrated

# prints the current board state
def print_board(board):
    col_labels = [str(i) for i in range(cols)]
    col_labels.insert(0, ' ')
    col_labels.insert(cols + 1, ' ')
    print(col_labels)
    for i in range(data.rows):
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

# used for checking to see if any _)er has four in a row
def word_search(board, word, data):
    for i in range(data.rows):
        for j in range(data.cols):
            if(word_search_from_square(board, word, i, j, data)):
                return True
    return False

def word_search_from_square(board, word, i, j, data):
    directions = [(-1, 1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for direction in directions:
        if word_search_in_direction(board, word, i, j, direction, data):
            return True
    return False

def word_search_in_direction(board, word, i, j, direction, data):
    (x_dir, y_dir) = direction
    for idx in range(len(word)):
        if(i < 0 or i >= data.rows or j < 0 or
           j >= data.cols or board[i][j] != word[idx]):
            return False
        i += x_dir
        j += y_dir
    return True

def status(game, data):
    (board, player) = game
    if(board_count(board, "-") == 0):
        if(word_search(board, 'o' * 4, data)):
            data.winner = ("Red")
            return "Winner: o"
        elif(word_search(board, 'x' * 4, data)):
            data.winner = ("Blue")
            return "Winner: x"
        else:
            return "Draw"
    elif word_search(board, 'o' * 4, data):
        data.winner = ("Red")
        return "Winner: o"
    elif word_search(board, 'x' * 4, data):
        data.winner = ("Blue")
        return "Winner: x"
    else:
        return "Playing"

# if a suggested column is a legal column to drop a piece,
# this function returns (x, y), where x and y are the row
# and column, respectively, where the piece is actually dropped
def is_legal_move(game, col, data):
    (board, player) = game
    if col < 0 or col >= data.cols:
        return None
    for i in range(data.rows)[::-1]:
        if board[i][col] == "-":
            return (i, col)
    return None

# determines what character to place on square, based on current player
def move(player):
    return 'o' if player == 0 else 'x'

def make_move(data, game, ipt):
    (board, player) = game
    square = is_legal_move(game, ipt, data)
    if square != None:
        (i, j) = square
        board[i][j] = move(player)
        data.current_player = (player + 1) % 2
    return (board, player)

#####################
def play_game(data):
    if(status((data.game_board, data.current_player), data) == "Playing"):
        if (data.made_move == True):
            col = data.placed_col
            game = (data.game_board, data.current_player)
            (board,player) = make_move(data, game, col)
            data.game_board = board
            data.made_move = False
    elif(status((data.game_board, data.current_player), data) != "Playing"):
        data.current_screen = "end"

def play_AI_game(data):
    if(status((data.game_board, data.current_player), data) == "Playing"):
        if(data.current_player == 0):
            if (data.made_move == True):
                col = data.placed_col
                game = (data.game_board, data.current_player)
                (board,player) = make_move(data, game, col)
                data.game_board = board
                data.made_move = False
        else:
            game = (data.game_board, data.current_player)
            (data.game_board, data.current_player) = ab_integrated.AI_move(game)

    elif(status((data.game_board, data.current_player), data) != "Playing"):
        data.current_screen = "end"
