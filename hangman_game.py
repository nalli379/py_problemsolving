# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def isWordGuessed(secretWord, guessedWord):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guess = False
    if secretWord == guessedWord:
      guess = True
      return guess

    
  
def isLetterGuessed(secretWord, guessedLetter, lettersGuessed):
  if not guessedLetter in secretWord:
      print('at isletter guessed function not found match')
      return False
  else:
        print('at isletter guessed function found match')  
        return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

def check_input():
  try:
    valid_input = (input("Please enter a letter or a word: ")).lower()
  except ValueError:
    print("Sorry, I didn't understand the input.")
  
  else:
    if valid_input.isalpha():
      if len(valid_input) > 1:
        return (valid_input, True)
      
      else:
        return (valid_input, False)
    
  

wordlist = loadWords()
secretWord = chooseWord(wordlist)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter/word) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    letter_count = 0
    word_count = 0
    lettersGuessed = []
    print("Let's Play Hangman")
    print(f"secret word: {secretWord}")
    
    while True:
      
      if letter_count > 8 or word_count > 1:
        break
      
      else:
        (valid_input, word) = check_input()
        print(valid_input, word)
        
        if word:
          word_count += 1
          print(f"word count {word_count}")
          
          #go to function to check word
          if isWordGuessed(secretWord, valid_input):
            #return here a value to end the game?
            print('You Win')
            break
               
    
        elif not word:
          letter_count += 1
          print(f"letter count {letter_count}")
          #go to function to check letter count
          if isLetterGuessed(secretWord, valid_input, lettersGuessed):
            print('letter match')
            break
          
        
        elif letter_count > 8 or word_count > 0:
          print('broke')
  
    print('game over')
      
  
hangman(secretWord)
    
    
    #repeat for count of 8 letter guesses/1 word guess
    #keep a count of number of tries - starting at 0, up to 8.
    #keep a count of input word - starting at 0, up to 1
    
    #ask the user for input letter or input word
    
    #check input letter is in the guessed word 
    
    #show guessed word so far...
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
