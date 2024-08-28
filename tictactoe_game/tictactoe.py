import random
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
drawBoard([' ', 'O', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '])

def inputPlayerLetter():
    """# Lets the player enter which letter they want to be. Returns a list with the player's letter as the first item and the computer's letter as the second."""
    letter = ''
    while not (letter == 'O' or letter == 'X'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # The first element in the list is the player's letter; the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    return ['O', 'X']
def whoGoesFirst():
    # randomly choose who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    return 'player'
def makeMove(board, letter, move):
    board[move] = letter
    print('This is the board')
    return drawBoard(board)
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(makeMove(board, 'O', 1))

def isWinner(bo, le):
    """
        Given a board and a player's letter, this function returns True if that player has won.
        We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
    """
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
board = [' ', 'X', ' ', 'O', ' ', 'X', ' ', 'O', ' ', 'X'] # 1, 7, 9
print(isWinner(board, 'X'))
board = [' ', 'X', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'X'] # 3, 5, 7
print(isWinner(board, 'O'))
board = [' ', 'X', 'X', 'X', 'O', ' ', ' ', 'O', ' ', 'X'] # 1, 2, 3
print(isWinner(board, 'X'))
board = [' ', 'X', ' ', 'O', 'O', 'O', 'O', 'X', ' ', 'X'] # 4, 5, 6
print(isWinner(board, 'O'))
board = [' ', 'X', ' ', 'O', ' ', 'X', ' ', 'X', 'X ', 'X'] # 7, 8, 9
print(isWinner(board, 'X'))
board = [' ', 'X', ' ', 'O', 'X', 'O', ' ', 'X', ' ', 'X'] # 1, 4, 7
print(isWinner(board, 'X'))
board = [' ', 'X', 'O', 'X', ' ', 'O', ' ', 'O', 'O', 'X'] # 2, 5, 8
print(isWinner(board, 'O'))
board = [' ', 'X', ' ', 'X', ' ', 'O', 'X', 'O', ' ', 'X'] # 3, 6, 9
print(isWinner(board, 'X'))
