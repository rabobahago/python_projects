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
print(inputPlayerLetter())
