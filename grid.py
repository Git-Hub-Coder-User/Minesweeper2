import random

from tile import(
    Tile, 
    Blank, 
    Number, 
    Cover, 
    Bomb, 
)

class Grid:
    def __init__(self, fill = 0, size = 8):
        self.fill = fill
        self.size = size
        self.grid = []

        for i in range(size):
            temp = []
            for i in range(size):
                temp = []
                for j in range(size):
                    temp.append(self.fill)
                self.grid.append(temp)
        
    def __str__(self):
        listed = ""
        for i in range(8):
            listed += f"{self.grid[i]}\n"
        return listed
    
    def convert_grid(self):
        for y in range(8):
            for x in range(8): 
                # print(y, x, self.grid[y][x])
                if type(self.grid[y][x]) == Bomb:
                    pass
                elif self.grid[y][x] == 0:
                    self.grid[y][x] = Blank(position=(y, x))
                elif self.grid[y][x] > 0 and self.grid[y][x]:
                    num = self.grid[y][x]
                    self.grid[y][x] = Number(position = (y, x), number = num)
                else:
                    pass
    def generate_bombs(self):
        for i in range(16):
            while True:
                col = random.randint(0, 7)
                row = random.randint(0, 7)
                # print(col, row)
                # print(row, col)
                if type(self.grid[row][col]) != Bomb:
                    self.grid[row][col] = Bomb(position = (col, row))
                    self.update_grid(col, row)
                    break
    
    def update_grid(self, col, row):
        for mod in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            y = mod[0]
            x = mod[1]
            try:
                if type(self.grid[y][x]) != Bomb:
                    self.grid[row + y][col + x] += 1 
            except:
                pass
    
    def visual_set_up(self, screen):
        for y in range(8):
            for x in range(8):
                try: 
                    # print(f"{y}, {x}")
                    temp = self.grid[y][x]
                    # print(type(temp))
                    temp.display(screen)
                except:
                    pass

    #This might blow up
    def delete(self, location):
        y, x = location
        temp = self.grid[y][x]
        self.grid[y][x] = 0
        del temp
    