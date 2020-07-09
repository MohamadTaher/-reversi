


import random
import turtle
wn = turtle.Screen()
wn.bgcolor("grey")
wn.setup(520,520)

s = turtle.Turtle()
s.pensize(1)
s.color('black')
s.speed(0)

#creating lists and booleans
existedRedPlayers = []
existedBluePlayers = []
rows = []
column = []




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

def possibleMoveCircle(x,y):
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

def redplayer (x,y):
    s.up()
    s.color('black', 'red')
    s.begin_fill()
    existedRedPlayers.append([x , y])
    s.goto(x+16, y-9)
    s.setheading(-135)
    s.down()
    circle(10)
    s.up()
    s.setheading(0)
    s.end_fill()

def blueplayer (x,y):
    s.up()
    s.color('black', 'blue')
    s.begin_fill()
    existedBluePlayers.append([x, y])
    s.goto(x+16, y-9)
    s.setheading(-135)
    s.down()
    circle(10)
    s.up()
    s.setheading(0)
    s.end_fill()





#defin the steps  
for i in range(8):
    rows.append(-260 + (i*65))
    column.append(260-(i*65))

def drawboard():
    def drawingbox(x):
        for y in range (8):
            square(x, 260-(y *65))   
    for i in range(8):
        drawingbox(-260 + (i*65))

isEmpty = False
def emptyBoxe(x, y):

    for items in existedRedPlayers:
        if items == [x , y]:
            print("it worked")
        else:
            isEmpty = True

        
    if isEmpty == True:
        possibleMoveCircle(x, y)






#calling the fanction to do the works
redplayer(rows[3], column[3])
blueplayer(rows[4], column[3])
redplayer(rows[4], column[4])
blueplayer(rows[3], column[4])
print(existedRedPlayers)
print(existedBluePlayers)
    
#here it work perfectly
emptyBoxe(65,110)


#but whene i try this one, it does not work
emptyBoxe( existedRedPlayers[0, 0])





















