from os import system

#initialise board with empty strings
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#array co-ordinates for all winning combinations
winningCombos = [[(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
                [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
                [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]

#all valid characters for move selection
validSelection = ['1','2','3','4','5','6','7','8','9']

#location edge cases, require special treatment when calculating position in array
edgeCases = ['3','6','9']

#stores current turn number, used to decide if X or O is displayed
turn = 0

def clearScreen():
    system('cls') 

def drawSelectionBoard():
    print('┌─┬─┬─┐')
    print('|{}|{}|{}|'.format(board[0][0], board[0][1], board[0][2]))
    print('├─┼─┼─┤')
    print('|{}|{}|{}|'.format(board[1][0], board[1][1], board[1][2]))
    print('├─┼─┼─┤')
    print('|{}|{}|{}|'.format(board[2][0], board[2][1], board[2][2]))
    print('└─┴─┴─┘')

def getMove():
    clearScreen()
    drawSelectionBoard()
    move = input("Please select your position from 1 to 9: ")
    found = False
    for num in validSelection:
        if num == move:
            found = True
            break
    if found == True:
        if checkFree(move) == True:
            applyMark(move)
    else:
        getMove()
    return move

def getArrayPosition(move):
    position = list(divmod(int(move),3))
    position[1] -= 1 #subtract 1 from the column value due to divmod value starting from 1
    if move in edgeCases:
        position[0] -= 1
        position[1] = 2  
    return position

def checkFree(move):
    position = getArrayPosition(move)
    if board[position[0]][position[1]] == ' ':
        return True
    else:
        return False
    
def applyMark(move):
    global turn
    position = getArrayPosition(move)

    #check which turn is it and apply correct mark
    if turn % 2 == 0:
        board[position[0]][position[1]] = 'X'
    else:
        board[position[0]][position[1]] = 'O'
    turn += 1 #mark applied successfully so increment turn

def checkWin(value):
    for combo in winningCombos:
        winCount = 0 #count to hold num of cells with value in
        for cell in combo:
            if board[cell[0]][cell[1]] == value:
                winCount += 1
        if winCount == 3:
            return True
    return False

complete = False
while complete == False:
    getMove()
    checkX = checkWin('X')
    checkO = checkWin('O')
    if checkX == True:
        clearScreen()
        drawSelectionBoard()
        print('Winner winner chicken dinner!! X wins')
        complete = True
    elif checkO == True:
        clearScreen()
        drawSelectionBoard()
        print('Winner winner chicken dinner!! O wins')
        complete = True
    elif turn > 8:
        clearScreen()
        drawSelectionBoard()
        print('No winners this time :(')
        complete = True