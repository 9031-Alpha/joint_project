# Assignment 2, hangman.py
# Group No/Name: 07 ( Alpha)
# Members: Igbasanmi Olusegun, Mohamed Omer Airaj, Mohamed Fahmy

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
    count=0
    for char in secret_word:
        if char in letters_guessed:
            count+=1
    if count == len(secret_word):
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE
    final_display = list('_' * len(secret_word))
    for i,char in enumerate(secret_word):
        if char in letters_guessed:
            final_display[i] = char
    return " ".join(final_display)
            

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE
    all_letters= string.ascii_lowercase
    available_letters=[]
    for char in all_letters:
        if char not in letters_guessed:
           available_letters.append(char)
    return "".join(available_letters)
    
# end of part 1
    
    
def word_point(secret_word):    # this function would calculate the point for each word
    unique=[]
    for char in secret_word:
        if char not in unique:
            unique.append(char)
    return len(unique)

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
    letters_guessed=[]
    n=6             # number of guesses
    warning = 3     # initialising warning count
    count = 0       # initialising the number of correct guesses
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print(' _ ' * len(secret_word))
    print("You have " + str(warning) + " warnings left")
    print("You have " +str(n) + " guesses left.")
    print("Available letters: ", get_available_letters(letters_guessed))
    vowels=['a','e','i','o','u']  #initialising the vowels
    
    while n > 0 and not is_word_guessed(secret_word, letters_guessed):
        guess = input("Please guess a letter: ").lower()   # takes user input and makes it a lowercase always
        if str.isalpha(guess):                             #checks if user input is an alphabet and only then does the game continue
            if guess in secret_word and guess not in letters_guessed:
                letters_guessed.append(guess)                  # keeps memory of user guesses by adding to a list
                print("Good guess: ",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                print("You have " +str(n) + " guesses left.")
                print("Available letters: ", get_available_letters(letters_guessed))
                count += 1                      # updating the number of correct guesses
            elif guess in letters_guessed:      # if guess is has been previously guessed
                warning -= 1
                if warning >= 0:
                    print("Oops! You have already guessed that letter. You now have " + str(warning) + " warnings left: ",get_guessed_word(secret_word,letters_guessed))
                    print("-------------")
                    print("You have " +str(n) + " guesses left.")
                    print("Available letters: ", get_available_letters(letters_guessed))
                else:
                    print("Oops! You have already guessed that letter. You now have no warnings left")
                    print("so you lose one guess: ",get_guessed_word(secret_word,letters_guessed))
                    n -=1
                    print("-------------")
                    print("You have " +str(n) + " guesses left.")
                    print("Available letters: ", get_available_letters(letters_guessed))
                    warning = 3
            elif guess not in secret_word and guess in vowels:
                letters_guessed.append(guess)                  # keeps memory of user guesses by adding to a list
                n -= 2
                print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                print("You have " +str(n) + " guesses left.")
                print("Available letters: ", get_available_letters(letters_guessed))
            else:
                letters_guessed.append(guess)                  # keeps memory of user guesses by adding to a list
                n -= 1
                print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                print("You have " +str(n) + " guesses left.")
                print("Available letters: ", get_available_letters(letters_guessed))
        else:
            warning -= 1
            if warning >= 0:
                print("Oops! That is not a valid letter. You have " + str(warning) + " warnings left: ",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                print("You have " +str(n) + " guesses left.")
                print("Available letters: ", get_available_letters(letters_guessed))
            else:    # To notify user when they lose a guess after exceeding allowed warnings
                print("Oops! That is not a valid letter. You have no warnings left")
                print("so you lose one guess: ",get_guessed_word(secret_word,letters_guessed))
                n -=1
                print("-------------")
                print("You have " +str(n) + " guesses left.")
                print("Available letters: ", get_available_letters(letters_guessed))
                warning = 3
                
    if is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("Congratulations, You won!")
        print("Your total score for this game:",word_point(secret_word)*n)
    else:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was",secret_word)

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
    count =0
    my_word = my_word.replace(' ','')       # replace function removes all space in my word to ensure proper comparison
    if len(my_word) == len(other_word):     # first screening crieteria is to check if words have same length
        for i, char in enumerate(my_word):  # if it passes first screening, then it compares element by element
            if (char == other_word[i]) or (char == '_' and other_word[i] not in my_word) : # two conditions satisfied for comparison
                count += 1
    if count == len(other_word):
        return True
    else:
        return False


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
    matches =[]
    for other_word in wordlist:             # looks through the wordlist for possible matches
        if match_with_gaps(my_word,other_word):     # calls the function match_wit_gaps to execute the comparison
            matches.append(other_word)              # if it matches, it stores for future display
    if matches == []:                               # if no match prints no match found
        print("No matches found")
    else:
        return ' '.join(matches)                    # prints all the possible matches


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
