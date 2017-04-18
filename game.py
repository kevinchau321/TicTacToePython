from board import Board
import time
import random

class Game:
  def __init__(self):
    self.board = Board()
    self.display_game_info()
    self.collect_player_info()
    self.play()

  def switch_players(self):
    if self.curr_player == 1:
      self.curr_player = 2
    else:
      self.curr_player = 1


  def display_game_info(self):
    print "Welcome to my version of Tic Tac Toe\n"
    print "I hope you came ready to play\n"

  #collects the initial information about each player
  def collect_player_info(self):
    #get the users name
    self.player_name = raw_input('Enter your name: ')
    #who goes first
    while(True):
      print "Please tell us who should go first"
      print "0 -- RANDOM"
      print "1 -- HUMAN"
      print "2 -- COMPUTER"
      self.curr_player = int(raw_input("Please enter a 0, 1, or 2: "))
      if self.curr_player in [0, 1, 2]:
        if self.curr_player == 0:
          self.curr_player = random.randint(1,2)
        break
      else:
        print "I am sorry, we didnt not recognize the input, try again \n"

  def play(self):
    print "----------------- HAVE FUN ----------------- "
    while(not self.board.out_of_moves()):
      print "Here is the current Board"
      self.board.print_board()
      if self.curr_player == 1:
        print "It is currently your turn " + self.player_name
        print "Good Luck."
        x = int(raw_input("Please input the x coordinate of your move"))
        y = int(raw_input("Please input the y coordinate of your move"))
        if x in [0, 1, 2] and y in [0, 1, 2]:
          if(self.board.can_put(x,y)):
            self.board.put(x, y, self.curr_player)
            if self.board.winning_board():
              print "Congradulations" + self.player_name + ", you won!"
              break
            self.switch_players()
          else:
            print "You input a valid position, but that position isn't available"
        else:
          print "Those coordinates are not valid, please try again"
      else:
        print "It is currently the computers turn:"
        print "Please Wait while he makes a move"
        time.sleep(2)
        optimal_move = self.board.optimal_move()
        self.board.put(optimal_move[0], optimal_move[1], self.curr_player)
        if self.board.winning_board():
          print "Too bad the computer won"
          break
        self.switch_players()
    print "Here was the winning Board:"
    print self.board.print_board()
    print "Thank you for playing"
    print "This Game was made by Daniel Anderson"


#executing the game
Game()

