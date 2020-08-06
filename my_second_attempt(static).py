import numpy as np
import turtle
from tkinter import *

#______________________________________creating trutle and tkninter_________________________#

#creating Tk window and screen
window = Tk()
screen = Canvas(master = window, width = 520, height = 520, highlightthickness=0)
screen.pack()

#controlling the background color
turtle_screen = turtle.TurtleScreen(screen)
turtle_screen.bgcolor("grey")

#bending turtle and TTk by RawTurtle + custimizing turtle propirties
s = turtle.RawTurtle(turtle_screen)
s.pensize(1)
s.color('black')
s.speed(0)

#drawing shapes methods
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



#_____________________________setting app data holders and updating data_____________________#

#main data array
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

# declaring varlables
rows, columns, existedRed, existedBlue, existedGreen, redTurn, blueTurn = [], [], [], [], [], True, False

# appending data to rows and columns
for i in range(10):
    rows.append(325-(i*65))
    columns.append(-325 + (i*65))

#updataing data
def updateRed():
    
    '''
    I know that is the not best way to uptade data but i will just hard code it for now until my code start working
    '''
    #first of all i clear the previous data then update the data when calling the function
    existedRed.clear()
    for indexs, items in np.ndenumerate(board):
        if items == 1:
            existedRed.append(indexs)

    #drawing the stones after updating
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


    
        
#checking derctions
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
   


#___________________________________the main working envoirment in the game______________________________#

#drawing the red and blue stones
updateRed()
updateBlue()

#checking the valid moves for every red stone when it is red player turn
for i in range(len(existedRed)):
    row = existedRed[i][0]
    col = existedRed[i][1]
    
    #set bluefound as False for defulte and left moves for 0
    bluefound = False
    left_moves = 0
    
    #checking left for possible move until the answear is yes or no.
    for k in range(8):
        
        #checking left if is blue then bluefound is true
        if checkLeft(row, col - k) == -1:
            bluefound = True
            left_moves = left_moves +1
            
        #if  bluefounmd is true then see if the box beside the blue stone is empty
        if bluefound ==True:
            if checkLeft(row, col - k ) == 0:
                
                #if yes and it is true then chnge the empty '0' to '5' which represent possibleMoveCircle or green stone
                board[row, col - k - 1] = 5
                
                #after changing '0' to '5' it is time to update the board and draw the green circles after the update.
                updateGreen()
                
                #break the loop becuase i accomplished my goal from this loop
                break

        #check the left if it is empty but bluefound is false (when empty is beside red stone) then end the loop
        if checkLeft(row, col - k ) == 0:
            break
        
        #check the left if is red then end the loop
        if checkLeft(row,col - k ) == 1:
            break
    
    #flip the stones if this method was called
    def dodo():
        #right her we are calling the left_moves varluable to see how many times the blue was found beside the red
        #or in other words how many stones we need to flip
        for g in range(left_moves):
            g = g + 1
            board[row, col  - g] = 1
            
            
            
#do this method when mous is clicked.
def clickHandle(event):
    
    #creating this two varubles to store where where the mouse was clicked
    yr, xc = 0, 0
    
    #here i store the the y and x as rows(ry) and columns(xc)
    for i in range(10):
        if event.y > i*65 and event.y < (i*65) + 65:
            yr = i + 1
        if event.x > i*65 and event.x < (i*65) + 65:
            xc = i + 1
    
    #store xc and yr in the same list to be ab le to compare it to the green circles postions
    xy = [[yr,xc]]
    
    #do the checkiong as long as there is green stones 
    for i in range(len(existedGreen)):
        
        #if the mouse was clicked one the of any of the green stones then do the flipping
        '''but the problem is that it always flipping the first row and nothing else'''
        if xy[0] == list(existedGreen[i]):
            dodo()
            
            #draw the red stones after the board is updated
            updateRed()


#bend the click handle with the left mouse button.
screen.bind("<Button-1>", clickHandle)

#stay the screen on until i close it
window.mainloop()
