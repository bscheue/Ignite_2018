import copy

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
# put AI work here!
#####################

# also switches whose turn it is
def place_piece(game, move):
    (x, y) = move
    (board, player) = game
    # board[x][y] = "hello"# move(player)
    return (board, (player + 1) % 2)

# delete the function body / add helper functions
# this currently just drops a piece into the first open column
# (returns the new board and player after doing this)
def minimax(game,depthRemaining):
    (board,player)=game
    state = status(game)
    if state !="Playing":
        return state
    if depthRemaining == 0:
        return estimator(game)
    possibleMoves = []
    for i in range(cols):
        new = is_legal_move(game, i)
        if new is not None:
            possibleMoves.append(new)
    if player%2==0:
        return min([minimax(place_piece(game,move),depthRemaining-1) \
            for move in possibleMoves])
    else:
        return max([minimax(place_piece(game,move),depthRemaining-1) \
            for move in possibleMoves])

    best = possibleMoves[estimations.indexOf(max(estimations))]
    minimax(game,depthRemaining-1)
    #if depth is odd, then the move made will be the max
    #if depth is even, then the move made will (theoretically) be the min

def est_check(board, player):
    for i in range(2, 5):
        return word_search_score(board, player, i)

def word_search_score(board, word, num):
    score = 0
    for i in range(data.rows):
        for j in range(cols):
            if(word_search_from_square(board, 'x' * num, i, j)):
                if num == 4:
                    return score + 1000000
                score = score + num

    for i in range(data.rows):
        for j in range(cols):
            if (word_search_from_square(board, 'o' * num, i, j)):
                if num == 4:
                    return score - 10000000000
                score = score - num
    return score

def estimator(game):
    player_list = ['o','x']
    player = player_list[game[1]]
    total = 0
    for x in range(data.rows):
        for y in range(cols-1):
            total += est_check(game[0], player)
    return  total

def mostNumberInRow(game, new):
    (board, player) = game
    (x,y)=new

    directions = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
    vals = [0 for i in range(8)]

    for i in range(8):
        startX, startY = x+directions[i][0],y+directions[i][1]
        while startX!=-1 and startY !=cols and startY!=-1 and startX!=data.rows:

            if board[startX][startY]=='x':
                vals[i]+=1
            else:
                break
            startX += directions[i][0]
            startY += directions[i][1]
    return max(vals)

def AI_move(game):
    best = minimax(game,2)
    (board, player) = game

    possibleMoves = []
    for i in range(cols):
        new = is_legal_move(game, i)
        if new is not None:
            possibleMoves.append(new)
            minMax = [mostNumberInRow(game,n) for n in possibleMoves]

    best = possibleMoves[minMax.index(max(minMax))]
    (x, y) = best
    board[x][y] = 'x'
    return (board, (player + 1) % 2)

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

# run this function if you want to play against your AI
def against_AI():
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
    print(status((board, player)))
    print("Thanks for playing!!")
    return None