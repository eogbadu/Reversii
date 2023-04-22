# File:             proj2.py
# Author:           Ekele Ogbadu
# Date:             12 APR 2019
# Section:          09
# E-mail:           eogbadu1@umbc.edu
# Description:      This program is a simple version of the game reversii
#                   where the user plays against a simple AI



COLUMN_POS = 4
ROW_POS    = 1
ROW        = 8
COLUMN     = 8
X_CHAR     = "X"
O_CHAR     = "O"
UNDERSCORE = "_"

###################################################################### 
# printBoard() prints the Reversi board with the right headings 
# Parameters:  board; a 2D list of single-char strings (X, O, _) 
# Output:      None     
def printBoard(board):

    print("Current board state:")
    # print header
    print("_|0|1|2|3|4|5|6|7")

    # print each row
    # for example: 3|_|_|_|X|O|_|_|_|
    for i in range(len(board)):
        print(str(i) + "|" + "|".join(board[i]) + "|")

######################################################################
# startGame()         Sets the initial board with X's and O's at the
#                     center of the board
# Parameters:         width; an integer specifying row width
#                     height; an integer specifying the height of the board
# Output:             board; a 2D list of single-char strings

def startGame(width, height):
    # Create list to store rows
    row = []

    # Create a row of underscores the lenght of "width"
    for i in range(width):
       row.append("_")

    # Create a 2nd list to append to
    board = []

    # Create a 2-D list by appending above row to the board list
    for i in range(height):
        board.append(row[:])

    # Calculate center positions
    firstColumn  = int((width / 2) - 1)
    secondColumn = int(width / 2)
    firstRow     = int((height / 2) - 1)
    secondRow    = int(height / 2)
    
    # Change characters at the center of the board to X's and O's
    board[firstRow][firstColumn]   = X_CHAR
    board[firstRow][secondColumn]  = O_CHAR
    board[secondRow][firstColumn]  = O_CHAR
    board[secondRow][secondColumn] = X_CHAR

    printBoard(board)

    return board

