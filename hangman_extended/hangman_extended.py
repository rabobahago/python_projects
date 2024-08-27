import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''',

      '''
    +---+
   [O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
   [O]  |
   /|\  |
   / \  |
       ===''']

words = {'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
         'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()
         }

def getRandomWord(wordDict):
    """This function returns a random string from the passed list of strings"""
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex], wordKey]
def displayBoard(missedLetters, correctLetters, secretWords):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    blanks = '_' * len(secretWords)
    for i, letter in enumerate(secretWords):
        if letter in correctLetters:
            blanks = blanks[:i] + secretWords[i] + blanks[i+1:]
    for char in blanks:
        print(char, end='')
    print()
def getGuess(alreadyGuessed):
    """Returns the letter the player entered. This function makes sure the
    player entered a single letter and not something else."""
    while True:
        print('Guess a letter')
        guess = input()
        guess =  guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Invalid character, Enter a letter')
        else:
            return guess
def playAgain():
    """This function returns True if the player wants to play again: otherwise, it returns False."""
    print('Do you want to play again? (yes or no)')
    return input('Do you want to play again? (yes or no)').lower().startswith('y')
print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input('Enter difficulty: E - Easy, M - Medium, H - Hard: ').upper()
    if difficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    if difficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False
while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters= True
        for i, val in enumerate(correctLetters):
            if val not in secretWord:
                foundAllWords = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
        # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
