
# copy and pasted backend file!


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

# used for checking to see if any _)er has four in a row
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


# creates starting board
def make_board():
    board = []
    for i in range(rows):
        board.append(["-" for i in range(cols)])
    return board


# returns (board, player) as a new state
# after prompting the user for a valid column
# or instructions to quit the game
def make_move(game, ipt):
    (board, player) = game
    while True:
            square = is_legal_move(game, ipt)
            (i, j) = square
            if square is not None:
                board[i][j] = move(player)
                player = (player + 1) % 2
                return (board, player)
            else:
                print("Not a valid move. Try again!")
            print("Not a valid move. Try again!")


#####################

# run this function to player two player, human vs human
def play_game(data):
    data.game_board = make_board()
    data.current_player = 0
    while(status((data.game_board, data.current_player)) == "Playing"):
        if data.made_move:
            col = data.col
            (board,player) = make_move(game, col)
    #board = make_board()
    #player = 0
    #print("Here is the starting board:")
    #print_board(board)
    #while(status((board, player)) == "Playing"):
    #    print("It's Player %i's move!" % player)
    #    (board, player) = make_move((board, player))
    #    if board == "quit":
    #        print("Game exited")
    #        return
    #    print("Here is the board now:")
    #    print_board(board)
    #print(status((board, player)))
    #print("Thanks for playing!!")
    #return None


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
        return min([minimax(place_piece(game,move),depthRemaining-1) for move in possibleMoves])
    else:
        return max([minimax(place_piece(game,move),depthRemaining-1) for move in possibleMoves])

    best = possibleMoves[estimations.indexOf(max(estimations))]
    minimax(game,depthRemaining-1)
    #if depth is odd, then the move made will be the max
    #if depth is even, then the move made will (theoretically) be the min

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

def estimator(game):
    player_list = ['o','x']
    player = player_list[game[1]]
    total = 0
    for x in range(rows):
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
        while startX!=-1 and startY !=cols and startY!=-1 and startX!=rows:

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

# against_AI()






# this is the front end!!!!
# above was copy and pasted in


# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

def draw_grid(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill = "#7f81a8" )
    canvas.create_rectangle(data.margin, data.margin, data.width-data.margin, data.height-data.margin,fill = "#dda02c")
    for i in range (data.rows):
        for j in range (data.cols):
            x = data.margin + j*data.square_width
            y = data.margin + i*data.square_height
            a = x + data.square_width
            b = y + data.square_height
            canvas.create_rectangle(x, y, a,b)

def intScrn (canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "#0ba23a")
    canvas.create_text(data.width/2, data.margin*2, fill = "#bd0093", font="Times 80 italic bold", text = "Select Players")
    canvas.create_text(236, data.height/2 - 100, fill = "#bd0093", font="Times 60 italic bold", text = "Player 1")
    canvas.create_text(236, data.height/2 + 100, fill = "#bd0093", font="Times 60 italic bold", text = "Player 2")
    data.rectcolorah = "#0b485a"
    data.rectcolorbh = "#0b485a"
    data.rectcoloraa = "#0b485a"
    data.rectcolorba = "#0b485a"
    
    if data.playera == "H":
        data.rectcolorah = "#0b4877"
    if data.playerb == "H":
        data.rectcolorbh = "#0b4877"
    if data.playera == "A":
        data.rectcoloraa = "#0b4877"
    if data.playerb == "A":
        data.rectcolorba = "#0b4877"
    
    canvas.create_rectangle(data.width/2 - 100,data.height/2-150, data.width/2 + 100,data.height/2 - 50, fill = data.rectcolorah)
    canvas.create_rectangle(data.width/2 - 100,data.height/2 +50, data.width/2 + 100,data.height/2 + 150, fill = data.rectcolorbh)
    canvas.create_rectangle((data.width/4)*3 - 100,data.height/2-150, (data.width/4)*3 + 100,data.height/2 - 50, fill = data.rectcoloraa)
    canvas.create_rectangle((data.width/4)*3 - 100,data.height/2 +50, (data.width/4)*3 + 100,data.height/2 + 150, fill = data.rectcolorba)
    canvas.create_text(data.width/2, data.height/2 - 100, fill = "#bd0093", font="Times 30 italic bold", text = "Human")
    canvas.create_text(data.width/2, data.height/2 + 100, fill = "#bd0093", font="Times 30 italic bold", text = "Human")
    canvas.create_text((data.width/4)*3, data.height/2 - 100, fill = "#bd0093", font="Times 40 italic bold", text = "AI")
    canvas.create_text((data.width/4)*3, data.height/2 + 100, fill = "#bd0093", font="Times 40 italic bold", text = "AI")
    
    
def rulesScrn (canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "#27b6a3")
    canvas.create_text(640, data.margin, fill = "#141519",font="Times 68 italic bold", text = "Rules")
    
            
def startScreen (canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "#702121")
    title(canvas, data)
    playBtn(canvas, data)
    info1(canvas, data)
    info2 (canvas, data)
    settingBtn (canvas, data)

    
