# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    
    # line: string
    line = inFile.readline()
    
    # wordlist: list of strings
    wordlist = line.split()
    
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)



def isWordGuessed(secretWord, guessedWord, lettersGuessed):

    if secretWord == guessedWord:
      return True
    else:
      print(getGuessedWord(secretWord, lettersGuessed))
      return False

  
def isLetterGuessed(secretWord, lettersGuessed):
  stringGuessed = getGuessedWord(secretWord, lettersGuessed)
  
  print(stringGuessed)
  if not '-' in stringGuessed:
    print('You Win!')
    return True
  
  else: return False


def getGuessedWord(secretWord, lettersGuessed):

  stringGuessed = '-' * len(secretWord)
  
  for letter in lettersGuessed:
      if letter in secretWord:
          count = secretWord.count(letter)
          
          if count > 1:
              result = [i for i, char in enumerate(secretWord) if char == letter]
              for i in result:
                  stringGuessed = stringGuessed[:i] + letter + stringGuessed[i + 1:]

          else:
              j = secretWord.find(letter)
              stringGuessed = stringGuessed[:j] + letter + stringGuessed[j+1:]
              
  return stringGuessed
    

def getAvailableLetters(lettersGuessed):
    
    alphabet_list = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        alphabet_list.remove(letter)
    
    return ''.join(alphabet_list)
    

def check_input():
  ifWord = False
  
  while True:
  
    try:
      valid_input = (input("Please enter a letter or a word: ")).lower()
      assert (valid_input.isalpha())
      
    except (AssertionError, ValueError):
      print("Sorry, I didn't understand the input.")
      
    else:
        if len(valid_input) > 1:
          ifWord = True

        return (valid_input, ifWord)
    

def hangman(secretWord):
    
    letter_count = 0
    word_count = 0
    lettersGuessed = []
    

    print("Let's Play Hangman")
    print("secret word: " + '-' * len(secretWord))
    
    
    while True:
      
      if letter_count > 8 or word_count > 1:
        break
      
      else:
        (valid_input, word) = check_input()
        
        if word:
          word_count += 1
          
          if isWordGuessed(secretWord, valid_input, lettersGuessed):
            print('You Win!')
            break
               
    
        elif not word:
          letter_count += 1
          lettersGuessed.append(valid_input)
          print(lettersGuessed)
          
          if isLetterGuessed(secretWord, lettersGuessed):
            break
          
          else:
            continue
        
        elif letter_count > 8 or word_count > 0:
          print("You've run out of guesses")
  
    print(f'Game Over. The secret word is {secretWord}')
      



wordlist = loadWords()
secretWord = chooseWord(wordlist)
 
hangman(secretWord)
