
def search(depth, game_state, interval):
    allmoves = moves(game_state)
    (board, player) = game_state
    if player == "maxie":
	# typo, you called maxie_search
	# i think the fn names got written in multiple ways somewhere
    # i think by game you meant game_state
        return maxie(depth, game_state, interval, allmoves, None)
    else:
        return minie(depth, game_state, interval, allmoves, None)

def maxie(depth, game_state, interval, allmoves, best):
    #best is a tuple
    (alpha, beta) = interval
    if allmoves == []:
        return best
    else:
	# you had [] as () originally, we want the first thing in the moves list
        first = allmoves[0]
        # should evaluate made move (originally just kept current game state)
        temp = evaluate(depth - 1, make_move(game_state, first), interval)
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
        return best
    else:
        first = allmoves[0]
        # should evaluate made move
        temp = evaluate(depth - 1, make_move(game_state, first), interval)
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
    (board, player) = game_state
    # changing this a bit to add print statements for debugging
    if depth == 0:
        cur_status = status(game_state)
        if cur_status == "Winner x" or cur_status == "Winner o":
            return win_states_estimator(game_state)
        est = estimator(board)
        return est
    (estimate, move) = search(depth, game_state, interval)
    return estimate

# yeahh this function is terrible - i added some cases
# still need to double check that this is all sensible
def compare_alpha_beta(interval, temp):
    (alpha, beta) = interval
    # the order that you check in here is important for typechecking
    # :(
    print(alpha, beta, temp)
    #if(alpha == "-inf" and beta == "-inf"):
    #    return 1/0
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

###########
# from other file
###########

# this game is pretty terrible
# it doesn't even make a ton of sense i just used it for debugging purposes
# basically one player wants a 3 bit string of all 1s
# and the other wants a 3 bit string of all 0s
# (yes this estimator function doesn't make sense for the game)
# i just wanted to have more unique scores for debugging purposes
# a more appropriate estimator would just count the number of 0s / 1s in some
# fashion
def estimator(board):
    total = 0
    n = len(board)
    for i in range(n):
        total += 2**i * int(board[n - i - 1])
    # the estimator isn't even centered around zero
    # should use 3.5 but didn't want to use floats
    return total - 4


def status(game_state):
    (board, player) = game_state
    if board == "111":
        return "Winner o"
    elif board == "000":
        return "Winner x"
    return "player"

def moves(game_state):
    return [0, 1, 2]

def make_move(game_state, i):
    (board, player) = game_state
    # strings are immutable so just cast them to lists?
    board = list(board)
    board[i] = flipped(board[i])
    board = "".join(board)
    return (board, (player + 1) % 2)

def flipped(s):
    return "0" if s == "1" else s

def map(f, a):
    return [f(x) for x in a]

def prepend(s, i):
    return i + s

def prep_curry(i):
    return lambda s : prepend(s, i)

def flipper(board):
    if board == "":
        return []
    return [flipped(board[0]) + board[1:]] + map(prep_curry(board[0]), flipper(board[1:]))


# print(next_move(("100", 0)))