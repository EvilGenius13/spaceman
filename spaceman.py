import random


##                                          READY TO GO
def load_word():
   
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word

    """
    Opens and reads external text file holding words.
    words are then split apart.
    a new variable named secret_word takes a randomized word from the list

    parameters: none

    returns : secret_word
    """
##                                          READY TO GO
def is_word_guessed(secret_word, letters_guessed):
   
  for character in secret_word:

        if character not in letters_guessed:
            return False
        
        else: 
            return True

def get_guessed_word(secret_word, letters_guessed):
    guess=''
    
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guess += secret_word[i]
        else: 
            guess += '_'
    return guess
   
##                                          READY TO GO
def is_guess_in_word(guess, secret_word):
    
    if guess in secret_word:
        #print('Yay! You guessed right! Keep going.')
        return True
    else:
        #print("Aww, that guess wasn't part of the word. Try again!")
        return False 
    """
    Checks if a letter guessed is in the secret word
    ex: is the letter a in the secret word apple (yes)

    paramaters:
    guess : the letter input by user
    secret_word : the secret word

    returns: 
    true or false based on if letter is in secret word or not

    
    """

def spaceman(secret_word):
  
    guesses = 7
    letters_guessed = ['']

    print('WHOOOOOOOOOOOOOOOSSSSSHHHHHHHHH')
    print("Welcome to Spaceman. It's time to fly, or crash...")
    print("Your goal is to guess the secret word letter by letter. (Think knockoff wheel of fortune)")
    print("You have 7 guesses. Let's go to space!")

    game_state = True

    while guesses != 0:
        userPrompt = input('Okay Cadet, take a guess: ')
        is_guess_in_word(userPrompt, secret_word)
        letters_guessed.append(userPrompt)
        get_guessed_word(secret_word, letters_guessed)
        guesses -= 1
    if is_word_guessed():
        print('BLAST OFF!!!! CADET, YOU ARE PROMOTED!')
    else:
        print('Sorry Cadet, better luck next time.')









#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
