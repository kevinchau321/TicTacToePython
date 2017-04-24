from board import Board
import unittest

class BoardTest(unittest.TestCase):
    """This is the test class for board."""
    def generalTests(self):
        """General Tests."""
        board = Board()
        list_of_moves = board.possible_moves()
        self.assertEquals(len(list_of_moves), 9)
        board.put(0, 0, 1)
        board.put(0, 1, 1)
        board.put(0, 2, 1)
        self.assertTrue(board.winning_board())
        board.put(1, 0, 1)
        self.assertEquals(len(list_of_moves), 5)
        board.put(1, 1, 1)
        board.put(1, 2, 1)
        board.put(2, 0, 1)
        board.put(2, 1, 1)
        board.put(2, 2, 1)
        self.assertEquals(len(list_of_moves), 0)
        board.print_board()
        self.assertTrue(board.out_of_moves())
