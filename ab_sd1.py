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
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
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

def moves(game_state):
    (board, player) = game_state
    allmoves = []
    print(game_state)
    for i in range(7):
        a =  is_legal_move(game_state,i)
        if a is not None:
            allmoves.append(a)
    return allmoves

def search(depth, game_state, interval):
    allmoves = moves(game_state)
    (board, player) = game_state
    if player == 1:
	# typo, you called maxie_search
	# i think the fn names got written in multiple ways somewhere
    # i think by game you meant game_state
        return maxie(depth, game_state, interval, allmoves, None)
    else:
        return minie(depth, game_state, interval, allmoves, None)

def FIXED_move(game_state, cord):
    (i, j) = cord
    (board, player) = game_state
    board = copy.deepcopy(board)
    board[i][j] = move(player)
    return (board, (player + 1) % 2)

def maxie(depth, game_state, interval, allmoves, best):
    #best is a tuple
    (alpha, beta) = interval
    if allmoves == []:
        print("best", best)
        assert(best is not None)
        return best
    else:
	# you had [] as () originally, we want the first thing in the moves list
        first = allmoves[0]
        print(first)
        # should evaluate made move (originally just kept current game state)
        temp = evaluate(depth - 1, FIXED_move(game_state, first), interval)
        # print(temp)
        pos = compare_alpha_beta(interval, temp)
        # making sure that we don't pass down None as our best
        some_best = best if best is not None else (temp, first)
        if pos == "ABOVE":
            return (temp, first)
        if pos == "IN":
            # i don't think best was originally updated in the code
            new_interval = (temp, beta)
            new_best = (temp, first)
            return maxie(depth, game_state, new_interval, allmoves[1:], new_best)
        if pos == "BELOW":
            return maxie(depth, game_state, interval, allmoves[1:], some_best)

def minie(depth, game_state, interval, allmoves, best):
    #best is a tuple
    (alpha, beta) = interval
    if allmoves == []:
        print("best", best)
        assert(best is not None)
        return best
    else:
        first = allmoves[0]
        # should evaluate made move
        temp = evaluate(depth - 1, FIXED_move(game_state, first), interval)
        # print(temp)
        pos = compare_alpha_beta(interval, temp)
        some_best = best if best is not None else (temp, first)
        if pos == "ABOVE":
            return minie(depth, game_state, interval, allmoves[1:], some_best)
        if pos == "IN":
            new_best = (temp, first)
            new_interval = (alpha, temp)
            return maxie(depth, game_state, new_interval, allmoves[1:], new_best)
        if pos == "BELOW":
            return (temp, first)

# changed arguments - could have more arguments and directly call
# minie or maxie but just calling search should work fine
def evaluate(depth, game_state, interval):
    print("here")
    (board, player) = game_state
    # changing this a bit to add print statements for debugging
    if depth == 0:
        cur_status = status(game_state)
        if cur_status == "Winner x" or cur_status == "Winner o":
            return win_states_estimator(game_state)
        est = estimator(board)
        return est
    a = search(depth, game_state, interval)
    print(a, depth, game_state,interval)
    (estimate, move) = a
    return estimate

# yeahh this function is terrible - i added some cases
# still need to double check that this is all sensible
def compare_alpha_beta(interval, temp):
    (alpha, beta) = interval
    # the order that you check in here is important for typechecking
    # :(
    # print(alpha, beta, temp)
    if(alpha == "-inf" and beta == "-inf"):
        return 1/0
    if (alpha == "-inf" and beta == "inf"):
        return "IN"
    elif (alpha == "inf" and beta == "inf"):
        return "BELOW"
    elif (alpha == "-inf" and beta == "-inf"):
        return "ABOVE"
    elif (beta == "inf" and temp <= alpha):
        return "BELOW"
    elif (temp == "inf"):
        return "ABOVE"
    elif (temp == "-inf"):
        return "BELOW"
    elif (beta == "inf" and temp > alpha):
        return "IN"
    elif (alpha == "-inf" and temp >= beta):
        return "ABOVE"
    elif (alpha == "-inf" and temp < beta):
        return "IN"
    elif (temp > alpha and temp < beta):
        return "IN"
    elif (temp < alpha):
        return "BELOW"
    elif (temp > beta):
        return "ABOVE"

