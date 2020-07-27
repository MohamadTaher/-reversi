import numpy as np


print('')
print('system start')

rows = []
column = []

#                  0 1 2 3 4 5 6 7 8 9
board = np.array([[6,6,6,6,6,6,6,6,6,6], #0
                  [6,0,0,0,0,0,0,0,0,6], #1
                  [6,0,0,0,0,0,0,0,0,6], #2
                  [6,0,0,0,0,0,0,0,0,6], #3
                  [6,0,0,0,1,2,0,0,0,6], #4
                  [6,0,0,0,2,1,0,0,0,6], #5
                  [6,0,0,0,0,0,0,0,0,6], #6
                  [6,0,0,0,0,0,0,0,0,6], #7
                  [6,0,0,0,0,0,0,0,0,6], #8
                  [6,6,6,6,6,6,6,6,6,6]])#9


redpos = board[red]
print(redpos)


rightEmpty, leftEmpty, upEmpty, downEmpty = False, False, False, False


def checkRight(col,row):
    cRight = row + 1
    checkRight = board[col][cRight]
    return checkRight

def checkLeft(col,row):
    cLeft = row - 1
    checkLeft = board[col][cLeft]
    return checkLeft

def checkUp(col,row):
    cUp = col + 1
    checkUp = board[col][cUp]
    return checkUp

def checkDown(col,row):
    cDown = col - 1
    checkDown = board[col][cDown]
    return checkDown


def validMove(y,x):
    if checkRight(y,x) == 0:
        rightEmpty = True


for v in range(8):
    for h in range(8):
        validMove(v, h)
        
        
    
    
