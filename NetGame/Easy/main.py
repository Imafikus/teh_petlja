import smor.client as sm

COLUMNS = 7
ROWS = 6

# WE and THEY are used to mark our and opponent's pieces on the board
WE = 1
THEY = -1

def configure_smor():
    """Sets up the SMOR library configuration"""
    sm.config('smor.cloud.magija.rs')

def get_room_name():
    """Asks the player for game room name, and returns it"""
    return input('Enter game room name: ')

def is_first_player(room_name):
    """Returns True if we are the first player (connected first to the server).

    First we try to get from `game/<room_name>/first` mailbox. 

    If something is there, we are the second player, and need to signal to the first in `game/<room_name>/second` mailbox.

    If not, we are the first player, and put something there (to signal for the other player).
    """
    first_room = 'game/%s/first' % room_name
    value = sm.get_one(first_room)

    if value is None:
        # we are first
        sm.put(first_room, 'we-are-first') # doesn't matter what we put
        return True
    else:
        # we are second
        sm.put('game/%s/second' % room_name, 'we-are-second')
        return False

def wait_for_other_player(room_name):
    """Waits for the second player (when we are the first)

    Constantly attempts to read from `game/<room_name>/second` mailbox, until it reads something,
    which signals the other player has connected and the game can start.
    """
    value = None

    while value is None:
        # as long as we get None, wait
        value = sm.get_one('game/%s/second' % room_name)

def setup_board():
    """Creates the board.

    Board is a list of columns, all of which are empty at the start. As the game progresses, 
    each column will hold the pieces starting from the bottom, i.e. columns are numbered from the bottom.
    """
    board = []

    for i in range(COLUMNS):
        board.append([])

    return board

def get_piece(board, col, row):
    """Helper function that returns the piece on the board, or 0 if it doesn't exist"""

    column = board[col]
    if len(column) > row:
        return column[row]
    else:
        return 0

def get_winner(board):
    """Returns `WE` (1) if we won, `THEY` (-1) if we lost, and 0 if there is no winner"""

    # first check the verticals
    for col in range(COLUMNS):
        # a 4-in-a-column can start on rows 0, 1 or 2
        for start in [0, 1, 2]:
            piece = get_piece(board, col, start + 0)
            if (piece != 0 and
                piece == get_piece(board, col, start + 1) and
                piece == get_piece(board, col, start + 2) and
                piece == get_piece(board, col, start + 3)):
                return piece # we found a winner

    # now check the horisontals
    for row in range(ROWS):
        # a 4-in-a-row can start on columns 0, 1, 2 or 3
        for start in [0, 1, 2, 3]:
            piece = get_piece(board, start, row)
            if (piece != 0 and
                piece == get_piece(board, start + 1, row) and
                piece == get_piece(board, start + 2, row) and
                piece == get_piece(board, start + 3, row)):
                return piece # we found a winner

    # now check the diagonals
    # diagonals can start on rows 0, 1, or 2
    for row in [0, 1, 2]:
        # up-right diagonals can start on cols 0, 1, 2 or 3
        for col in [0, 1, 2, 3]:
            piece = get_piece(board, col, row)
            if (piece != 0 and
                piece == get_piece(board, col + 1, row + 1) and
                piece == get_piece(board, col + 2, row + 2) and
                piece == get_piece(board, col + 3, row + 3)):
                return piece # we found a winner

        # up-left diagonals can start on cols 3, 4, 5 or 6
        for col in [3, 4, 5, 6]:
            piece = get_piece(board, col, row)
            if (piece != 0 and
                piece == get_piece(board, col - 1, row + 1) and
                piece == get_piece(board, col - 2, row + 2) and
                piece == get_piece(board, col - 3, row + 3)):
                return piece # we found a winner

    return 0 # no winner found
       

def is_game_done(board):
    """Returns true if the game is finished.
    
    Game is finished if either someone won, or the board is full (a tie)
    """
    winner = get_winner(board)

    if winner != 0:
        return True

    is_full = True

    for column in board:
        if len(column) < ROWS:
            is_full = False

    return is_full

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

    # `range(n)` returns numbers 0, 1, ..., n-1
    # which is perfect for indexing lists of `n` elements
    for row in reversed(range(ROWS)):
        s = ' '
        for col in range(COLUMNS):
            piece = get_piece(board, col, row)
            s += PIECE_SYMBOL[piece] + ' '

        print(s)

    print('---------------')
    print(' 1 2 3 4 5 6 7 ')

def get_my_move():
    """Asks the player for a move. a move is a 1 - 7 integer designating a column"""
    v = input('Your move [1-7]: ')
    while not v.isdigit() or 1 > int(v) or int(v) > 7:
        v = input('Your move [1-7]: ')

    return int(v)


def send_move(room_name, box_name, move):
    """Sends a move to `game/<room_name>/move_<box_name>` mailbox"""
    sm.put('game/%s/move_%s' % (room_name, box_name), move)

def get_other_player_move(room_name, box_name):
    """Reads a move from `game/<room_name>/move_<box_name>` mailbox. waits until a message is found"""
    value = None

    while value is None:
        value = sm.get_one('game/%s/move_%s' % (room_name, box_name))

    return value

def perform_move(move, board, my_turn):
    """Puts a move (1-7) in the board. my_turn is True if it's our move, otherwise it's an opponents move."""
    if my_turn:
        board[move - 1].append(WE)
    else:
        board[move - 1].append(THEY)

def show_lost_message():
    """Shows a message in an event of a defeat, along with a reassuring yet meaningless supportive message about luck during further attempts."""
    print()
    print('You lost! Better luck next time!')

    
def show_win_message():
    """Shows a well deserved victory message, asserting the greatnes of the work just achieved."""
    print()
    print('You won! Great job!')

def show_tie_message():
    """Shows a tie message. 
    
    Thinking up with method documentation descriptions is hard work.
    """
    print()
    print("It's a tie!")

def main():
    """Main method"""

    # First, configure the smor library
    # Then ask the player for the name of the game room
    # Then check if you are the first player in the game
    #     If you are, wait for the other player
    # Then set the board up
    # If you are the first player, its your turn
    # As long as the game is not done do the following:
    #     Show the board to the player
    #     If it's your turn
    #         ask the player for the move, and send it to the other player
    #         otherwise, get the move from the other player
    #     perform that move on the board
    #     now its other players turn
    #
    #     show the board one last time
    #     get the winner, and show the correct message

    pass




if __name__ == "__main__":
    main()