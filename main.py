import pygame
import sys
from grid import Grid
from tile import(
    Tile, 
    Blank, 
    Number, 
    Cover, 
    Bomb,
    Flag
)

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

def generate_puzzle(): 
    background = Grid()
    background.generate_bombs()
    background.convert_grid()
    return background

def check_win(background, flags):
    returned = True
    for y in range(8):
        for x in range(8):
            if type(background.grid[y][x]) == Bomb and type(flags.grid[y][x]) == Flag:
                pass
            elif type(background.grid[y][x]) == Bomb and type(flags.grid[y][x]) == int:
                returned = False
            elif type(background.grid[y][x]) != Bomb and type(flags.grid[y][x]) == Flag:
                returned = False
    
    return returned


def main():
    screen.fill((225, 225, 225))

    flags = Grid()
    background = generate_puzzle()
    foreground = Grid("")
    foreground.convert_grid()
    foreground.visual_set_up(screen)

    first_click = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                #print(pygame.mouse.get_pos())
                y = int(y / 100)
                x = int(x / 100)
                #print(int(x), int(y), background.grid[y][x])
                mouse_button = pygame.mouse.get_pressed(num_buttons=3)
                if mouse_button[0] == True:
                    if first_click == True:
                        if type(flags.grid[y][x]) == int:
                            if background.grid[y][x].displayed == False:
                                foreground.delete(background, screen, (y, x))
                    elif first_click == False:
                        while True: 
                            if type(background.grid[y][x]) == Bomb: 
                                background = generate_puzzle()
                            else:
                                foreground.delete(background, screen, (y, x), 1)
                                first_click = True
                                break
                elif mouse_button[2]:
                    if type(flags.grid[y][x]) == int: 
                        flags.grid[y][x] = Flag((y, x))
                        flags.grid[y][x].display(screen)
                    else:
                        foreground.remove_flag(flags, (y, x), screen)
        

        # background.visual_set_up(screen)


        
        #foreground.visual_set_up(screen)

        if check_win(background, flags):
            pass
        
        pygame.display.update()
        clock.tick(30)

        

        # [print(pygame.mouse.get_pos())]
    


main()
# print(background)