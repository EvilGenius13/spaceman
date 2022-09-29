import random

user_guess = ''
guesses = ''


##                                          READY TO GO
def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word
##                                          READY TO GO
def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            user_guess += secret_word[i]
    if secret_word == user_guess:
        return True
    else: 
        return False


def get_guessed_word(secret_word, letters_guessed):
    underscore = '_' * len(secret_word)
    
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    
   


##                                          READY TO GO
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    if guess in secret_word:
        print('Yay! You guessed right! Keep going.')
        return True
    else:
        print("Aww, that guess wasn't part of the word. Try again!")
        return False 


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    guesses = 0
    letters_guessed = ['']

    print('WHOOOOOOOOOOOOOOOSSSSSHHHHHHHHH')
    print("Welcome to Spaceman. It's time to fly, or crash...")
    print("Your goal is to guess the secret word letter by letter. (Think knockoff wheel of fortune)")
    print("You have 7 guesses. Let's go to space!")

    game_state = True

    while game_state:







#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
