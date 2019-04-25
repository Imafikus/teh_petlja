import numpy as np

C_ROWS = 3
C_COLS = 3
EMPTY_SYMBOL = ' - '

def display_welcome_message():
    """
    Displays welcome message for the players.
    """
    print("Welcome to the awesome tick-tack-toe game simulator, I hope you'll have fun!")

def get_player_names():
    """
    Gets and returns player names as a tuple.
    First element in the tuple is the name of the first player.
    Second element in the tuple is the name of the second player.
    """
    print("Please input the name of the first player")
    first_player = input()

    print("Please input the name of the second player")
    second_player = input()

    return tuple(first_player, second_player)

def construct_board():
    """
    Creates empty tick-tack-toe board

    It returns it as a matrix of strings.
    """
    #? numpy has .full() function which produces matrix of the given size
    #? EMPTY_SYMBOL is there to tell np to fill the whole matrix with that element
    #? dtype = "S10" just says that our matrix will store strings whose max length
    #? is <= 10, this is done because by default only stores strings of length = 1
    #? so whatever string we give that is longer, only first char of the string will be read
    board = np.full([C_ROWS, C_COLS], EMPTY_SYMBOL, dtype = "S10")

    return board

def create_signs()

def print_board(board):
    """
    Prints the current board.
    """
    print("print_board")

    i = 0
    j = 0

    while i < C_COLS:
        to_print = ""
        
        while j < C_ROWS:
            #? .decode() is used because np has it's own special string encoding
            #? while python string default is the utf-8 format, .decode() will cast from
            #? special encoding to the utf-8
            #? if we don't do that, we cannot add string to to_print
            to_print += board[i][j].decode("utf-8")
            j += 1
        
        print(to_print)
        i += 1
        j = 0

def make_input(board):
    """
    Asks the player for input, check if the input is correct and update the board if it is.
    """
    #? This is used because we know that we have a square matrix, and that only
    #? valid cols and rows are those below, so this is the easiest solution
    valid_fields = [0, 1, 2]

    valid_input = False
    while(not valid_input):
        column = int(input("Please input column: "))
        row = int(input("Please input row: "))

        if(row not in valid_fields or column not in valid_fields):
            print("You must enter a valid field, try again")
            continue
        
        else:
            if board[column][row].decode("utf-8") != EMPTY_SYMBOL:
                print("That field already has an input, try again")
                continue
        
        board[column][row] = ' ' + 'H' + ' '
        valid_input = True
        print_board(board)

def tie(board):
    """
    Checks if the result is tied. This function is always called after
    win checking, so that we for sure know that there are no more fields to be field
    and that no one has won
    """

    all_filled = True

    cols = 0
    rows = 0

    while cols < C_COLS:
        while rows < C_ROWS:
            if board[cols][rows].decode("utf-8") == EMPTY_SYMBOL: 
                all_filled = False
            rows += 1
        cols += 1
        rows = 0

    print("all_filled: ", all_filled)
    return all_filled

def main():

    display_welcome_message()
    first_player, second_player = get_player_names()
    board = construct_board()
    print_board(board)
    print("Izasao iz print")

    


    while not tie(board):
        print("usao u while")
        
        make_input(board, first_player, signs)
        print_board(board)
        check_win(board)

        make_input(board)    
        print_board(board)
        check_win(board)
        


    #? Initialization part here
    #? You need to display welcome message
    #? You need to ask players to enter their names
    #? You need to save those names for future use
    #? You need to construct empty 3x3 tick-tack-toe board

    #? Game loop and logic here. Loop must go on until it's a tie or one of the players has one
        
        #? Check if it's a tie
        
        #? Ask first player to choose a field 
        #? Check if the player has won

        #? Ask second player to choose a field 
        #? Check if the player has won
    
    #? When the game is finished, result is saved in /results folder
    #? IMPORTANT: Every pair of players must have his own .txt files (order of the players is irrelevant), player names are not case sensitive
    #? If the .txt file already exist, it must be updated with new results
    #? Example file you can use as pattern (but you don't have to) is example_saved_data.txt


    #? Appropriate message is displayed after the game has finished (based on who won (or if it was a tie))
    #? After 'enter' key is pressed current game statistics are show in the following format
        #? - Number of wins for the first player, win percentage of the first player
        #? - Number of wins for the second player, win percentage of the second player
        #? - Number of tied games, tie games percentage
        #? eg. if there was 4 games and first player won 2, second won 1, and the 1 was tied the the output would be
            #? first_player_name: 2 wins, 50% of all games
            #? second_player_name: 1 win, 25% of all games
            #? Number of tied games: 1, 25% of all games
            #? Keep in mind that your generated sentences must be grammatically correct
        #? After this there is an additional message which asks the players if they want to play another game or they want to quit
        #? If they want to play another game, everything except welcome message is repeated
        #? If they want to exit, program displays goodbye message and finishes
        


if __name__ == "__main__":
    main()