# get all winning combinations for a player at all times during the game
# to select the most appropriate location by calculating difference between 
# current players winning combinations and opponents winning combination



def getMirrorGrid(newGrid):
    temp = newGrid[0]
    newGrid[0] = newGrid[2]
    newGrid[2] = temp
    temp = newGrid[3]
    newGrid[3] = newGrid[5]
    newGrid[5] = temp
    temp = newGrid[6]
    newGrid[6] = newGrid[8]
    newGrid[8] = temp
    return newGrid

# shape 1 -> circle
# shape 2 -> cross
def getWinningCombination(grid):
    winCircle = 0
    winCross = 0
    tempGrid = grid
    for i in range(9):
        grid = tempGrid
        if(grid[i] == 1 or grid[i] == 2):
            modVal = i%3
            if(modVal == 0 or modVal == 2):
                if(modVal == 2):
                    grid = getMirrorGrid(grid)
                checkBound = i-6
                if(checkBound>=0 and checkBound<=8):
                    if(grid[i-3]==0 and grid[checkBound]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound = i+2
                if(checkBound>=0 and checkBound<=8):
                    if(grid[i+1]==0 and grid[checkBound]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound = i+6
                if(checkBound>=0 and checkBound<=8):
                    if(grid[i+3]==0 and grid[checkBound]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound1 = i-3
                checkBound2 = i+3
                if((checkBound1>=0 and checkBound1<=8) and (checkBound2>=0 and checkBound2<=8)):
                    if(grid[checkBound2]==0 and grid[checkBound1]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound = i+8
                if(checkBound>=0 and checkBound<=8):
                    if(grid[i+4]==0 and grid[checkBound]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound = i-4
                if(checkBound>=0 and checkBound<=8):
                    if(grid[i-2]==0 and grid[checkBound]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
            elif (modVal==1):
                checkBound = i+6
                if(checkBound>=0 and checkBound<=8):
                    if(grid[i+3]==0 and grid[checkBound]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound = i-6
                if(checkBound>=0 and checkBound<=8):
                    if(grid[i-3]==0 and grid[checkBound]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound1 = i-1
                checkBound2 = i+1
                if((checkBound1>=0 and checkBound1<=8) and (checkBound2>=0 and checkBound2<=8)):
                    if(grid[checkBound2]==0 and grid[checkBound1]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound1 = i-4
                checkBound2 = i+4
                if((checkBound1>=0 and checkBound1<=8) and (checkBound2>=0 and checkBound2<=8)):
                    if(grid[checkBound2]==0 and grid[checkBound1]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound1 = i-2
                checkBound2 = i+2
                if((checkBound1>=0 and checkBound1<=8) and (checkBound2>=0 and checkBound2<=8)):
                    if(grid[checkBound2]==0 and grid[checkBound1]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
                checkBound1 = i-3
                checkBound2 = i+3
                if((checkBound1>=0 and checkBound1<=8) and (checkBound2>=0 and checkBound2<=8)):
                    if(grid[checkBound2]==0 and grid[checkBound1]==0):
                        if(grid[i] == 1):
                            winCircle = winCircle + 1
                        else:
                            winCross = winCross + 1
    print("Wincirlces -> " + str(winCircle))
    print("Wincrosses -> " + str(winCross))


while(True):
    grid = list(map(int,input().split()))
    getWinningCombination(grid)