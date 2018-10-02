def search(depth, game_state, interval):
    allmoves = moves(game_state)
    (board, player) = game_state
    if player == "maxie":
        return maxie_search(depth, game, interval, allmoves, None)
    else:
        return minie_search(depth, game, interval, allmoves, None)

def maxie(depth, game_state, interval, allmoves, best):
    #best is a tuple
    (alpha, beta) = interval
    if allmoves == []:
        return best
    else:
        first = allmoves(0)
        temp = evaluate(first, game_state, depth)
        pos = compare_alpha_beta(interval, temp)
        if pos == "ABOVE":
            return best
        if pos == "IN":
            new_interval = (temp, beta)
            return maxie(depth, game_state, new_interval, allmoves[1:], best)
        if pos == "BELOW":
            return maxie(depth, game_state, interval, allmoves[1:], best)

def minie(depth, game_state, interval, allmoves, best):
    #best is a tuple
    (alpha, beta) = interval
    if allmoves == []:
        return best
    else:
        first = allmoves(0)
        temp = evaluate(first, game_state, depth)
        pos = compare_alpha_beta(interval, temp)
        if pos == "ABOVE":
            return minie(depth, game_state, interval, allmoves[1:], best)
        if pos == "IN":
            new_interval = (alpha, temp)
            return maxie(depth, game_state, new_interval, allmoves[1:], best)
        if pos == "BELOW":
            return best

def evaluate(move, game_state, depth):
    pass

def compare_alpha_beta(interval, temp):
    (alpha, beta) = interval
    if alpha == "-inf" and beta == "inf":
        return "IN"
    elif temp > alpha and temp < beta:
        return "IN"
    elif beta == "-inf":
        return "ABOVE"
    elif alpha == "inf":
        return "BELOW"
    elif temp < alpha:
        return "BELOW"
    elif temp > beta:
        return "ABOVE"

def next_move(game_state):
    pass

def win_states_estimator(game_state):
    winner = status(game_state)
    if winner == "Winner o":
        return "inf"
    if winner == "Winner x":
        return "-inf"
    return 0
