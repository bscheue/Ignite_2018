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
    data.game_board= [['','','','','','',''],
                      ['','','','','','',''],
                      ['','','','x','','',''],
                      ['','','o','x','','x',''],
                      ['','','x','x','o','o',''],
                      ['o','x','o','o','o','x','']]
    
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

run(1280,720)