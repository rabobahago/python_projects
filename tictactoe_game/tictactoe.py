import random
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
# drawBoard([' ', 'O', ' ', 'X', ' ', 'O', ' ', ' ', ' ', 'X'])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O? ').upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
# print(inputPlayerLetter())

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    return 'player'

def makeMove(board, letter, move):
    board[move] = letter
    print(drawBoard(board))
    return board
player, computer = inputPlayerLetter()
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
result = makeMove(board, player, 1)
print(makeMove(board, player, 1))

def isWinner(bo,le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le))
print(isWinner(result, player))