######################################################################
# getValidMoves()   finds all valid moves available to the player
#                   for each play
# Parameters:       board; a 2D list of single-char strings
#                   player; A single-char string character of the
#                           player making the current move
#                   enemy; A single-char string character of the               
#                           player not making the current move 
# Output:           validMoves; a string with the valid moves
def getValidMoves(board, player, enemy):
    count = 0           # int variable that is used in for/while loop
    count2 = 0          # int variable that is used in for/while loop
    isGood = True
    validMoves = []

    # loop for the lenght of the board
    for i in range(len(board)):
        if player in board[i]:
            while count < ROW:
                if board[i][count] == player:
                    
                    # Find enemy players on the same row and in columns before player position
                    if board[i][count - 1] == enemy:
                        count2 = count - 1
                        
                        # set start position
                        startPosition = "[" + str(i) + ", " + str(count) + "]"

                        # go through row backwards till you find an underscore
                        while count2 > 0 and board[i][count2] != UNDERSCORE:
                            count2 -= 1

                            # check if the player character is between the start position
                            # and the underscore
                            if board[i][count2] == player:
                                isGood = False
                                
                        # set end position when you reach the underscore
                        if count2 >= 0 and board[i][count2] == UNDERSCORE:
                            endPosition = "[" + str(i) + ", " + str(count2) + "]"

                            # put start and end position in a list
                            row = [startPosition, endPosition]
                            
                            # check if row is already in valid moves list
                            # and that there is no player char in the row
                            # before setting it as a vaid move
                            if row not in validMoves and isGood:
                                validMoves.append(row)
                                
                        isGood = True
                    # Find enemy players on the same row and in columns after player position
                    if count + 1 < ROW:
                        if board[i][count + 1] == enemy:
                            count2 = count + 1

                            # set start position
                            startPosition = "[" + str(i) + ", " + str(count) + "]"
                            
                            # go through row forward till you find an underscore
                            while count2 < ROW and board[i][count2] != UNDERSCORE:

                                # check if the player character is between the start position
                                # and the underscore
                                if board[i][count2] == player:
                                    isGood = False
                                count2 += 1

                            # set end position when you reach the underscore
                            if count2 < ROW and board[i][count2] == UNDERSCORE:
                                endPosition = "[" + str(i) + ", " + str(count2) + "]"

                                # put start and end position in a list
                                row = [startPosition, endPosition]
                                
                                # check if row is already in valid moves list                                                                  
                                # and that there is no player char in the row
                                # before setting it as a vaid move  
                                if row not in validMoves and isGood:
                                    validMoves.append(row)
                        isGood = True
                    # Find enemy players in the same column and in the row above the player
                    if i > 0:
                        if board[i - 1][count] == enemy:
                            count2 = i - 1

                            # set start position
                            startPosition = "[" + str(i) + ", " + str(count) + "]"

                            # go through column upwards till you find an underscore
                            while count2 > 0 and board[count2][count] != UNDERSCORE:
                                count2 -= 1

                                # check if the player character is between the start position
                                # and the underscore
                                if board[count2][count] == player:
                                    isGood = False

                            # set end position when you reach the underscore
                            if count2 >= 0 and board[count2][count] == UNDERSCORE:
                                endPosition = "[" + str(count2) + ", " + str(count) + "]"

                                # put start and end position in a list
                                row = [startPosition, endPosition]

                                # check if row is already in valid moves list             
                                # and that there is no player char in the row   
                                # before setting it as a vaid move 
                                if row not in validMoves and isGood:
                                    validMoves.append(row)
                        isGood = True
                    # Find enemy players in the same column and in the row below the player
                    if i + 1 < COLUMN:
                        if board[i + 1][count] == enemy:
                            count2 = i + 1

                            # set start position
                            startPosition = "[" + str(i) + ", " + str(count) + "]"

                            # go through column downwards till you find an underscore 
                            while count2 < COLUMN and board[count2][count] != UNDERSCORE:

                                # check if the player character is between the start position
                                # and the underscore
                                if board[count2][count] == player:
                                    isGood = False
                                count2 += 1
                                
                            # set end position when you reach the underscore
                            if count2 < COLUMN and board[count2][count] == UNDERSCORE:
                                endPosition = "[" + str(count2) + ", " + str(count) + "]"

                                # put start and end position in a list
                                row = [startPosition, endPosition]

                                # check if row is already in valid moves list
                                # and that there is no player char in the row 
                                # before setting it as a vaid move  
                                if row not in validMoves and isGood:
                                    validMoves.append(row)
                        isGood = True
                count += 1
            count = 0
    return validMoves

######################################################################
# getUserInput()    gets moves from the player
# Parameters:       none;
# Output:           userInput; a string with the players input
def getUserInput():
    userInput = input("Enter a move: ")
    return userInput

######################################################################
# inputIsValidated() validates the input entered by the player
# Parameters:        userInput; a string with the players input
#                    validMoves; a 2-D list with the valid moves
#                                available to the player
# Output:            isValid; a boolean stating whether the user input
#                             is valid
def inputIsValidated(userInput, validMoves):

    inputList = []
    isValid = False
    inputList = userInput.split()

    # check that user put exactly two numbers (number lenght doesn't
    # matter).
    if len(inputList) == 2:
        inputString = "[" + str(inputList[0]) + ", " + str(inputList[1]) + "]"

        # Check that the number entered matches one in the valid input
        # list
        for i in range(len(validMoves)):
            if str(inputString) == str(validMoves[i][1]):
                isValid = True

    return isValid

