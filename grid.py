import random
import pygame

from tile import(
    Tile, 
    Blank, 
    Number, 
    Cover, 
    Bomb, 
)

class NegativeNumber(Exception):
    pass

class Grid:
    def __init__(self, fill = 0, size = 8):
        self.fill = fill
        self.size = size
        self.grid = []

        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(self.fill)
            self.grid.append(temp)
        
    def __str__(self):
        listed = ""
        for i in range(8):
            listed += f"{str(self.grid[i])}\n"
        return listed
    
    def convert_grid(self):
        for y in range(8):
            for x in range(8): 
                # print(y, x, self.grid[y][x])
                if type(self.grid[y][x]) == Bomb:
                    pass
                elif self.grid[y][x] == "":
                    self.grid[y][x] = Cover(position = (y, x))
                elif self.grid[y][x] == 0:
                    self.grid[y][x] = Blank(position=(y, x))
                elif self.grid[y][x] > 0 and self.grid[y][x]:
                    num = self.grid[y][x]
                    self.grid[y][x] = Number(position = (y, x), number = num)
                else:
                    pass

    def generate_bombs(self):
        #i should be 16
        for i in range(16):
            while True:
                col = random.randint(0, 7)
                row = random.randint(0, 7)
                #col = 3
                #row = i
                # print(col, row)
                # print(row, col)
                if type(self.grid[row][col]) != Bomb:
                    self.grid[row][col] = Bomb(position = (row, col))
                    self.update_grid(col, row)
                    break
    
    def update_grid(self, col, row):
        for mod in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            y = mod[1]
            x = mod[0]
            try:
                if type(self.grid[y][x]) != Bomb:
                    self.grid[row + y][col + x] += 1
            except:
                pass
    
    def visual_set_up(self, screen):
        #print(self.grid)
        for y in range(8):
            for x in range(8):
                try: 
                    temp = self.grid[y][x]
                    #print(f"{x}, {y}, {self.grid[y][x]}")
                    #print(type(temp))
                    temp.display(screen)
                except:
                    pass

    #This might blow up
    def delete(self, background, screen, location):
        y, x = location

        #temp = self.grid[y][x]
        #self.grid[y][x] = None
        #del temp

        
        temp = background.grid[y][x]
        #print(temp)
        temp.display(screen)

        for i in range(3):
            y2, x2 = location
            mod = (random.randint(-1, 1), random.randint(-1, 1))
            x2 += mod[0]
            y2 += mod[1]
            print(y2, x2)
            try: 
                if x2 >= 0 and y2 > 0: 
                    if type(background.grid[y2][x2]) != Bomb:
                            background.grid[y2][x2].display(screen)
            except:
                pass