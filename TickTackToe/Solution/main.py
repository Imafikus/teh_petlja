import os

C_ROWS = 3
C_COLS = 3
EMPTY_SYMBOL = ' - '
DIR_PATH = "results"
FILE_SUFIX = ".txt"

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
    print("Welcome to the awesome tick-tack-toe game simulator, I hope you'll have fun!")

def get_player_names():
    """
    Gets and returns player names as a tuple.
    First element in the tuple is the name of the first player.
    Second element in the tuple is the name of the second player.
    """
    first_player = input("Please input the name of the first player: ")

    second_player = input("Please input the name of the second player: ")

    return first_player, second_player

def construct_board():
    """
    Creates empty tick-tack-toe board

    It returns it as a matrix of strings.
    """

    #? We will construct board as array of strings, because it's the easiest way to do it
    board = []
    
    i = 0
    while i < C_ROWS * C_COLS:
        board.append(EMPTY_SYMBOL)
        i += 1

    return board

def create_signs(first_player, second_player):
    """
    Creates and returns dictionary which contains signs which players are using,
    it can be modifed to take custom signs.
    """

    signs = {}
    signs[first_player] = " X "  
    signs[second_player] = " O "

    return signs

def print_board(board):
    """
    Prints the current board.
    """

    i = 0
    j = 0

    to_print = ""
    while i < C_COLS * C_ROWS:
        
        to_print += board[i]
        j += 1
        
        #? if the j is 3, we know that we must go to the new row
        if j == 3:
            to_print += "\n"
            j = 0        
        
        i += 1

    print(to_print)

def make_input(board, player, player_sign):
    """
    Asks the player for input, check if the input is correct and update the board if it is.

    Returns the col and row players has input
    """
    #? This is used because we know that we have a square matrix, and that only
    #? valid cols and rows are those below, so this is the easiest solution
    valid_fields = ['0', '1', '2']

    #? We want to have them in the main scope so we can return their valid values
    row = ""
    col = ""

    print(player, " on the move")

    valid_input = False
    while(not valid_input):

        player_input = input("Please input row and column, separated by space: ")
        player_input = player_input.split(" ")
        
        if(len(player_input) != 2): 
            print("You must enter 2 valid fields separated by space, try again")
            continue
        
        row = player_input[0]
        col = player_input[1]

        if((row not in valid_fields or col not in valid_fields)):
            print("You must enter 2 valid fields, try again")
            continue
        
        row = int(row)
        col = int(col)

        if board[BOARD_FIELDS[(row, col)]] != EMPTY_SYMBOL:
            print("That field already has an input, try again")
            continue
        
        valid_input = True
        board[BOARD_FIELDS[(row, col)]] = player_sign
        
    print_board(board)

def tie(board):
    """
    Checks if the result is tied. This function is always called after
    win checking, so that we for sure know that there are no more fields to be filled
    and that no one has won
    """
    all_filled = True
    
    #? Another way this loop can be done is to 
    #? go directly to values which corespond to
    #? dictionary keys.
    #? we can do that by typing: for key, value in dict.items(): do something
    for pos in BOARD_FIELDS:
        if(board[BOARD_FIELDS[pos]] == EMPTY_SYMBOL):
            all_filled = False

    return  all_filled

def check_win(board, sign):
    """
    Checks if the player who had last input has won, returns true or false
    """
    
    #? All horizontal checks
    if(board[0] == board[1] == board[2] == sign):
        return True
    
    if(board[3] == board[4] == board[5] == sign):
        return True
    
    if(board[6] == board[7] == board[8] == sign):
        return True

    #? All vertical checks
    if(board[0] == board[3] == board[6] == sign):
        return True
    
    if(board[1] == board[4] == board[7] == sign):
        return True

    if(board[2] == board[5] == board[8] == sign):
        return True

    #? upper left to lower right diagonal check
    if(board[0] == board[4] == board[8] == sign):
        return True

    #? upper right to lower left diagonal check
    if(board[2] == board[4] == board[6] == sign):
        return True

    #? If we are here, we know for sure that win hasn't happened
    return False

