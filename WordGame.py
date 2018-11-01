import random
import string
import math
import copy

WORDLIST_FILENAME = "words.txt"
vowels = ['a','e','i','o','u']
def load_words():
    """
    Returns a list of words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME) as f:
        wordlist = f.read().lower().splitlines()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

words = load_words()

def get_word_score(word, n):
    """
    word (string): Word that is played using the current hand.
    n (int): Number of letters available in the current hand. It can be 
             integer value from 1 to 10.
    """
    word_length = len(word)
    SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                              'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                              'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
                              's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                              'y': 4, 'z': 10, '*':0}
    score = 0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    second = 7*word_length-3*(n-word_length)
    if second < 1:
        return score
    else:
        return score * second


def get_frequency_dict(string_of_letters): 
    myDict = {} 
    for letter in string_of_letters: 
        if letter in myDict:
            myDict[letter] += 1
        else:
            myDict[letter] = 1 
    return myDict


def display_hand(hand):
    displayed = ''
    for i in hand.keys():
        displayed += i*hand[i]
    return (' '.join(displayed))


def deal_hand(n):
    v = math.ceil(n/3)          
    vowels = ['a','e','i','o','u']
    generate_hand = '*'            # including the wild card
    for i in range(v-1):
        generate_hand += random.choice(vowels)
    for i in range(n-v):
        letter = 'a'
        while (letter in vowels):           #ensure the next random numbers are consonants
            letter = random.choice(list(string.ascii_lowercase))    
        generate_hand += letter
    return get_frequency_dict(generate_hand)


def update_hand(hand, spelled_word):
    current_hand = copy.deepcopy(hand)   # clone dictionary 
    for i in spelled_word:
        if i not in hand:           # if word contains letters not in hand, skip to the next letter
            continue
        elif current_hand[i] == 1:        # delete elements one after the other
            del(current_hand[i])
        elif current_hand[i] > 1:
            current_hand[i] -= 1
    return current_hand


def is_valid_word(word):
    ''' word(string): word that is played using the current hand. It takes into account the possibility of a wildcard
        If a wildcard is found, it replaces it with different vowels and checks if it forms a valid word '''
        
    count = 0
    if '*' in word:     # Check if word played has a wild card in it
        i=word.find('*')
        while count < len(vowels):  # replace wild card with vowels and check if word exist, if it does break out of loop (why while instead of for) 
            check=list(word)
            check[i]=vowels[count]
            count +=1
            check=''.join(check)
            if check in words:
                break
        return check in words
    else:
        return word in words  
   

def substitute_hand(current_hand):
    ''' current hand(dictionary) of the cards the user currently has. This code substitues the letter the user prompts 
        with a new random letter that is not neither in his hand nor the letter is is trying to exchange '''
        
    letter= input('Which letter would you like to replace: ')
    if letter in current_hand:
        number = current_hand[letter]
        del(current_hand[letter])
        while number > 0:
           add = random.choice(string.ascii_lowercase) 
           if add not in current_hand and add != letter:
               current_hand[add] = 1
               number -=1
        return current_hand
    else:
        return current_hand

        
def play_hand():
    total_score = 0
    n=7
    current_hand =  deal_hand(n)
    print('Current Hand: ',display_hand(current_hand))
    sub_no = 0                      # number of times substitution has been done in a game
    while len(current_hand)>0:
        response = input('Would you like to substitute a letter? ')
        if response == 'yes':
            sub_no += 1
            current_hand = substitute_hand(current_hand)
            print('')
            print('Current Hand: ',display_hand(current_hand))
        elif response == 'no':
            print('')
            print('Current Hand: ',display_hand(current_hand))
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        if is_valid_word(word):
            total_score += get_word_score(word,n)
            print(word +' earned '+str(get_word_score(word,n)) + ' points. Total '+str(total_score)+' points')
            print('')
            current_hand = update_hand(current_hand,word)
            print('Current Hand: ',display_hand(current_hand))
        elif not is_valid_word(word) and (word !='!!'):
            print('This is not a valid word. Please choose another word')
            current_hand = update_hand(current_hand,word)                   
            print('Current Hand: ',display_hand(current_hand))
        elif word == '!!':
            print('Total score: ',total_score )
            break
        n=len(current_hand)
    if len(current_hand) == 0:
        print('Ran out of letters. Total score: ',total_score)
    return total_score   
            

def play_game():
    overall_score = 0
    series_N = int(input('Enter total number of hands: '))
    for i in range(series_N):
        score1 = play_hand()
        response2 = input('Would you like to replay the hand? ')
        if response2 == 'yes':
            score2 = play_hand()
            score = max([score1,score2])
        else:
            score = score1
        overall_score += score
    
    print('----------------')
    print("Total score over all hands: ",overall_score)














    
