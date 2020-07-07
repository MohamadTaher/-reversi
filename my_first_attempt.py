
import random
import turtle
wn = turtle.Screen()
wn.bgcolor("grey")
wn.setup(520,520)

s = turtle.Turtle()
s.pensize(1)
s.color('black')
s.speed(0)

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

existedRedPlayersX = []
existedRedPlayersY = []

def redplayer (x,y):
    s.up()
    s.color('black', 'red')
    s.begin_fill()

    existedRedPlayersX.append(x)
    existedRedPlayersY.append(y)        

    s.goto(x+16, y-9)
    s.setheading(-135)
    s.down()
    circle(10)
    s.up()
    s.setheading(0)
    s.end_fill()

existedBluePlayersX = []
existedBluePlayersY = []
 
def blueplayer (x,y):
    s.up()
    s.color('black', 'blue')
    s.begin_fill()

    existedBluePlayersX.append(x)
    existedBluePlayersY.append(y) 
    
    s.goto(x+16, y-9)
    s.setheading(-135)
    s.down()
    circle(10)
    s.up()
    s.setheading(0)
    s.end_fill()


def possibleMoveCircle (x,y):
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
    

rows = []
column = []
for i in range(8):
    rows.append(-260 + (i*65))
    column.append(260-(i*65))

def drawboard():
    def drawingbox(x):
        for y in range (8):
            square(x, 260-(y *65))   
    for i in range(8):
        drawingbox(-260 + (i*65))




        print("hi")
        possibleMoveCircle(existedBluePlayersX[1] -65, column[1])
    if c< len (existedBluePlayersX):
        break



   

#drawboard()
redplayer(rows[3], column[3])
blueplayer(rows[4], column[3])
redplayer(rows[4], column[4])
blueplayer(rows[3], column[4])



while (set(existedBluePlayersX) & set(existedRedPlayersX)):
    c = 0
    for i in range(len (existedBluePlayersX)):
        c+=1
        print("hi")
        possibleMoveCircle(existedBluePlayersX[1] -65, column[1])
    if c< len (existedBluePlayersX):
        break







