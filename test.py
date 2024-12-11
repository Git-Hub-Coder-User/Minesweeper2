from grid import Grid
from tile import Bomb

grid = Grid()

grid.generate_bombs()

for i in range(8):
    for j in range(8):
        if type(grid.grid[i][j]) == Bomb:
            grid.grid[i][j] = "x"


for i in range(8):
    for j in range(8):
        grid.grid[j][i] = 3