######################################################################
# processInput()    processes the input from player and AI
# Parameters:       board; a 2D list of single-char strings
#                   userInput; a string holding the input
#                   validMoves; a string with the valid moves
#                   letter; a single char string that the positions
#                           will be changed into
# Output:           wins; an integer used to keep track of number
#                         of wins
def processInput(userInput, validMoves, board, letter):
    wins = 0
    inputList = userInput.split()
    inputString = "[" + inputList[0] + ", " + inputList[1] + "]"

    # check if there are valid moves for both the player and AI
    isCompleteAi = isGameComplete(board, O_CHAR, X_CHAR)
    isCompletePlayer = isGameComplete(board, X_CHAR, O_CHAR)

    
    if isCompleteAi == False or isCompletePlayer == False:
        for i in range(len(validMoves)):

            # get start point if input is valid
            if inputString == validMoves[i][1]:
                validMovesString = validMoves[i][0]
                startPoint = validMoves[i][0]

                # get end point for going through a row
                if inputList[0] == validMovesString[1]:
                    count = int(startPoint[COLUMN_POS])
                    endPoint = int(inputList[1])

                    # flip the X's or O's if not at the end point
                    # to "letter" to the right of start point
                    if count < endPoint:
                        while count <= endPoint:
                            board[int(inputList[0])][count] = letter
                            count += 1    
                        wins += 1

                    # flip the X's or O's if not at the end point
                    # to "letter" to the left of start point
                    elif endPoint < count:
                        while endPoint <= count:
                            board[int(inputList[0])][endPoint] = letter
                            endPoint += 1
                        wins += 1

                # get end point for going through a column
                elif inputList[1] == validMovesString[COLUMN_POS]:
                    count = int(startPoint[1])
                    endPoint = int(inputList[0])

                     # flip the X's or O's if not at the end point
                     # to "letter" upwards from the start point
                    if count < endPoint:
                        while count <= endPoint:
                            board[count][int(inputList[1])] = letter
                            count += 1
                        wins += 1

                    # flip the X's or O's if not at the end point
                    # to "letter" downwards from the start point
                    elif endPoint < count:
                        while endPoint <= count:
                            board[endPoint][int(inputList[1])] = letter
                            endPoint += 1
                        wins += 1

    return wins

######################################################################
# processPlayerInput() processes the player input
# Parameters:          board; a 2D list of single-char strings
#                      userInput; a string with the player input
# Output:              win; an integer used to keep track of number
#                            of wins
def processPlayerInput(userInput, board):

    validMoves = []
    win = 0
    isCompleteAi = isGameComplete(board, O_CHAR, X_CHAR)
    isCompletePlayer = isGameComplete(board, X_CHAR, O_CHAR)
    
    if isCompleteAi == False or isCompletePlayer == False:
        validMoves = getValidMoves(board, X_CHAR, O_CHAR)
        win = processInput(userInput, validMoves, board, X_CHAR)

    return win

######################################################################
# processAiInput()  processes the AI input    
# Parameters:       board; a 2D list of single-char strings
# Output:           win; an integer used to keep track of number
#                        of wins
def processAiInput(board):

    win = 0
    minRow = minColumn = ROW
    validMoves = []
    isCompleteAi = isGameComplete(board, O_CHAR, X_CHAR)
    isCompletePlayer = isGameComplete(board, X_CHAR, O_CHAR)

    
    if isCompleteAi == False or isCompletePlayer == False:
        validMoves = getValidMoves(board, O_CHAR, X_CHAR)

        for i in range(len(validMoves)):
            validMoveString = validMoves[i][1]

            if minRow > int(validMoveString[ROW_POS]):
                minRow = int(validMoveString[ROW_POS])
                minColumn = int(validMoveString[COLUMN_POS])
                minMove = validMoveString

            elif minRow == int(validMoveString[ROW_POS]):
                if minColumn > int(validMoveString[COLUMN_POS]):
                    minColumn = int(validMoveString[COLUMN_POS])
                    minMove = validMoveString

        aiInput = minMove[ROW_POS] + " " + minMove[COLUMN_POS]
        print("CPU takes move: [" + minMove[ROW_POS] + ", " + minMove[COLUMN_POS] + "]")
        win = processInput(aiInput, validMoves, board, O_CHAR)
        printBoard(board)

    return win

