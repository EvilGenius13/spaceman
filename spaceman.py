#imported isdigit for if statement later in game loop
from curses.ascii import isdigit
import random

##                                          READY TO GO
def ascii(times_wrong_answer):
    #list of ascii art - prints the ascii depending on how many times answer is wrong
    ascii_dynamite = ['''
___________________   
(________TNT_______|~~~~~~~X ''', '''
___________________   
(________TNT_______|~~~~~~X''', '''
___________________   
(________TNT_______|~~~~~X''', '''
___________________   
(________TNT_______|~~~X''', '''
___________________   
(________TNT_______|~~X''', '''
___________________   
(________TNT_______|~X''', '''
___________________   
(________TNT_______|X''', '''
          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \\
_____________/_ __ \_____________'''
]
    print(ascii_dynamite[times_wrong_answer])
    return

##                                          READY TO GO
def new_round():
    #new round request y to continue else break
    play_again = input("Did you want to play again? y/n: ")
    if play_again == 'y':
        secret_word = load_word()
        spaceman(secret_word)
        return False
    return False

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
    #function to find out if the secret word has been fully guessed
    #if all letters guessed returns final True, if not, returns False
    is_letter_guessed = True
       
    while is_letter_guessed:
        for letter in secret_word:
            if letter in letters_guessed:
                is_letter_guessed = True
            else:
                return False
        return True

def get_guessed_word(secret_word, letters_guessed):
    #if letter guessed is in secret word, add letter to guess_board. if not, place '_' in guess_board
    guess_board= ''
    
    for letter in secret_word:
        if letter in letters_guessed:
            guess_board += letter
        else:
            guess_board += '_'

    return guess_board
   
##                                          READY TO GO
def is_guess_in_word(guess, secret_word):
    #colours for guess being in secret word
    green = '\033[1;92m' 
    red = '\033[1;91m'
    #if guess is in secret word, return True and positive message
    #else return false and try again message
    if guess in secret_word:
        print(f"{green}Yes Cadet! Keep Going!")
        return True
    else:
        print(f"{red}Oh no! Try again!")
        return False 
    
    
    """
    Checks if a letter guessed is in the secret word
    ex: is the letter a in the secret word apple (yes)

    parameters:
    guess : the letter input by user
    secret_word : the secret word

    returns: 
    true or false based on if letter is in secret word or not

    
    """

##                                          READY TO GO
def spaceman(secret_word):
  #initialize guesses left, letters guessed, times wrong answer (ascii) and colours for terminal
    guesses_left = 7
    letters_guessed = ''
    times_wrong_answer = 0
    yellow = '\033[0;93m'
    blue = '\033[1;94m'   
    green = '\033[1;92m' 

   #initial start message
    print("        |")
    print('       / \ ')
    print('      / _ \ ')
    print("     |.o '.|")
    print("     |'._.'|")
    print("     |     |")
    print("   ,'|  |  |`.")
    print("   /  |  |  |  \ ")
    print("   |,-'--|--'-.|  ") 
    print('WHOOOOOOOOOOOOOOOSSSSSHHHHHHHHH')
    print("Welcome to Spaceman. It's time to launch, or explode...") 
    
    #ask if user wants instructions
    want_instructions = input("Do you want to learn how to play? y/n: ")
    if want_instructions == 'y':
        print("Your goal is to guess the secret word letter by letter. (Think knockoff wheel of fortune)")
        print("You have 7 guesses. Let's go to space!")
    else:
        print("Let's play!")
   
    #game loop while user guesses are not equal to 0.
    #tells you how many guesses are left and what letters have been guessed.
    while guesses_left != 0:
        print(f"{yellow}You are down to {guesses_left} guesses.")
        print(f"{green}You've guessed {letters_guessed}")
        game_state = True

        while game_state:
            #guess input - if guess length longer than 1 or guess isnumeric (a number)
            #or guess has already been entered, a response will be spit back to guess again.
            guess = input(f'{blue}Okay Cadet, take a guess: ')
            if len(guess) >1:
                print(f"{blue}One letter at a time Cadet!")
            elif guess.isnumeric() == True:
                print(f"{blue}You need to pick a letter Cadet")
            elif guess in letters_guessed:
                print(f'{blue}You already guessed that letter Cadet, pick again!')
            else:
                letters_guessed += guess
                game_state = False
                
        #if guess is not in secret word remove a guess remaining, increment times wrong answer by 1
        #which will change the ascii art. else will print current ascii art (as they have guessed correctly)
        if not is_guess_in_word(guess, secret_word):
            guesses_left -= 1
            times_wrong_answer += 1
            ascii(times_wrong_answer)
        else:
            ascii(times_wrong_answer)

        #prints current letters guessed and blank spaces
        print(get_guessed_word(secret_word, letters_guessed))

        #win statement - will then pass to new round after break
        if is_word_guessed(secret_word, letters_guessed):
            print(f"Promoted Cadet!.. or should I say Corporal. Your word was {secret_word}")
            break
            

    #losing message and offer up new round
    print(f"Time's up! The word was {secret_word}")
    new_round()



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)


