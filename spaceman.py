import random

def ascii(times_wrong_answer):
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
              /   \
_____________/_ __ \_____________'''
]
    print(ascii_dynamite[times_wrong_answer])
    return

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
    is_letter_guessed = True
    
    while is_letter_guessed:
        for letter in secret_word:
            if letter in letters_guessed:
                is_letter_guessed = True
            else:
                return False
        return True

def get_guessed_word(secret_word, letters_guessed):
    guess_board= ''
    
    for letter in secret_word:
        if letter in letters_guessed:
            guess_board += letter
        else:
            guess_board += '_'

    return guess_board
   
##                                          READY TO GO
def is_guess_in_word(guess, secret_word):
    
    if guess in secret_word:
        print("Yes Cadet! Keep Going!")
        return True
    else:
        print("Oh no! Try again!")
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
def new_round():
    play_again = input("Did you want to play again? y/n: ")
    if play_again == 'y':
        secret_word = load_word()
        spaceman(secret_word)
        return False
    return False

def spaceman(secret_word):
  
    guesses_left = 7
    letters_guessed = ''
    times_wrong_answer = 0
   
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
    
    
    want_instructions = input("Do you want to learn how to play? y/n: ")
    if want_instructions == 'y':
        print("Your goal is to guess the secret word letter by letter. (Think knockoff wheel of fortune)")
        print("You have 7 guesses. Let's go to space!")
    else:
        print("Let's play!")
   

    while guesses_left != 0:
        print(f"You are down to {guesses_left} guesses.")
        game_state = True

        while game_state:

            guess = input('Okay Cadet, take a guess: ')
            if len(guess) >1:
                print("One letter at a time Cadet!")
            elif guess in letters_guessed:
                print('You already guessed that letter Cadet, pick again!')
            else:
                letters_guessed += guess
                game_state = False
                print(f"You've guessed {letters_guessed}")

        if not is_guess_in_word(guess, secret_word):
            guesses_left -= 1
            times_wrong_answer += 1
            ascii(times_wrong_answer)
        else:
            ascii(times_wrong_answer)

        print(get_guessed_word(secret_word, letters_guessed))

        if is_guess_in_word(secret_word, letters_guessed):
            print(f"Promoted Cadet!.. or should I say Corporal. Your word was {secret_word}")



    print(f"Time's up! The word was {secret_word}")
    new_round()



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)


