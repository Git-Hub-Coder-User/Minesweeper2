import random
import pygame

from tile import(
    Blank, 
    Number, 
    Cover, 
    Bomb, 
    Flag
)

class NegativeNumber(Exception):
    pass

class Grid:
    square = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

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

    def generate_bombs(self, bombs = 16):
        for i in range(bombs):
            while True:
                col = random.randint(0, 7)
                row = random.randint(0, 7)
                if type(self.grid[row][col]) != Bomb:
                    self.grid[row][col] = Bomb(position = (row, col))
                    self.update_grid(col, row)
                    break
    
    def update_grid(self, col, row):
        i = 0
        for mod in Grid.square:
            y = mod[1]
            x = mod[0]
            #print(i)
            try:
                if (y + row) >= 0 and  (col + x) >= 0: 
                    if type(self.grid[y + row][x + col]) != Bomb:
                        #print(f"Item: {self.grid[col + x][row + y]}, Location: {col + x}, {row + y}")
                        self.grid[row + y][col + x] += 1
                else:
                    pass
            except:
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
    def delete(self, background, flags, screen, location, behavior = 0, repeat = 5):
        y, x = location
        temp = background.grid[y][x]
        temp.display(screen)
        for i in range(repeat):
            y2, x2 = location
            mod = (random.randint(-1, 1), random.randint(-1, 1))
            x2 += mod[0]
            y2 += mod[1] 
            try: 
                #print("Line 111")
                if type(background.grid[y2][x2]) != Bomb:
                    if behavior == 0: 
                        if x2 >= 0 and y2 > 0: 
                            if type(flags.grid[y2][x2]) != Flag:
                                background.grid[y2][x2].display(screen)

                    if behavior == 1:
                        if x2 >= 0 and y2 > 0: 
                            if type(flags.grid[y2][x2]) != Flag:
                                background.delete(background, flags, screen, (y2, x2), 0, 8)
            except:
                pass
    
    def remove_flag(self, flags, position, screen):
        y, x = position
        flags.grid[y][x] = 0
        temp = Cover((y, x))
        temp.display(screen)
