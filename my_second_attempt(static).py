import numpy as np
#                  0 1 2 3 4 5 6 7 8 9
board = np.array([[6,6,6,6,6,6,6,6,6,6], #0
                  [6,0,0,0,0,0,0,0,0,6], #1
                  [6,0,0,0,0,0,0,0,0,6], #2
                  [6,0,0,0,0,0,0,0,0,6], #3
                  [6,0,0,0,1,0,0,0,0,6], #4
                  [6,2,0,1,0,2,0,0,0,6], #5
                  [6,0,0,0,0,0,0,0,0,6], #6
                  [6,0,0,0,0,0,0,0,0,6], #7
                  [6,0,0,0,0,0,0,0,0,6], #8
                  [6,6,6,6,6,6,6,6,6,6]])#9

def validMove(row,col):
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


existedRed, existedBlue = [], []
for indexs, items in np.ndenumerate(board):
    if items == 1:
        existedRed.append(indexs)
    if items == 2:
        existedBlue.append(indexs)

   
def checkRedHor(row):
    if np.any(board[row, :] == 1):
        return np.argwhere(board[row, :] == 1)
    else:
        return False  
def checkRedVer(col):
    if np.any(board[:, col] == 1):
        return np.argwhere(board[:, col] == 1)
    else:
        return False
def checkBlueHor(row):
    if np.any(board[row, :] == 2):
        return np.argwhere(board[row, :] == 2)
    else:
        return False  
def checkBlueVer(col):
    if np.any(board[:, col] == 2):
        return np.argwhere(board[:, col] == 2)
    else:
        downEmpty = True
        return False


print('red stones:', existedRed, "\n", 'blue stones:', existedBlue, '\n')
for i in range(len(existedRed)):
    h = existedRed[i][0]
    if np.any(checkBlueHor(h) != False):
        if np.any(existedRed[i][1] > checkBlueHor(h)):
            print(checkBlueHor(h), 'is the blue stone location at the row', h, '\n the blue is also on the left of', existedRed[i][1])
        if np.any(existedRed[i][1] < checkBlueHor(h)):#on the right
            print(checkBlueHor(h), 'is the blue stone location at the row', h, '\n the blue is also on the right of', existedRed[i][1])    
        
    else:
        print('there is no blue pleyer at row', h, '\n')    
    



redTurn = True
blueTurn = False

if redTurn == True:
    blueTurn = True
    redTurn = False
else:
    blueTurn = True
    redTurn = False










        