######################################################################
# isGameComplete()  checks if there are no more moves to play
# Parameters:       board; a 2D list of single-char strings
#                   player; a single char string of current player
#                   enemy; a single char string of opposing player
# Output:           isOver; a boolean stating if there are any valid
#                           moves available or not
def isGameComplete(board, player, enemy):
    validMoves = []
    isOver = False
    validMoves = getValidMoves(board, player, enemy)
    
    if len(validMoves) < 1:
        isOver = True
                
    return isOver

######################################################################
# sortValidMoves() puts valid moves into a list with each valid move
#                  getting added to the list only once
# Parameters:      validMoves; a string with the valid moves
# Output:          sortedValidMoves; a string with the valid moves
def sortValidMoves(validMoves):
    sortedValidMoves = []
    
    for i in range(len(validMoves)):
        if validMoves[i][1] not in sortedValidMoves:
            sortedValidMoves.append(validMoves[i][1])
            
    return sortedValidMoves

######################################################################
# printFinalMessage() prints out the final message when game is over
# Parameters:         gameBoard; a 2D list of single-char strings
#                     playerScore; an int with the final score of
#                                  the player
#                     aiScore; an int with the final score of the AI
# Output:             none
def printFinalMessage(gameBoard, playerScore, aiScore):
    print("GAME OVER")
    printBoard(gameBoard)
    print("Player score: " + str(playerScore))
    print("CPU score: " + str(aiScore))
    if playerScore > aiScore:
        print("Player wins!")
    elif aiScore > playerScore:
        print("CPU wins!")
    else:
        print("It's a draw!")

def main():

    # declare variables
    validMoves = []
    sortedValidMoves = []
    isComplete = False
    noMoreMovesPlayer = False
    noMoreMovesAi = False
    playerScore = 0
    aiScore = 0

    # print initial board
    gameBoard = startGame(ROW, COLUMN)
    
    while isComplete == False:
        i = 0
        validMovesString = ""
        isValid = False
        validMoves = getValidMoves(gameBoard, X_CHAR, O_CHAR)
        sortedValidMoves = sortValidMoves(validMoves)
        
        # add valid moves list to a string
        while i < len(sortedValidMoves):
            if i < len(sortedValidMoves) - 1:
                validMovesString = validMovesString + sortedValidMoves[i] + ", "
            else:
                validMovesString = validMovesString + sortedValidMoves[i]
            i = i + 1

        # print out the valid moves to the user    
        print("Valid moves are: [" + validMovesString + "]")


        # get user input and check if it is valid
        userInput = getUserInput()
        isValid = inputIsValidated(userInput, validMoves)

        # repeat getting user input till valid input is entered
        while isValid == False:
            print("Invalid move. ", end="")
            print("Valid moves are: [" + validMovesString + "]")
            userInput = getUserInput()
            isValid = inputIsValidated(userInput, validMoves)

        # check if there are no more valid moves for player and AI
        noMoreMovesPlayer = isGameComplete(gameBoard, X_CHAR, O_CHAR)
        noMoreMovesAi = isGameComplete(gameBoard, O_CHAR, X_CHAR)

    
        if noMoreMovesPlayer == True or noMoreMovesAi == True:
            isComplete = True
        else:
            playerScore += processPlayerInput(userInput, gameBoard)

        # check if there are no more valid moves for player and AI
        noMoreMovesPlayer = isGameComplete(gameBoard, X_CHAR, O_CHAR)
        noMoreMovesAi = isGameComplete(gameBoard, O_CHAR, X_CHAR)
        if noMoreMovesPlayer == True or noMoreMovesAi == True:
            isComplete = True
        else:
            aiScore += processAiInput(gameBoard)


    # print final game over message
    printFinalMessage(gameBoard, playerScore, aiScore)

main()
