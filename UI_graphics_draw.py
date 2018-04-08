from tkinter import *

####################################
#Player movement graphics
####################################

def dropChip (canvas, data, row, column, color):
    x1 = data.margin + data.square_width*column +25
    y1 =data.margin + data.square_height*row + 8.3
    x2 = x1 + data.square_width - 50
    y2 = y1 + data.square_height - 16.7
    canvas.create_oval(x1,y1,x2,y2, fill = color)

def draw_grid(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill = "#7f81a8" )
    canvas.create_rectangle(data.margin, data.margin, 
        data.width-data.margin, data.height-data.margin,fill = "#dda02c")
        
    for i in range (data.rows):
        for j in range (data.cols):
            x = data.margin + j*data.square_width
            y = data.margin + i*data.square_height
            a = x + data.square_width
            b = y + data.square_height
            canvas.create_rectangle(x, y, a,b)
    player_color = "blank"
    if data.current_player == 0:
        player_color = "Red"
    if data.current_player == 1:
        player_color = "Blue"
        
        
    canvas.create_text(50, 25, fill = "#bd0093", 
                        font="Times 40 italic bold", text = player_color)

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
                dropChip(canvas, data,g,h,"#4a478d")

####################################
#Starting screen graphics
####################################

def intScrn (canvas, data):
    data.rectcolorah = "#0b485a"
    data.rectcolorbh = "#0b485a"
    data.rectcoloraa = "#0b485a"
    data.rectcolorba = "#0b485a"
    
    canvas.create_rectangle(0,0,data.width,data.height,fill = "#0ba23a")
    canvas.create_text(data.width/2, data.margin*2, fill = "#bd0093",
        font="Times 80 italic bold", text = "Select Players")
    canvas.create_text(236, data.height/2 - 100, fill = "#bd0093",
        font="Times 60 italic bold", text = "Player 1")
    canvas.create_text(236, data.height/2 + 100, fill = "#bd0093",
        font="Times 60 italic bold", text = "Player 2")
            
    if data.playera == "H":
        data.rectcolorah = "#0b4877"
    if data.playerb == "H":
        data.rectcolorbh = "#0b4877"
    if data.playera == "A":
        data.rectcoloraa = "#0b4877"
    if data.playerb == "A":
        data.rectcolorba = "#0b4877"
    
    canvas.create_rectangle(data.width/2 - 100,data.height/2-150,
        data.width/2 + 100,data.height/2 - 50, fill = data.rectcolorah)
    canvas.create_rectangle(data.width/2 - 100,data.height/2 +50, 
        data.width/2 + 100,data.height/2 + 150, fill = data.rectcolorbh)
    canvas.create_rectangle((data.width/4)*3 - 100,data.height/2-150,
        (data.width/4)*3 + 100,data.height/2 - 50, fill = data.rectcoloraa)
    canvas.create_rectangle((data.width/4)*3 - 100,data.height/2 +50, 
        (data.width/4)*3 + 100,data.height/2 + 150, fill = data.rectcolorba)
    canvas.create_text(data.width/2, data.height/2 - 100,
        fill = "#bd0093", font="Times 30 italic bold", text = "Human")
    canvas.create_text(data.width/2, data.height/2 + 100,
        fill = "#bd0093", font="Times 30 italic bold", text = "Human")
    canvas.create_text((data.width/4)*3, data.height/2 - 100,
        fill = "#bd0093", font="Times 40 italic bold", text = "AI")
    canvas.create_text((data.width/4)*3, data.height/2 + 100,
        fill = "#bd0093", font="Times 40 italic bold", text = "AI")
    
def winScrn (canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "0050f3")
    canvas.create_text(640, data.margin, fill = "#141519",
        font="Times 68 italic bold", text = data.current_player + "Wins")
    
def rulesScrn (canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "#27b6a3")
    canvas.create_text(640, data.margin, fill = "#141519",
        font="Times 68 italic bold", text = "Rules")
        
def intScreen2 (canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill = "#7f81a8" )
    canvas.create_rectangle(data.margin, data.margin, 
        data.width-data.margin, data.height-data.margin,fill = "#dda02c")
    canvas.create_text(640, 200, fill = "#141519",
        font="Times 68 italic bold", text =  data.winner + " wins! Press m to restart!")
    
def startScreen (canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "#702121")
    title(canvas, data)
    playBtn(canvas, data)
    info1(canvas, data)
    info2(canvas, data)

def playBtn (canvas, data):
    canvas.create_rectangle(data.margin, data.margin+50,
        data.width - data.margin, data.margin +250, fill = "#294168")
    canvas.create_text(640,195,fill="#e2c24f",
        font="Times 80 italic bold",text="Start")
    
def info1 (canvas, data):
    canvas.create_rectangle(data.margin,data.height*0.5, 
        data.width*0.5 - data.margin, data.height*0.75, fill = "#294168")
    canvas.create_text(data.width*0.25, data.height*0.625,
        fill="#e2c24f",font="Times 40 italic bold",text="Rules And Controls")
    
def info2 (canvas, data):
    canvas.create_rectangle(data.width - data.margin,data.height*0.5, 
        data.width*0.5 + data.margin, data.height*0.75, fill = "#294168")
    canvas.create_text(data.width*0.75, data.height*0.625,fill="#e2c24f",
        font="Times 40 italic bold",text="Project Info")
    

    

def title(canvas, data):
    canvas.create_text(640,45,fill="#e2c24f",font="Times 80 italic bold",
        text="Connect Four")