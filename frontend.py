# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

def draw_grid(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height)
    canvas.create_rectangle(data.margin, data.margin, data.width-data.margin, data.height-data.margin)
    for i in range (data.rows):
        for j in range (data.cols):
            x = data.margin + j*data.square_width
            y = data.margin + i*data.square_height
            a = x + data.square_width
            b = y + data.square_height
            canvas.create_rectangle(x, y, a,b)
 
            
def startScreen (canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "#702121")
    title(canvas, data)
    playBtn(canvas, data)
    info1(canvas, data)
    info2 (canvas, data)
    settingBtn (canvas, data)

    
def playBtn (canvas, data):
    canvas.create_rectangle(data.margin, data.margin+50, data.width - data.margin, data.margin +250, fill = "#294168")
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
    
    
            
def dropChip (canvas, data):
    x1 = data.margin + data.square_width*data.key_press_row
    y1 = data.height - data.margin + data.square_height
    x2 = x1 + data.square_width
    y2 = y1 + data.square_height
    canvas.create_oval(x1,y1,x2,y2)
    
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

    
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    startScreen(canvas, data)

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