def playBtn (canvas, data):
    canvas.create_rectangle(data.margin, data.margin+50, data.width - data.margin,
            data.margin +250, fill = "#294168")
    canvas.create_text(640,195,fill="#e2c24f",font="Times 80 italic bold",text="Start")
    canvas.update
    
    
def info1 (canvas, data):
    canvas.create_rectangle(data.margin,data.height*0.5, data.width*0.5 - data.margin, data.height*0.75, fill = "#294168")
    canvas.create_text(data.width*0.25, data.height*0.625,fill="#e2c24f",font="Times 40 italic bold",text="Rules And Controls")
    canvas.update
    
def info2 (canvas, data):
    canvas.create_rectangle(data.width - data.margin,data.height*0.5, data.width*0.5 + data.margin, data.height*0.75, fill = "#294168")
    canvas.create_text(data.width*0.75, data.height*0.625,fill="#e2c24f",font="Times 40 italic bold",text="Project Info")
    canvas.update
    
def settingBtn (canvas, data):
    canvas.create_oval(data.width - data.margin * 2.75, data.height - data.margin*2.75,data.width - data.margin, data.height-data.margin, fill = "#122a33")
    
    
def title(canvas, data):
    canvas.create_text(640,45,fill="#e2c24f",font="Times 80 italic bold",text="Connect Four")
    canvas.update
    
    
def dropChip (canvas, data, row, column, color):
    x1 = data.margin + data.square_width*column +25
    y1 =data.margin + data.square_height*row + 8.3
    x2 = x1 + data.square_width - 50
    y2 = y1 + data.square_height - 16.7
    canvas.create_oval(x1,y1,x2,y2, fill = color)
    
def drawAllChips (canvas, data):
    for g in range(0,6):
        for h in range(0,7):
            if data.game_board[g][h] == "o":
                dropChip(canvas, data,g,h,"#a72109")
            if data.game_board[g][h] == "x":
                dropChip(canvas, data,g,h,"#6297c1")
                dropChip(canvas, data,g,h,"#4a478d")
            
def get_col (data, col):
    for c in range(0,7):
        if col == c:
            print (c)
#############################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.margin = 50
    data.height = 720
    data.width = 1280
    data.board_width = data.width-2*data.margin
    data.board_height = data.height - 2*data.margin
    data.rows = 6
    data.cols = 7
    data.square_width = data.board_width/data.cols
    data.square_height = data.board_height/data.rows
    data.key_press_row = 0
    data.key_press_column = 0
    data.current_screen = "start"
    data.fill_color = "blue"
    data.playera = "H"
    data.playerb = "H"
    data.twoplayer = False
    data.aivhuman = False
    data.aivai = False
    data.ipt= 0
    data.current_player = 0
    data.made_move = False
    data.started = False
    data.col = 0
    data.game_board= [['','','','','','',''],
                      ['','','','','','',''],
                      ['','','','','','',''],
                      ['','','','','','',''],
                      ['','','','','','',''],
                      ['','','','','','','']]
    
def mousePressed(event, data):
    if data.current_screen == "start":
        if (event.x > data.margin) and (event.x < data.width - data.margin):
            if (event.y > data.margin + 50) and (event.y < data.margin + 250):
                data.current_screen = "int"
        if (event.x > data.margin) and (event.x < data.width*0.5 - data.margin):
            if (event.y > data.height*0.5) and (event.y <  data.height*0.75):
                data.current_screen = "rules"
    
    if data.current_screen == "grid":
        get_col(data, int((event.x/data.board_width)*7))
        
    if data.current_screen == "int":
        if (event.x > data.width/2 - 100) and (event.x < data.width/2 + 100):
            if (event.y > data.height/2-150) and (event.y < data.height/2 - 50):
                data.playera = "H"
            if (event.y > data.height/2+50) and (event.y < data.height/2 + 150):
                data.playerb = "H"
        if (event.x > (data.width/4)*3 - 100) and (event.x < (data.width/4)*3 + 100):
            if (event.y > data.height/2-150) and (event.y < data.height/2 - 50):
                data.playera = "A"
            if (event.y > data.height/2+50) and (event.y < data.height/2 + 150):
                data.playerb = "A"
            
    
    

def keyPressed(event, data):
    if data.current_screen == "start":
        if event.keysym == "s":
            data.current_screen = "int"
    if data.current_screen != "start":
        if event.keysym == "m":
            data.current_screen = "start"
    if data.current_screen == "grid":
        if event.keysym in ["0","1","2","3","4","5","6"]:
            data.col = int(event.keysym)
    if data.current_screen == "int":
        if event.keysym == "r":
            data.current_screen = "grid"
def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    if data.current_screen == "start":
        startScreen(canvas, data)
    elif data.current_screen == "int":
        intScrn(canvas, data)
    elif data.current_screen == "grid":
        draw_grid(canvas, data)
        if data.started != True:
            play_game(data)
            data.started = True
        drawAllChips(canvas, data)
    elif data.current_screen == "rules":
        rulesScrn(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
    




# run(1280,720)