# Assignment 2, hangman.py
# Group No/Name: 
# Members:

# Hangman Game
# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



# -------------------------------------
# Hangman Part 1: Three helper functions

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            boo = True
        else:
            boo = False
            break
    return boo



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE
    guessed_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            guessed_word = guessed_word + '_ '
        else:
            guessed_word = guessed_word + secret_word[i]
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE
    available_letters = ''
    for i in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[i] not in letters_guessed:
            available_letters = available_letters + string.ascii_lowercase[i]
    return available_letters
   
    
# end of part 1
    
    
    
    
# -------------------------------------
# Hangman Part 2: The Game

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("You have 3 warnings left.")
    print ("-----------------")
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    guessed = False
    warnings_left = 3
    guesses_left = 6
    vowels = 'aeiou'
    while (guessed != True and guesses_left > 0):
        print ("You have " + str(guesses_left) + " guesses left.")
        print ("Available letters: " + available_letters)
        letter = input("Please guess a letter: ")
        letter = letter.lower()
        if letter not in string.ascii_lowercase and warnings_left != 0:
            warnings_left -= 1
            print ("Oops! That is not a valid letter. You have " + str(warnings_left) + " warnings left: " + guessed_word)
        elif letter not in string.ascii_lowercase and warnings_left == 0:
            guesses_left -= 1
            print ("Oops! That is not a valid letter. You have no warnings left so you lose one guess: " + guessed_word)
        elif letter not in available_letters and warnings_left != 0:
            warnings_left -= 1
            print ("Oops! You've already guessed that letter. You have " + str(warnings_left) + " warnings left: " + guessed_word)
        elif letter not in available_letters and warnings_left == 0:
            guesses_left -= 1
            print ("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + guessed_word)
        elif letter not in secret_word and letter in vowels:
            guesses_left -= 2
            print("Oops! That letter is not in my word: " + guessed_word)
            letters_guessed.insert(0,letter)
            available_letters = get_available_letters(letters_guessed)
        elif letter not in secret_word and letter not in vowels:
            guesses_left -= 1
            print("Oops! That letter is not in my word: " + guessed_word)
            letters_guessed.insert(0,letter)
            available_letters = get_available_letters(letters_guessed)
        elif letter in secret_word:
            letters_guessed.insert(0,letter)
            available_letters = get_available_letters(letters_guessed)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print ("Good guess: " + guessed_word)
        guessed = is_word_guessed(secret_word, letters_guessed)
        print ("-----------------")
    
    if guessed == True:
        result = ''
        for s in string.ascii_letters:
            if secret_word.count(s) >= 1:
                result+=s
        number_of_unique_letters = len(result)
        score = guesses_left * number_of_unique_letters
        print ("Congratulations, you won!")
        print ("Your total score for this game is: " + str(score))
    else:
        print ("Sorry, you ran out of guesses. The word was " + secret_word)
            
                
            
        



# -----------------------------------
# end of part 2
    
    
    
# -------------------------------------
# Hangman Part 3: The Game with Hints


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE


# -----------------------------------
# end of part 3

# Main code 

# To test part 2
# uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)


    
# To test part 3 re-comment out the above lines and 
# uncomment the following two lines. 
    
#secret_word = choose_word(wordlist)
#hangman_with_hints(secret_word)
