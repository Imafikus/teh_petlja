import os   

C_ROWS = 3
C_COLS = 3
EMPTY_SYMBOL = ' - '
DIR_PATH = "results"
FILE_EXTENSION = ".txt"

#? Used to map 2D coordinates to 1D array we use for board representation
BOARD_FIELDS = {
    (0, 0) : 0,
    (0, 1) : 1,
    (0, 2) : 2,
    
    (1, 0) : 3,
    (1, 1) : 4,
    (1, 2) : 5,
    
    (2, 0) : 6,
    (2, 1) : 7,
    (2, 2) : 8
}

def display_welcome_message():
    """
    Displays welcome message for the players.
    """
    pass
def get_player_names():
    """
    Gets and returns player names as a tuple.
    First element in the tuple is the name of the first player.
    Second element in the tuple is the name of the second player.
    """
    pass

def construct_board():
    """
    Creates empty tick-tack-toe board

    It returns it as a matrix of strings.
    """
    pass

def create_signs(first_player, second_player):
    """
    Creates and returns dictionary which contains signs which players are using,
    it can be modifed to take custom signs.
    """
    pass 
    
def print_board(board):
    """
    Prints the current board.
    """
    pass 

def make_input(board, player, player_sign):
    """
    Asks the player for input, check if the input is correct and update the board if it is.

    Returns the col and row players has input
    """
    pass

def tie(board):
    """
    Checks if the result is tied. This function is always called after
    win checking, so that we for sure know that there are no more fields to be filled
    and that no one has won
    """
    pass

def check_win(board, sign):
    """
    Checks if the player who had last input has won, returns true or false
    """
    pass

def create_file_path(first_player, second_player):
    """
    Creates appropriate file path as stated in the specification
    
    File path is: first_player + second_player + FILE_EXTENSION 
    
    Returns that file as a string.
    """
    pass

def record_result(first_player, second_player, winner):
    """
    Records the result for the current game. Tries to write into the 
    file which is named first_player_second_player and which is stored in
    the directory results. 
    
    If the file with the same name (or with the inverted name) exists, it writes into 
    that file, otherwise makes a new file. 
    
    File name is all lower case.
    """
    pass

def display_current_stats(first_player, second_player):
    """
    Opens the file for the players, and reads displays the game data following format:

    - Number of wins for the first player, win percentage of the first player
    - Number of wins for the second player, win percentage of the second player
    - Number of tied games, tie games percentage
    """
    pass

def ask_for_another_game():
    """
    Asks the players if they want to play another game.
    
    Returns true if they want, false otherwise
    """
    pass

def main():    
    
    #? Initialization part here
    #? You need to display welcome message
    #? You need to ask players to enter their names
    #? You need to save those names for future use
    #? You need to construct empty 3x3 tick-tack-toe board

    #? Game loop and logic here. Loop must go on until it's a tie or one of the players has won
        
        #? Check if it's a tie
        
        #? Ask first player to choose a field 
        #? Check if the player has won

        #? Ask second player to choose a field 
        #? Check if the player has won
    
    #? When the game is finished, result is saved in /results folder
    #? IMPORTANT: Every pair of players must have its own .txt files (order of the players is relevant), player names are not case sensitive
    #? If the .txt file already exist, it must be updated with the new results
    #? Data in the file is in the following order:
        #? - Number of wins for the first player
        #? - Number of wins for the second player
        #? - Number of tied games

    #? Appropriate message is displayed after the game has finished (based on who won, or if it was a tie)
    #? After that all games statistics are shown in the following format:
        #? - Number of wins for the first player, win percentage of the first player
        #? - Number of wins for the second player, win percentage of the second player
        #? - Number of tied games, tie games percentage
        #? eg. if there was 4 games and first player won 2, second won 1, and the 1 was tied the the output would be
            #? first_player_name wins: 2, 50% of all games
            #? second_player_name wins: 1, 25% of all games
            #? Number of tied games: 1, 25% of all games
        #? After this there is an additional message which asks the players if they want to play another game or they want to quit
        #? If they want to play another game, everything except welcome message is repeated
        #? If they want to exit, program displays goodbye message and finishes
        
if __name__ == "__main__":
    main()