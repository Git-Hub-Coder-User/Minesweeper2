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
                #col = 7 - i
                #row = 0
                # print(col, row)
                # print(row, col)
                if type(self.grid[row][col]) != Bomb:
                    self.grid[row][col] = Bomb(position = (row, col))
                    self.update_grid(col, row)
                    break
    
    def update_grid(self, col, row):
        i = 0
        for mod in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            y = mod[1]
            x = mod[0]
            #print(i)
            try:
                if (y + row) >= 0 and  (col + x) >= 0: 
                    if type(self.grid[y + row][x + col]) != Bomb:
                        #print(f"Item: {self.grid[col + x][row + y]}, Location: {col + x}, {row + y}")
                        self.grid[row + y][col + x] += 1
                else:
                    #print(f"Failed the first test: {col + x}, {row + y}")
                    #print((y + col) >= 0)
                    #print((x + row) >= 0)
                    pass
            except:
                #print("The except ran", x + col, y + row)
                pass
            
            #i += 1
    
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

        for i in range(5):
            y2, x2 = location
            mod = (random.randint(-1, 1), random.randint(-1, 1))
            x2 += mod[0]
            y2 += mod[1]
            try: 
                #print(x2, y2, background.grid[y2][x2])
                if x2 >= 0 and y2 > 0: 
                    if type(background.grid[y2][x2]) != Bomb:
                        background.grid[y2][x2].display(screen)
                        if type(background.grid[y2][x2]) == Blank:
                            print("Made it to line 122", i)
                            background.blank_tile(screen, [y2][x2])
            except:
                pass
        
    def blank_tile(self, screen, location):
        for mod in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            y, x = location
            try:
                if (y + mod[1]) >= 0 and  (x + mod[0]) >= 0: 
                    if type(self.grid[y + row][x + col]) != Bomb:
                        self.grid[y + mod[1]][x + mod[0]] += 1
            except:
                pass