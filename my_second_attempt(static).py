"""
    1.1: check if there is a blue player horizontally virtually or diagonally.

    1.2: horizontally by checking the same row,
     vertically by checking the same column,
     diagonally by checking rows and columns at the same time.

    1.3: if yes than check its right/left when horizontally,
     up/down    when vertically,
     and two directions when diagonally.

    1.4: if any of the valid moves is true, than change 0 and 1||2 to number 5
"""
import numpy as np
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


existedRed = []
existedBlue = []
for indexs, items in np.ndenumerate(board):
    if items == 1:
        existedRed.append(indexs)
    if items == 2:
        existedBlue.append(indexs)

    
def checkRedHor(row):
    if np.any(board[row, :] == 1):
        return np.argwhere(board[row, :] == 1)
def checkRedVer(col):
    return np.argwhere(board[:, col] == 1)
def checkBlueHor(row):
    return np.argwhere(board[row, :] ==2)
def checkBlueVer(col):
    return np.argwhere(board[:, col] == 2)

for i in range(10):
    if checkRedHor(i) != None:
        print(checkRedHor(i))

#this function is currently is not used.
def validMove(row,col):
    rightEmpty, leftEmpty, upEmpty, downEmpty = False, False, False, False

    def checkRight(row,col):
        cRight = row + 1
        checkRight = board[row][cRight]
        return checkRight
    def checkLeft(row,col):
        cLeft = row - 1
        checkLeft = board[row][cLeft]
        return checkLeft
    def checkUp(row,col):
        cUp = col + 1
        checkUp = board[row][cUp]
        return checkUp
    def checkDown(row,col):
        cDown = col - 1
        checkDown = board[row][cDown]
        return checkDown

    if checkRight(row,col) == 0:
        rightEmpty = True
    if checkLeft(row,col) == 0:
        leftEmpty = True
    if checkUp(row,col) == 0:
        upEmpty = True 
    if checkDown(row,col) == 0:
        downEmpty = True


        
        
