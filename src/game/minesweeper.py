from random import seed, choice
from cellstatus import CellStatus
from gamestatus import GameStatus

class MineSweeper():
  def __init__(self):
    self.BOUNDS = 10
    self.cell_status = [[CellStatus.UNEXPOSED for i in range(self.BOUNDS)] \
      for j in range(self.BOUNDS)]
    self.is_mined = [[False for i in range(self.BOUNDS)] \
      for j in range(self.BOUNDS)]
  
  def is_valid_cell(self, row, column):
    return 0 <= row < self.BOUNDS and 0 <= column < self.BOUNDS
  
  def expose_neighbours(self, row, column):
    neighbor_range = [-1, 0, 1]
    for i in neighbor_range:
      for j in neighbor_range:
        if self.is_valid_cell(row + i, column + j):
          self.expose_cell(row + i, column + j)
  
  def expose_cell(self, row, column):
    if row < 0 or column < 0:
      raise IndexError('Outside of the range...')
    
    if self.cell_status[row][column] == CellStatus.UNEXPOSED:
      self.cell_status[row][column] = CellStatus.EXPOSED
      
      if not self.calculate_adjacent_mine_count(row, column):
        self.expose_neighbours(row, column)
  
  def get_cell_status(self, row, column):
    return self.cell_status[row][column]
  
  def seal_unseal_cell(self, row, column):
    if self.cell_status[row][column] != CellStatus.EXPOSED:
      self.cell_status[row][column] = CellStatus.SEALED if \
        self.cell_status[row][column] == CellStatus.UNEXPOSED else \
        CellStatus.UNEXPOSED
  
  def is_mine_at(self, row, column):
    return self.is_valid_cell(row, column) and self.is_mined[row][column]
  
  def set_mine_at(self, row, column):
    if self.is_valid_cell(row, column):
      self.is_mined[row][column] = True
  
  def calculate_adjacent_mine_count(self, row, column):
    adjacent_mine_count = 0
    neighbor_range = [-1, 0, 1]
    
    if self.is_mine_at(row, column):
      return 0
    
    for i in neighbor_range:
      for j in neighbor_range:
        if self.is_mine_at(row + i, column + j):
          adjacent_mine_count = adjacent_mine_count + 1
    
    return adjacent_mine_count
  
  def get_game_status(self):
    cells = [(i, j) for i in range(self.BOUNDS) for j in range(self.BOUNDS)]

    if any(filter(lambda cell: self.is_mined[cell[0]][cell[1]] and \
      self.cell_status[cell[0]][cell[1]] == CellStatus.EXPOSED, cells)):
      return GameStatus.LOST

    def check_won_or_in_progress():
      mined_unsealed_or_unmined_unexposed = lambda i, j: \
        self.is_mined[i][j] and self.cell_status[i][j] != CellStatus.SEALED \
          or not self.is_mined[i][j] and \
          self.cell_status[i][j] != CellStatus.EXPOSED

      if any(filter(lambda cell: \
        mined_unsealed_or_unmined_unexposed(cell[0], cell[1]), cells)):
        return GameStatus.INPROGRESS 
      
      return GameStatus.WIN

    return check_won_or_in_progress()
  
  def set_mines(self, seed_val):
    seed(seed_val)
    cells = [i for i in range(self.BOUNDS * self.BOUNDS)]
    
    for _ in range(10):
      selection = choice(cells)
      self.set_mine_at(int(selection % 10), int(selection / 10))
