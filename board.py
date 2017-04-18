class Board:
  #creates a new empty game board
  #the board is a 2d array of 0, 1, 2 Empty, Player 1, Player 2
  def __init__(self):
    self.game_board = [[0,0,0],[0,0,0],[0,0,0]]

  #checks to see if this board has a winner
  def winning_board(self):
    #check horizontal and vertical
    for i in range(0,2):
      if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] != 0:
        return True
      if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] != 0:
        return True

    #check diagonals
    if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != 0:
        return True
    if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != 0:
        return True
    #else return false
    return False

  #can we place a new square on the board
  def can_put(self, x, y):
    return self.game_board[x][y] == 0

  #player must be 1, or 2
  #x, y must be within the game board
  def put(self, x, y, player):
    self.game_board[x][y] = player

  #returns true if there are no more available squares
  def out_of_moves(self):
    for i in self.game_board:
      for j in i:
        if j == 0:
          return False
    return True

  #returns a list of all possible moves
  def possible_moves(self):
    move_list = []
    for i in range(0,3):
      for j in range(0,3):
        if self.game_board[i][j] == 0:
          move_list.append([i,j])
    return move_list


  #return the best move out of the list of moves
  def optimal_move(self):
    move_list = self.possible_moves()
    return move_list[0]

  def print_board(self):
    print '----------'
    for i in self.game_board:
      print i
    print "--------------"