from os import system

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

def createBoard():
    #initialise board with empty strings
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    return board

def clearScreen():
    system('cls') 

def drawBoard(board):
    clearScreen()
    print('┌─┬─┬─┐')
    for i in range(0,len(board)):
        print('|{}|{}|{}|'.format(board[i][0], board[i][1], board[i][2]))
        if i < len(board)-1:
            print('├─┼─┼─┤')
    print('└─┴─┴─┘')

def getMove(board):
    clearScreen()
    drawBoard(board)
    move = input("Please select your position from 1 to 9: ")
    found = False
    for num in validSelection:
        if num == move:
            found = True
            break #break once validated, no need to continue iteration
    if found == True:
        if checkFree(move, board) == True:
            applyMark(move, board)
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

def checkFree(move, board):
    position = getArrayPosition(move)
    if board[position[0]][position[1]] == ' ':
        return True
    else:
        return False
    
def applyMark(move, board):
    global turn
    position = getArrayPosition(move)

    #check which turn is it and apply correct mark
    if turn % 2 == 0:
        board[position[0]][position[1]] = 'X'
    else:
        board[position[0]][position[1]] = 'O'
    turn += 1 #mark applied successfully so increment turn

def checkWin(value, board):
    for combo in winningCombos:
        winCount = 0 #count to hold num of cells with value in
        for cell in combo:
            if board[cell[0]][cell[1]] == value:
                winCount += 1
        if winCount == 3:
            return True
    return False

#Program initialisation
board = createBoard()
complete = False
while complete == False:
    getMove(board)
    checkX = checkWin('X', board)
    checkO = checkWin('O', board)
    if checkX == True:
        drawBoard(board)
        print('Winner winner chicken dinner!! X wins')
        complete = True
    elif checkO == True:
        drawBoard(board)
        print('Winner winner chicken dinner!! O wins')
        complete = True
    elif turn > 8:
        drawBoard(board)
        print('No winners this time :(')
        complete = True