def create_file_path(first_player, second_player):
    """
    Creates appropriate file path as stated in the specification
    File path is: first_player+second_player+FILE_SUFIX 
    Returns that file as a string
    """
    file_name = first_player.lower() + second_player.lower() + FILE_SUFIX
    file_path = os.path.join(DIR_PATH, file_name)
    return file_path

def file_exists(first_player, second_player):
    """
    Checks if file exists.
    If it does, return true, else return false

    """
    file_path = create_file_path(first_player, second_player)
    return(os.path.isfile(file_path))

def record_result(first_player, second_player, winner):
    """
    Records the result for the current game. Tries to write into the 
    file which is named first_player_second_player and which is stored in
    the directory results. 
    If the file with the same name (or with the inverted name) exists, it writes into 
    that file, otherwise makes a new file. 
    File name is all lower case.
    """

    file_already_exists = False

    if(file_exists(first_player, second_player)):
        file_path = create_file_path(first_player, second_player)
        file_already_exists = True
    
    elif(file_exists(second_player, first_player)):
        file_path = create_file_path(first_player, second_player)
        file_already_exists = True
    
    else:
        file_path = create_file_path(first_player, second_player)

    print("file_path: ", file_path)

    first_player_won = 0
    second_player_won  = 0
    tie = 0

    #? we are using these variables so we can easily write updated data to files
    #? because logic is the same, only difference is if the file already existed
    if winner == first_player:
            first_player_won += 1
        
    elif winner == second_player:
        second_player_won += 1
        
    else:
        tie += 1

    #! needs inverted name check

    #? If the file exists, we wanna get existing data, and after that we want to update that data
    if(file_already_exists):
        data = open(file_path, 'w+')

        games_data = data.readlines()
        print(games_data)
        first_player_wins = int(games_data[0])
        second_player_wins = int(games_data[1])
        ties = int(games_data[2])

        #? we are checking to see which result we need to update
        #? we are adding values everywhere because we know that only one 
        #? value will be 1, others will be zero, so they won't change anything
        data.write(str(first_player_wins + first_player_won) + "\n")
        data.write(str(second_player_wins + second_player_won) + "\n")
        data.write(str(ties + tie) + "\n")
        data.close()

    #? if the file doesn't exist, we want to create new file and write
    #? just the data from the latest game
    else:
        data = open(file_path, "w")
        data.writelines(str(first_player_won) + "\n")
        data.writelines(str(second_player_won) + "\n")
        data.writelines(str(tie) + "\n")
        data.close()


def main():

    print(BOARD_FIELDS[(0, 0)])

    board = construct_board()
    
    display_welcome_message()
    first_player, second_player = get_player_names()
    
    signs = create_signs(first_player, second_player)    

    first_player_move = True
    
    #! To be removed
    winner = ""
    record_result(first_player, second_player, winner)


    while(not tie(board) and winner == ""):
        
        if(first_player_move):
            make_input(board, first_player, signs[first_player])
            
            if(check_win(board, signs[first_player])):
                winner = first_player
            
            first_player_move = False
        
        else:
            make_input(board, second_player, signs[second_player])
            
            if(check_win(board, signs[second_player])):
                winner = second_player
            
            first_player_move = True
        
    if(winner == ""):
        print("It's a tie!")
        
    else:
        print("Winner is: ", winner)

    record_result(first_player, second_player, winner)


    display_current_stats()
    playing_again = ask_for_another_game()
    

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
    #? IMPORTANT: Every pair of players must have his own .txt files (order of the players is irrelevant), player names are not case sensitive
    #? If the .txt file already exist, it must be updated with the new results
    #? Example file you can use as pattern (but you don't have to) is example_saved_data.txt

    #? Appropriate message is displayed after the game has finished (based on who won, or if it was a tie)
    #? After 'enter' key is pressed current game statistics are show in the following format:
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