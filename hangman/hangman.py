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
     ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(listWord):
    """This function returns a random string from the passed list of strings"""
    wordIndex = random.randint(0, len(listWord)-1)
    return listWord[wordIndex]
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
    return input().lower().startswith('y')
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
while True:
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
            secretWord = getRandomWord(words)
        else:
            break
