import copy
from UI_graphics_draw import*
from frontend_two_player import *

def make_board(data):
    board = []
    for i in range(data.rows):
        board.append(["-" for i in range(data.cols)])
    return board
    
def clearBoard (data):
    init(data)

def init(data):
    data.rows = 6
    data.cols = 7
    data.margin = 50
    data.height = 720
    data.width = 1280
    
    data.board_width = data.width-2*data.margin
    data.board_height = data.height - 2*data.margin
    data.square_width = data.board_width/data.cols
    data.square_height = data.board_height/data.rows
    
    data.current_screen = "start"

    data.playera = "H"
    data.playerb = "H"
    data.twoplayer = False
    data.aivhuman = False
    data.aivai = False

    data.current_player = 0
    data.made_move = False
    data.started = False
    data.placed_col = -1
    data.game_board = make_board(data)
    data.winner ="" 
    data.clickwidth = 0

def mousePressed(event, data):
    if data.current_screen == "start":
        if (event.x > data.margin) and (event.x < data.width - data.margin):
            if (event.y > data.margin + 50) and (event.y < data.margin + 250):
                data.current_screen = "int"
        if (event.x > data.margin) and (event.x < data.width*0.5 - data.margin):
            if (event.y > data.height*0.5) and (event.y <  data.height*0.75):
                data.current_screen = "rules"
            
    if data.current_screen == "int":
        if (event.x > data.width/2 - 100) and (event.x < data.width/2 + 100):
            if (event.y > data.height/2-150) and (event.y < data.height/2 - 50):
                data.playera = "H"
            if (event.y > data.height/2+50) and (event.y < data.height/2 + 150):
                data.playerb = "H"
        if (event.x >(data.width/4)*3-100) and (event.x < (data.width/4)*3+100):
            if (event.y > data.height/2-150) and (event.y < data.height/2 - 50):
                data.playera = "A"
            if (event.y > data.height/2+50) and (event.y < data.height/2 + 150):
                data.playerb = "A"
    
    if data.current_screen == "grid":
        data.clickwidth = (event.x - 50)
        col = (int)(data.clickwidth // data.square_width)
        data.made_move = True
        data.placed_col = col
        
def keyPressed(event, data):
    if data.current_screen == "start":
        if event.keysym == "s":
            data.current_screen = "int"
    if data.current_screen != "start":
        if event.keysym == "m":
            data.current_screen = "start"
            clearBoard(data)
    #if data.current_screen == "grid":
        #if event.keysym in ["1","2","3","4","5","6","7"]:
           # data.made_move = True
            #data.placed_col = int(event.keysym)-1

    if data.current_screen == "int":
        if event.keysym == "r":
            data.current_screen = "grid"
            data.game_board = make_board(data)
            data.made_move = True
            
            
def timerFired(data): pass

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
        drawAllChips (canvas, data)
    elif data.current_screen == "rules":
        rulesScrn(canvas, data)
    elif data.current_screen == "end":
        intScreen2(canvas, data)

#Run function for animation barebone
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)

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
    
####################################

run(1280,720)