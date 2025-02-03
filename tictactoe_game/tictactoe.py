import random
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    return board
# drawBoard([' ', 'O', ' ', 'X', ' ', 'O', ' ', ' ', ' ', 'X'])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
print(inputPlayerLetter())

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo,le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le))

def getBoardCopy(board):
    boardCopy = []
    for move in board:
        boardCopy.append(move)
    return boardCopy
def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    while True:
        print('What is your next move? (1-9)')
        move = input().strip()
        if not move.isdigit():
            print('Invalid input, please enter a number between 1-9')
            continue
        move = int(move)
        if move < 1 or move > 9:
            print('Please, enter number between 1-9')
        elif not isSpaceFree(board, move):
            print('That space is already occupied. Choose another.')
        else:
            return move
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for move in movesList:
        if isSpaceFree(board, move):
            possibleMoves.append(move)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    return None
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic-Tac-Toe!')
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:

        if turn == 'player':
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer’s turn

            if turn == 'computer':

                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break