




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
xred = []



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



#1) isemtpy == True >>> then draw (isempty == no red or blue stones)
#2) if isempty == False >>>  check the box beside red and blue stones if isempty  
isEmpty = True


def emptyBoxes(xPlayer):
    rightEmpty = False
    leftEmpty = False
    upEmpty = False
    downEmpty = False
    xs = []
    ys = []

    for items in xPlayer:
        xs.append(items[0])
        ys.append(items[1])                    
    print('xs are',xs,'     ys are',ys)

        
    for xitem in xs:
        checkRight = xitem +65
        checkLeft = xitem -65
        

        if checkRight not in xs:
            rightEmpty = True
            print(rightEmpty, 'right')
                    
        if checkLeft not in xs:
            leftEmpty = True
            print(rightEmpty, 'left')
            
        
        if rightEmpty == True:
            possibleMoveCircle(xitem + 65, xPlayer[0][1])
            print(items[0])
            rightEmpty = False
             
        if leftEmpty == True:
            possibleMoveCircle(xitem - 65, xPlayer[0][1])
            print(items[0])
            leftEmpty = False


            


#calling the fanction to do the works
            
redplayer(rows[3], column[3])
#blueplayer(rows[4], column[3])
redplayer(rows[4], column[4])
#blueplayer(rows[3], column[4])
#redplayer(rows[3], column[3])
#redplayer(rows[4], column[3])

print('existed red player:', existedRedPlayers)



redTurn = True
blueTurn = False

if redTurn == True:
    emptyBoxes(existedRedPlayers)
    blueTurn = True
    redTurn = False





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



