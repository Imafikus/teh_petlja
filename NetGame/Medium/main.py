import smor.client as sm

COLUMNS = 7
ROWS = 6

# WE and THEY are used to mark our and opponent's pieces on the board
WE = 1
THEY = -1

def configure_smor():
    """Sets up the SMOR library configuration"""
    pass

def get_room_name():
    """Asks the player for game room name, and returns it"""
    pass

def is_first_player(room_name):
    """Returns True if we are the first player (connected first to the server).

    First we try to get from `game/<room_name>/first` mailbox. 

    If something is there, we are the second player, and need to signal to the first in `game/<room_name>/second` mailbox.

    If not, we are the first player, and put something there (to signal for the other player).
    """
    pass

def wait_for_other_player(room_name):
    """Waits for the second player (when we are the first)

    Constantly attempts to read from `game/<room_name>/second` mailbox, until it reads something,
    which signals the other player has connected and the game can start.
    """
    pass

def setup_board():
    """Creates the board.

    Board is a list of columns, all of which are empty at the start. As the game progresses, 
    each column will hold the pieces starting from the bottom, i.e. columns are numbered from the bottom.
    """
    pass

def get_piece(board, col, row):
    """Helper function that returns the piece on the board, or 0 if it doesn't exist"""

    pass

def get_winner(board):
    """Returns `WE` (1) if we won, `THEY` (-1) if we lost, and 0 if there is no winner"""

    pass
       

def is_game_done(board):
    """Returns true if the game is finished.
    
    Game is finished if either someone won, or the board is full (a tie)
    """
    pass

# symbols to display for each player. 
# 
# we could swap WE and THEY when we are the second player
# to give the same experience for both players.
PIECE_SYMBOL = {
    WE: '@',
    THEY: 'X',
    0: ' '
}

def show_board(board):
    """Displays the board. also includes the 1 - 7 numbers under the board to assist in moves
    """

    pass

def get_my_move():
    """Asks the player for a move. a move is a 1 - 7 integer designating a column"""
    pass


def send_move(room_name, box_name, move):
    """Sends a move to `game/<room_name>/move_<box_name>` mailbox"""
    pass

def get_other_player_move(room_name, box_name):
    """Reads a move from `game/<room_name>/move_<box_name>` mailbox. waits until a message is found"""
    pass

def perform_move(move, board, my_turn):
    """Puts a move (1-7) in the board. my_turn is True if it's our move, otherwise it's an opponents move."""
    pass

def show_lost_message():
    """Shows a message in an event of a defeat, along with a reassuring yet meaningless supportive message about luck during further attempts."""
    pass

    
def show_win_message():
    """Shows a well deserved victory message, asserting the greatnes of the work just achieved."""
    pass

def show_tie_message():
    """Shows a tie message. 
    
    Thinking up with method documentation descriptions is hard work.
    """
    pass

def main():
    """Main method"""
    pass




if __name__ == "__main__":
    main()