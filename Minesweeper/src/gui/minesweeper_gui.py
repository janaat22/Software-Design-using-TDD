import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src/game'))

from random import randint
from tkinter import *
from tkinter import messagebox

from minesweeper import MineSweeper
from cellstatus import CellStatus
from gamestatus import GameStatus

is_first_click = True
minesweeper = MineSweeper()
minesweeper.set_mines(randint(0, 100))
root = Tk()
root.title('Minesweeper')

def disable_cells():
  for row in range(minesweeper.BOUNDS):
    for col in range(minesweeper.BOUNDS):
      button[row][col].config(state="disabled")

def handle_left_click(row, col):
  minesweeper.expose_cell(row, col)
  
  if minesweeper.get_game_status() == GameStatus.INPROGRESS:
    expose_cell_ui(row, col)
  elif minesweeper.get_game_status() == GameStatus.LOST:
    button[row][col].configure(text="X")
    disable_cells()
    messagebox.showinfo("Game Over!", ":(")
  elif minesweeper.get_game_status() == GameStatus.WIN:
    button[row][col].configure(text=minesweeper.calculate_adjacent_mine_count(row, col))
    disable_cells()
    messagebox.showinfo("You WON!!!", ":D")

def handle_right_click(row, col):
  minesweeper.seal_unseal_cell(row, col)
  
  button_text = '*' if \
    minesweeper.cell_status[row][col] == CellStatus.SEALED \
    else " "
  button[row][col].configure(text=button_text)
  
  if minesweeper.get_game_status() == GameStatus.WIN:
    disable_cells()
    messagebox.showinfo("You WON!!!", ":D")

def expose_cell_ui(row, col):
  for row in range(minesweeper.BOUNDS):
    for col in range(minesweeper.BOUNDS):
      if minesweeper.cell_status[row][col] == CellStatus.EXPOSED:
        button_text = '' if not \
          minesweeper.calculate_adjacent_mine_count(row, col) \
          else str(minesweeper.calculate_adjacent_mine_count(row, col))
        
        button[row][col].configure(text=button_text, state=DISABLED, fg='black', bg='light blue')

frame1 = Frame(root, bg='green')
frame1.pack(expand=True, fill=BOTH)

def __cbHandler(event, row, col):
  if (event.num == 1):
    handle_left_click(row, col)
  elif (event.num == 3 or event.num == 2):
    handle_right_click(row, col)

def get_button(row, col):
  button = Button(frame1,
    height=2,
    width=4,
    highlightbackground='#3E4149',
    text=" ")
  
  def handler(event, row=row, col=col):
    return __cbHandler(event, row, col)
  
  button.bind('<Button>', handler)
  return button

button = [[get_button(i, j) for j in range(minesweeper.BOUNDS)] for i in range(minesweeper.BOUNDS)]

for row in range(minesweeper.BOUNDS):
  for col in range(minesweeper.BOUNDS):
    button[row][col].grid(row=row, column=col, sticky="nsew")

root.mainloop()
