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