import numpy as np
#                  0 1 2 3 4 5 6 7 8 9
board = np.array([[6,6,6,6,6,6,6,6,6,6], #0
                  [6,0,0,0,0,0,0,0,0,6], #1
                  [6,0,0,0,0,0,0,0,0,6], #2
                  [6,0,0,0,0,0,0,0,0,6], #3
                  [6,0,0,0,0,0,0,0,0,6], #4
                  [6,0,0,0,0,0,0,0,0,6], #5
                  [6,0,0,0,0,0,0,0,0,6], #6
                  [6,0,0,0,0,0,1,2,0,6], #7
                  [6,0,0,0,0,0,0,0,0,6], #8
                  [6,6,6,6,6,6,6,6,6,6]])#9

redTurn, blueTurn = True, False
existedRed, existedBlue = [], []

for indexs, items in np.ndenumerate(board):
    if items == 1:
        existedRed.append(indexs)
    if items == 2:
        existedBlue.append(indexs)

existedStones = existedRed + existedBlue


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



if checkLeft(7,7) == 2 or 1:
    print('hi')
   
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


print('red stones:', existedRed, "\n", 'blue stones:', existedBlue, '\n', existedStones)
while redTurn:
    for i in range(len(existedRed)):
        rowOfRed = existedRed[i][0]
        colOfRed = existedRed[i][1]
        if checkLeft(rowOfRed,colOfRed) == 2:
            print('on the left')
            break
        else:
            print('not on the left')
            break
    

    
    
    





#if redTurn == True:
#    blueTurn = True
#    redTurn = False
#else:
#    blueTurn = True
#    redTurn = False








        
