
from random import randint

def print_welcome_message():
    """
    Waits for the player to input his name, then
    prints welcome message for him
    """

    print("Welcome to hangman game, please tell me you name")
    player_name = input()
    print("Hello " + player_name + " I hope that you'll have fun!")

def get_random_word():   
    """
    Opens file with words, gets one of the words at random and returns it.
    Also removes any possible whitespaces from the choosen word.
    """ 

    words_file = open("words.txt", "r")
    all_words = words_file.readlines()
    random_index = randint(0, len(all_words)-1)

    random_word = all_words[random_index].rstrip()
    random_word = random_word.lower()
    return random_word

def make_display_string(selected_word):
    """
    Makes and returns the string which is displayed in the terminal, it's used at the beggining of the program.
    
    Example: If the chosen word is 'plane' display string will be '_____' - this 
    is '_' written 5 times. 
    """

    display_string = []
    for char in selected_word:
        display_string.append("_")
    
    return display_string

def update_display_string(display_string, selected_word, guessed_letter):
    """
    Updates the display_string based on the selected_word and guessed_letter.
    It just removes all '_' and puts the guessed_letter in it's place

    Example: If we had a word 'aeroplane' and first letter we guessed was 'a'
    display string would be:

    _________ - before the insertion
    a_____a__ - after the insertion

    """

    for i, char in enumerate(selected_word):
        if char == guessed_letter:
            display_string[i] = guessed_letter

def draw_screen(display_string, number_of_lives):
    """
    Displays the number of lives which player has left(number_of_lives) and 
    displays guessed words so far (display_string)
    
    Example: If we had a word 'aeroplane' and guessed letters so far 
    were 'a'  and 'e' and we have 2 lives left printed info would be:

    'Lives left: 2'
    'a e _ _ _ _ a _ e'
    
    """

    print("Lives left: ", number_of_lives)

    #?We use pretty display just to have spaces between words 
    #?so we can see missing letters more clearly
    pretty_display = ""

    for char in display_string:
        pretty_display += char + " "
    
    print(pretty_display)

def player_guessed(selected_word, guessed_letter):
    """
    Checks if the guessed_letter is in the selected word.

    If it is that means that player has guessed the word.
    """

    if guessed_letter in selected_word:
        return True
    else:
        return False

def check_win(display_string):
    """
    Checks win condition for player.
    We know that our game endeed when there are not more unguessed letters left
    in our word(display_string).
    
    So we are just checking if there are any '_' left.
    If there aren't - player won the game
    """

    if "_" not in display_string:
        return True
    else:
        return False

def read_letter():
    """
    Reads the letter players has input. 
    Also checks if the input is valid English letter.
    """
    
    letter = None
    while letter == None:
        print("Please enter a letter")
        letter = input()
        if letter.isalpha() and len(letter) == 1:
            return letter.lower()
        else:
            letter = None
    

def main():
    
    #? Initialization part here.
    #? You have to set number of lives for the player
    #? You have to set indicator if the player has won
    #? You have to choose random word from the words.txt file
    #? You have to initialize display string 
    #? You have to print welcome message

    #? You main loop has to go until either player won or they have no more lives 
    #? Everything that has to do with the game has to be in that loop
        
        #? First thing you need to do before each attempt is to draw the screen
        #? Then you have to get the input from the player and to check if the player has guessed the word
        
        #? After that you have to update the number of lives or the display screen. It depends whether 
        #? player has guessed the whole word or not
        
    #? After the game loop has ended you have to display proper message depending on whether the player has won or not
    #? It would be nice if you could show the word that was chosen if the player lost.
    
    pass
if __name__ == "__main__":
    main()