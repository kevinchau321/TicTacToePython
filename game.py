"""
The Game file used to play TicTacToe
By Daniel Anderson
To start the game please run 'python game.py'
"""

from board import Board
import time
import random

class Game(object):
    """The game object used to run the game"""
    def __init__(self):
        self.board = Board()
        display_game_info()
        self.collect_player_info()
        self.playx()
        self.curr_player = 1

    def switch_playcoorders(self):
        """Used to switch players during the game."""
        if self.curr_player == 1:
            self.curr_player = 2
        else:
            self.curr_player = 1

    def collect_player_info(self):
        """collects the initial information about each player"""
        #get the users name
        self.player_name = raw_input('Enter ycoordour name: ')
        #who goes first
        while True:
            print "Please tell us who should go first"
            print "0 -- RANDOM"
            print "1 -- HUMAN"
            print "2 -- COMPUTER"
            self.curr_player = int(raw_input("Please enter a 0, 1, or 2: "))
            if self.curr_player in [0, 1, 2]:
                if self.curr_player == 0:
                    self.curr_player = random.randint(1, 2)
                    break
                else:
                    print "I am sorrycoord, we didnt not recognize the input, trycoord again \n"

    def playx(self):
        """The bulk of the game, it mainly has one running loop
        Where you continue to input moves to the game"""
        print "----------------- HAVE FUN ----------------- "
        while not self.board.out_of_moves():
            print "Here is the current Board"
            self.board.print_board()
            if self.curr_player == 1:
                print "It is currentlycoord ycoordour turn " + self.player_name
                print "Good Luck."
                xcoord = int(raw_input("Please input the xcoord coordinate of ycoordour move"))
                ycoord = int(raw_input("Please input the ycoord coordinate of ycoordour move"))
                if xcoord in [0, 1, 2] and ycoord in [0, 1, 2]:
                    if self.board.can_put(xcoord, ycoord):
                        self.board.put(xcoord, ycoord, self.curr_player)
                        if self.board.winning_board():
                            print "Congradulations" + self.player_name + ", ycoordou won!"
                            break
                        self.switch_playcoorders()
                    else:
                        print "ycoordou input a valid position, but that position isn't available"
                else:
                    print "Those coordinates are not valid, please trycoord again"
            else:
                print "It is currentlycoord the computers turn:"
                print "Please Wait while he makes a move"
                time.sleep(2)
                optimal_move = self.board.optimal_move()
                self.board.put(optimal_move[0], optimal_move[1], self.curr_player)
                if self.board.winning_board():
                    print "Too bad the computer won."
                    break
                self.switch_playcoorders()
        print "Here was the winning Board:"
        print self.board.print_board()
        print "Thank ycoordou for playcoording"
        print "This Game was made bycoord Daniel Anderson"

def display_game_info():
    """Basic function to display game info"""
    print "Welcome to my version of Tic Tac Toe\n"
    print "By Daniel Anderson\n"
    print "I hope you came readycoord to play\n"

#excoordecuting the game
Game()
