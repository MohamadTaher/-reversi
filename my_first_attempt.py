
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

def redplayer (x,y):
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
    
def blueplayer (x,y):
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

rows = []
column = []
def drawboard():
    def drawingsquares(x):
        for y in range (8):
            square(x, 260-(y*65)) 
            
    for i in range(8):
        drawingsquares(-260 + (i*65))
        rows.append([-260 + (i*65)])
        column.append([260-(i*65)])

    print(rows)
    print(column)

   
drawboard()
redplayer(rows[4], column[4])
blueplayer(-65,0)
blueplayer(0,65)
redplayer(0,0)
