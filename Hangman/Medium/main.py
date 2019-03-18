
from random import randint

def print_welcome_message():
    """
    Waits for the player to input his name, then
    prints welcome message for him
    """
    pass

def get_random_word():   
    """
    Opens file with words, gets one of the words at random and returns it.
    Also removes any possible whitespaces from the choosen word.
    """ 
    pass

def make_display_string(selected_word):
    """
    Makes and returns the string which is displayed in the terminal, it's used at the beggining of the program.
    
    Example: If the chosen word is 'plane' display string will be '_____' - this 
    is '_' written 5 times. 
    """
    pass

def update_display_string(display_string, selected_word, guessed_letter):
    """
    Updates the display_string based on the selected_word and guessed_letter.
    It just removes all '_' and puts the guessed_letter in it's place

    Example: If we had a word 'aeroplane' and first letter we guessed was 'a'
    display string would be:

    _________ - before the insertion
    a_____a__ - after the insertion

    """
    pass
    
def draw_screen(display_string, number_of_lives):
    """
    Displays the number of lives which player has left(number_of_lives) and 
    displays guessed words so far (display_string)
    
    Example: If we had a word 'aeroplane' and guessed letters so far 
    were 'a'  and 'e' and we have 2 lives left printed info would be:

    'Lives left: 2'
    'a e _ _ _ _ a _ e'
    
    """
    pass

def player_guessed(selected_word, guessed_letter):
    """
    Checks if the guessed_letter is in the selected word.

    If it is that means that player has guessed the word.
    """
    pass

def check_win(display_string):
    """
    Checks win condition for player.
    We know that our game endeed when there are not more unguessed letters left
    in our word(display_string).
    
    So we are just checking if there are any '_' left.
    If there aren't - player won the game
    """
    pass

def read_letter():
    """
    Reads the letter players has input. 
    Also checks if the input is valid English letter.
    """
    pass

def main():
    #? Main function should initialize all of the components that are 
    #? needed for the program to work
    
    #? It should start a game loop.

    #? It should display if the user has won or not, and it should the display the correct
    #? word if the user has lost.
    pass

if __name__ == "__main__":
    main()