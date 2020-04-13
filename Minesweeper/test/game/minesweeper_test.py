import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src/game'))

from minesweeper import MineSweeper
from cellstatus import CellStatus
from gamestatus import GameStatus

class MinesweeperTests(unittest.TestCase):
  def setUp(self):
    self.minesweeper = MineSweeper()
  
  def test_Canary(self):
    self.assertTrue(True)
  
  def test_expose_an_unexposed_cell(self):
    self.minesweeper.expose_cell(1, 3)
    
    self.assertEqual(CellStatus.EXPOSED,
      self.minesweeper.get_cell_status(1, 3))
  
  def test_expose_an_exposed_cell(self):
    self.minesweeper.expose_cell(4, 3)
    self.minesweeper.expose_cell(4, 3)
    
    self.assertEqual(CellStatus.EXPOSED,
      self.minesweeper.get_cell_status(4, 3))
  
  def test_expose_a_cell_outside_of_the_range(self):
    with self.assertRaises(IndexError):
      self.minesweeper.expose_cell(-1, 2)
    with self.assertRaises(IndexError):
      self.minesweeper.expose_cell(10, 3)
    with self.assertRaises(IndexError):
      self.minesweeper.expose_cell(3, -1)
    with self.assertRaises(IndexError):
      self.minesweeper.expose_cell(3, 10)
  
  def test_check_initial_status(self):
    self.assertEqual(CellStatus.UNEXPOSED,
      self.minesweeper.get_cell_status(2, 3))
  
  def test_seal_unexposed_cell(self):
    self.minesweeper.seal_unseal_cell(4, 3)
    
    self.assertEqual(CellStatus.SEALED,
      self.minesweeper.get_cell_status(4, 3))
  
  def test_unseal_sealed_cell(self):
    self.minesweeper.seal_unseal_cell(4, 3)
    self.minesweeper.seal_unseal_cell(4, 3)
    
    self.assertEqual(CellStatus.UNEXPOSED,
      self.minesweeper.get_cell_status(4, 3))
  
  def test_seal_exposed_cell(self):
    self.minesweeper.expose_cell(4, 3)
    self.minesweeper.seal_unseal_cell(4, 3)
    
    self.assertEqual(CellStatus.EXPOSED,
      self.minesweeper.get_cell_status(4, 3))
  
  def test_expose_sealed_cell(self):
    self.minesweeper.seal_unseal_cell(4, 3)
    self.minesweeper.expose_cell(4, 3)
    
    self.assertEqual(CellStatus.SEALED,
      self.minesweeper.get_cell_status(4, 3))
  
  def test_expose_calls_expose_neighbors(self):
    expose_neighbours_called = False
    
    class MineSweeperStub(MineSweeper):
      def expose_neighbours(self, row, column):
        nonlocal expose_neighbours_called
        expose_neighbours_called = True
    
    minesweeper = MineSweeperStub()
    minesweeper.expose_cell(3, 4)
    
    self.assertTrue(expose_neighbours_called)
    expose_neighbours_called = False
  
  def test_expose_call_on_exposed_cell_does_not_expose_neighbors(self):
    expose_neighbours_called = False
    
    class MineSweeperStub(MineSweeper):
      def expose_neighbours(self, row, column):
        nonlocal expose_neighbours_called
        expose_neighbours_called = True
    
    minesweeper = MineSweeperStub()
    minesweeper.cell_status[4][3] = 2
    minesweeper.expose_cell(4, 3)
    
    self.assertFalse(expose_neighbours_called)
    expose_neighbours_called = False
  
  def test_expose_call_on_sealed_cell_does_not_expose_neighbors(self):
    expose_neighbours_called = False
    
    class MineSweeperStub(MineSweeper):
      def expose_neighbours(self, row, column):
        nonlocal expose_neighbours_called
        expose_neighbours_called = True
    
    minesweeper = MineSweeperStub()
    minesweeper.cell_status[4][3] = 3
    minesweeper.expose_cell(4, 3)
    
    self.assertFalse(expose_neighbours_called)
    expose_neighbours_called = False
  
  def test_expose_neighbors_calls_expose_on_eight_neighbors(self):
    neighbors = []
    
    class MineSweeperStub(MineSweeper):
      
      def expose_cell(self, row, column):
        nonlocal neighbors
        neighbors.append((row, column))
    
    minesweeper = MineSweeperStub()
    minesweeper.expose_neighbours(4, 3)
    neighbors.remove((4, 3))
    
    self.assertEqual(
      [(3, 2), (3, 3), (3, 4), (4, 2), (4, 4), (5, 2), (5, 3), (5, 4)],
      neighbors)
  
  def test_expose_neighbours_top_left_cell_calls_expose_only_existing_cells(self):
    neighbors = []
    
    class MineSweeperStub(MineSweeper):
      
      def expose_cell(self, row, column):
        nonlocal neighbors
        neighbors.append((row, column))
    
    minesweeper = MineSweeperStub()
    minesweeper.expose_neighbours(0, 0)
    neighbors.remove((0, 0))
    
    self.assertEqual([(0, 1), (1, 0), (1, 1)], neighbors)
  
  def test_expose_neighbours_bottom_left_cell_calls_expose_only_existing_cells(self):
    neighbors = []
    
    class MineSweeperStub(MineSweeper):
      
      def expose_cell(self, row, column):
        nonlocal neighbors
        neighbors.append((row, column))
    
    minesweeper = MineSweeperStub()
    minesweeper.expose_neighbours(9, 9)
    neighbors.remove((9, 9))
    
    self.assertEqual([(8, 8), (8, 9), (9, 8)], neighbors)
  
  def test_expose_neighbors_border_cell_calls_expose_only_existing_cells(self):
    neighbors = []
    
    class MineSweeperStub(MineSweeper):
      
      def expose_cell(self, row, column):
        nonlocal neighbors
        neighbors.append((row, column))
    
    minesweeper = MineSweeperStub()
    minesweeper.expose_neighbours(9, 5)
    neighbors.remove((9, 5))
    
    self.assertEqual([(8, 4), (8, 5), (8, 6), (9, 4), (9, 6)], neighbors)
  
  def test_check_mine_at_3_2(self):
    self.assertFalse(self.minesweeper.is_mine_at(3, 2))
  
  def test_set_and_check_mine_at_3_2(self):
    self.minesweeper.set_mine_at(3, 2)
    self.assertTrue(self.minesweeper.is_mine_at(3, 2))
  
  def test_check_mine_at_neg1_4(self):
    self.minesweeper.set_mine_at(-1, 4)
    self.assertFalse(self.minesweeper.is_mine_at(-1, 4))
  
  def test_check_mine_at_10_5(self):
    self.assertFalse(self.minesweeper.is_mine_at(10, 5))
  
  def test_check_mine_at_5_neg1(self):
    self.assertFalse(self.minesweeper.is_mine_at(5, -1))
  
  def test_check_mine_at_7_10(self):
    self.assertFalse(self.minesweeper.is_mine_at(7, 10))
  
  def test_exposing_adjacent_cell_does_not_expose_neighbors(self):
    expose_neighbours_called = False
    
    class MineSweeperStub(MineSweeper):
      def expose_neighbours(self, row, column):
        nonlocal expose_neighbours_called
        expose_neighbours_called = True
    
    minesweeper = MineSweeperStub()
    minesweeper.set_mine_at(0, 0)
    minesweeper.expose_cell(0, 1)
    
    self.assertFalse(expose_neighbours_called)
    expose_neighbours_called = False
  
  def test_adjacentMinesCountAt_4_6(self):
    self.assertEqual(0, self.minesweeper.calculate_adjacent_mine_count(4, 6))
  
  def test_set_and_verify_adjacentMinesCountAt_3_4(self):
    self.minesweeper.set_mine_at(3, 4)
    
    self.assertEqual(0, self.minesweeper.calculate_adjacent_mine_count(3, 4))
  
  def test_set_mine_at_3_4_and_verify_adjacentMinesCountAt_3_5(self):
    self.minesweeper.set_mine_at(3, 4)
    
    self.assertEqual(1, self.minesweeper.calculate_adjacent_mine_count(3, 5))
  
  def test_set_mine_at_3_4_and_2_6_verify_adjacentMinesCountAt_3_5(self):
    self.minesweeper.set_mine_at(3, 4)
    self.minesweeper.set_mine_at(2, 6)
    
    self.assertEqual(2, self.minesweeper.calculate_adjacent_mine_count(3, 5))
  
  def test_set_mine_at_0_1_and_verify_adjacentMinesCountAt_0_0(self):
    self.minesweeper.set_mine_at(0, 1)
    
    self.assertEqual(1, self.minesweeper.calculate_adjacent_mine_count(0, 0))
  
  def test_adjacentMinesCountAt_0_9(self):
    self.assertEqual(0, self.minesweeper.calculate_adjacent_mine_count(0, 9))
  
  def test_set_mine_at_9_8_and_verify_adjacentMinesCountAt_9_9(self):
    self.minesweeper.set_mine_at(9, 8)
    
    self.assertEqual(1, self.minesweeper.calculate_adjacent_mine_count(9, 9))
  
  def test_adjacentMinesCountAt_9_0(self):
    self.assertEqual(0, self.minesweeper.calculate_adjacent_mine_count(9, 0))
  
  def test_get_game_status(self):
    self.assertEqual(GameStatus.INPROGRESS, self.minesweeper.get_game_status())
  
  def test_expose_mined_cell_and_getGameStatus_returns_LOST(self):
    self.minesweeper.set_mine_at(4, 3)
    self.minesweeper.expose_cell(4, 3)
    self.assertEqual(GameStatus.LOST, self.minesweeper.get_game_status())
  
  def test_game_in_progress_after_all_mines_sealed_but_cells_remain_unexposed(self):
    self.minesweeper.set_mine_at(4, 3)
    self.minesweeper.seal_unseal_cell(4, 3)
    
    self.assertEqual(GameStatus.INPROGRESS, self.minesweeper.get_game_status())
  
  def test_game_in_progress_all_mines_sealed_not_an_empty_cell(self):
    self.minesweeper.set_mine_at(4, 3)
    self.minesweeper.seal_unseal_cell(4, 3)
    self.minesweeper.seal_unseal_cell(4, 4)
    
    self.assertEqual(GameStatus.INPROGRESS, self.minesweeper.get_game_status())
  
  def test_game_in_progress_all_mines_sealed_one_adjacent_cell_unexposed(self):
    self.minesweeper.set_mine_at(4, 3)
    self.minesweeper.seal_unseal_cell(4, 3)
    self.minesweeper.expose_cell(0, 0)
    self.minesweeper.cell_status[5][2] = CellStatus.UNEXPOSED
    
    self.assertEqual(GameStatus.INPROGRESS, self.minesweeper.get_game_status())
  
  def test_game_won_all_mines_sealed_and_all_other_cells_exposed(self):
    self.minesweeper.set_mine_at(4, 3)
    self.minesweeper.seal_unseal_cell(4, 3)
    
    self.minesweeper.expose_cell(0, 0)
    
    self.assertEqual(GameStatus.WIN, self.minesweeper.get_game_status())
  
  def test_total_mines_from_set_mines(self):
    self.minesweeper.set_mines(0)
    total_mine = 0
    
    for i in range(self.minesweeper.BOUNDS):
      for j in range(self.minesweeper.BOUNDS):
        if self.minesweeper.is_mine_at(i, j):
          total_mine += 1
    
    self.assertEqual(total_mine, 10)
  
  def test_mine_difference_calling_set_mines_with_different_seeds(self):
    self.minesweeper.set_mines(0)
    self.minesweeper.set_mines(1)
    total_mine = 0
    
    for i in range(self.minesweeper.BOUNDS):
      for j in range(self.minesweeper.BOUNDS):
        if self.minesweeper.is_mine_at(i, j):
          total_mine += 1
    
    self.assertLess(total_mine, 20)

if __name__ == '__main__':
  unittest.main()
