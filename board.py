"""
Board file, should only be used from the game file,
and not manipulated directly.
"""

class Board(object):
    """
    Board Class used to hold a respresentation of the current Game Board
    By Daniel Anderson
    """
    def __init__(self):
        """#creates a new empty game board
        #2d array of 0 Empty, 1 Human, 2 Computer
        """
        self.game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def winning_board(self):
        """
        checks to see if this board has a winner
        """
        #horizontal and vertical
        for i in range(0, 2):
            if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] != 0:
                return True
            if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] != 0:
                return True

        #diagonals
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != 0:
            return True
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != 0:
            return True

        return False

    def can_put(self, xcoord, ycoord):
        """Return true or false if a new piece can be place at that position
        Arguments:
            xcoord- row index,
            ycoord - y index
        """
        return self.game_board[xcoord][ycoord] == 0

    def put(self, xcoord, ycoord, player):
        """Places a new tile on the game board
        player must be [1, 2]
        xcoord, ycoord must be [0, 1, 2]
        """
        self.game_board[xcoord][ycoord] = player

    def out_of_moves(self):
        """returns true if there are no more available squares """
        for i in self.game_board:
            for j in i:
                if j == 0:
                    return False
        return True

    #returns a list of all possible moves
    def possible_moves(self):
        """returns a list of all possible moves """
        move_list = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.game_board[i][j] == 0:
                    move_list.append([i, j])
        return move_list

    def optimal_move(self):
        """return the best move out of the list of moves"""
        move_list = self.possible_moves()
        return move_list[0]

    def print_board(self):
        """Displays the game board"""
        print '----------'
        for i in self.game_board:
            print i
        print "--------------"
