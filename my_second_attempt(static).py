import numpy as np
import turtle
from tkinter import *


window = Tk()
screen = Canvas(master = window, width = 520, height = 520, highlightthickness=0)
screen.pack()

turtle_screen = turtle.TurtleScreen(screen)
turtle_screen.bgcolor("grey")

s = turtle.RawTurtle(turtle_screen)
s.pensize(1)
s.color('black')
s.speed(0)

#drawing shapes
def circle(f):
    for i in range(18):
        s.forward(f)
        s.left(20)
def square (x,y):
    s.up()
    s.goto(x,y)
    s.down()
    for m in range(4):
        s.forward(65)
        s.right(90)
def drawboard():
    def drawingboxs(x):
        for y in range (8):
            square(x, 260-(y *65))   
    for i in range(8):
        drawingboxs(-260 + (i*65))
def possibleMoveCircle(y, x):
    s.up()
    s.color('black', 'green')
    s.begin_fill()
    s.goto(x+16, y-9)
    s.setheading(-135)
    s.down()
    circle(10)
    s.up()
    s.setheading(0)
    s.end_fill()
def redplayer (y, x):
    s.up()
    s.color('black', 'red')
    s.begin_fill()
    s.goto(x+16, y-9)
    s.setheading(-135)
    s.down()
    circle(10)
    s.up()
    s.setheading(0)
    s.end_fill()
def blueplayer (y, x):
    s.up()
    s.color('black', 'blue')
    s.begin_fill()
    s.goto(x+16, y-9)
    s.setheading(-135)
    s.down()
    circle(10)
    s.up()
    s.setheading(0)
    s.end_fill()



#                  0 1 2 3 4 5 6 7 8 9
board = np.array([[6,6,6,6,6,6,6,6,6,6], #0
                  [6,0,0,0,0,0,0,0,0,6], #1
                  [6,0,0,0,0,0,0,0,0,6], #2
                  [6,0,0,-1,0,1,0,0,0,6], #3
                  [6,0,0,-1,-1,1,0,0,0,6], #4
                  [6,0,0,0,0,0,0,0,0,6], #5
                  [6,0,0,0,0,0,0,0,0,6], #6
                  [6,0,0,0,0,0,0,0,0,6], #7
                  [6,0,0,0,0,0,0,0,0,6], #8
                  [6,6,6,6,6,6,6,6,6,6]])#9

redTurn, blueTurn = True, False
rows, columns, existedRed, existedBlue, existedGreen = [], [], [], [], []
for i in range(10):
    rows.append(325-(i*65))
    columns.append(-325 + (i*65))



        

def updateRed():
    existedRed.clear()
    for indexs, items in np.ndenumerate(board):
        if items == 1:
            existedRed.append(indexs)

    for i in range(len(existedRed)):
        row = existedRed[i][0]
        col = existedRed[i][1]
        redplayer(rows[row], columns[col])
        
def updateBlue():
    existedBlue.clear()
    for indexs, items in np.ndenumerate(board):
        if items == -1:
            existedBlue.append(indexs)

    for i in range(len(existedBlue)):
        row = existedBlue[i][0]
        col = existedBlue[i][1]
        blueplayer(rows[row], columns[col])

def updateGreen():
    existedGreen.clear()        
    for indexs, items in np.ndenumerate(board):
        if items == 5:
            existedGreen.append(indexs)
    
    for i in range(len(existedGreen)):
        grow = existedGreen[i][0]
        gcol = existedGreen[i][1]
        possibleMoveCircle(rows[grow], columns[gcol])


    
        
        
def checkRight(row,col):
    cRight = col + 1
    checkRight = board[row][cRight]
    return checkRight
def checkLeft(row,col):
    cLeft = col - 1
    checkleft = board[row][cLeft]
    return checkleft
def checkUp(row,col):
    cUp = row + 1
    checkUp = board[cUp][col]
    return checkUp
def checkDown(row,col):
    cDown = row - 1
    checkDown = board[cDown][col]
    return checkDown
   


while redTurn:
    
    updateRed()
    updateBlue()
       
    for i in range(len(existedRed)):
        row = existedRed[i][0]
        col = existedRed[i][1]
        bluefound = False
        left_moves = 0
        for k in range(8): 
            if checkLeft(row, col - k) == -1:
                bluefound = True
                left_moves = left_moves +1
            if bluefound ==True:
                if checkLeft(row, col - k ) == 0:
                    board[row, col - k - 1] = 5
                    updateGreen()
                    bluefound = False



            if checkLeft(row, col - k ) == 0:
                break
            if checkLeft(row,col - k ) == 1:
                break
            
        def dodo():
            for g in range(left_moves):
                g = g + 1
                board[row, col  - g] = 1
            print(board, 'leftare', left_moves)
            
    break



def clickHandle(event):
    yr, xc = 0, 0
    for i in range(10):
        if event.y > i*65 and event.y < (i*65) + 65:
            yr = i + 1
        if event.x > i*65 and event.x < (i*65) + 65:
            xc = i + 1
    xy = [[yr,xc]]
    for i in range(len(existedGreen)):
        if xy[0] == list(existedGreen[i]):
            dodo()
            updateRed()


screen.bind("<Button-1>", clickHandle)
window.mainloop()