def next_move(game_state):
    interval = ("-inf", "inf")
    depth = 1 # for now
    (estimate, move) = search(depth, game_state, interval)
    return move

def win_states_estimator(game_state):
    winner = status(game_state)
    if winner == "Winner o":
        return "inf"
    if winner == "Winner x":
        return "-inf"
    return 0

def est_check(board, player):
    for i in range(2, 5):
        return word_search_score(board, player, i)


def word_search_score(board, word, num):
    score = 0
    for i in range(rows):
        for j in range(cols):
            if(word_search_from_square(board, 'x' * num, i, j)):
                if num == 4:
                    return score + 1000000
                score = score + num


    for i in range(rows):
        for j in range(cols):
            if (word_search_from_square(board, 'o' * num, i, j)):
                if num == 4:
                    return score - 10000000000
                score = score - num

    return score
def chainChecker(board):
        total1 = word_search_Count(board, 'xxx-')
        total2 = word_search_Count(board, 'x-xx')
        total3 = - word_search_Count(board, 'ooo-')
        total4 = - word_search_Count(board, 'o-oo')
        return total1+total2+total3+total4

def centerChecker(board):
    centered = 0
    for i in range(6):
        for j in range(7):
            if board[i][j] == 'x':
                centered += abs(3-j)
            if board[i][j]=='o':
                centered -= abs(3-j)
            if board[i][j]== '-':
                centered += 0
    return centered

def word_search_Count(board, word):
    numberOfChains = 0
    for i in range(rows):
        for j in range(cols):
            if(word_search_from_square(board, word, i, j)):
                numberOfChains+= 1
    return numberOfChains
#board1 = [['-','-','-','-','-','-','-'],
          #['-','-','-','-','-','-','-'],
          #['-','-','-','-','-','-','-'],
          #['-','-','-','-','-','-','-'],
          #['-','-','-','o','-','-','-'],
          #['-','-','o','x','x','x','-']]
#print(centerChecker(board1), chainChecker(board1))
def estimator(board):
    #checking game status
    total = 0
    total = chainChecker(board)-centerChecker(board)
    print(total)
    return total


def mostNumberInRow(game, new):
    (board, player) = game
    (x,y)=new


    directions = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
    vals = [0 for i in range(8)]

    for i in range(8):
        startX, startY = x+directions[i][0],y+directions[i][1]
        while startX!=-1 and startY !=cols and startY!=-1 and startX!=rows:

            if board[startX][startY]=='x':
                vals[i]+=1
            else:
                break
            startX += directions[i][0]
            startY += directions[i][1]
    return max(vals)

def AI_move(game):
    print("Alice")
    # game_state = (game, "maxie")
    game_state = game
    best = next_move(game_state)
    (i,j) = best
    (board, player) = game
    board[i][j] = 'x'

    print("TTTTTTTTTTTTTTTTTTTT----BEST", best)
    # print(1/0)
    # possibleMoves = []
    # # for i in range(cols):
    # #     new = is_legal_move(game, i)
    # #     if new is not None:
    # # possibleMoves.append(new)
    # minMax = [mostNumberInRow(game,n) for n in possibleMoves]
    # best = possibleMoves[minMax.index(max(minMax))]
    # (x, y) = best
    # board[x][y] = 'x'
    return (board, (player + 1) % 2)

#####################

# run this function if you want to play against your AI
def against_AI():
    board = make_board()
    player = 0
    print("Here is the starting board:")
    print_board(board)
    while(status((board, player)) == "Playing"):
        if player == 0:
            print(len(board), len(board[0]))
            (board, player) = make_move((board, player))
            if board == "quit":
                print("Game exited")
                return
        else:
            print("---------------------")
            print(player)
            (board, player) = AI_move((board, player))
            print("Here is the board now:")
            print_board(board)
            print(player)
            # assert (1==0)
    print(status((board, player)))
    print("Thanks for playing!!")
    return None

against_AI()