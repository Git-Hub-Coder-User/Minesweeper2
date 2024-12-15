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
            if type(background.grid[y][x]) == Bomb and type(flags.grid[y][x]) == int:
                returned = False
            elif type(background.grid[y][x]) != Bomb and type(flags.grid[y][x]) == Flag:
                returned = False
    
    return returned

def won_game(time):
    print(time)
    font = pygame.font.SysFont(None, 84)
    surface = font.render("You Won! ", True, (0, 225, 0))
    screen.blit(surface, (300, 100))
    surface = font.render(f"Time: {int(time / 1000)} seconds", True, (0, 225, 0))
    screen.blit(surface, (200, 150)) 
    surface = font.render("Press space to play again", True, (0, 105, 50))
    screen.blit(surface, (50, 200))
    pygame.display.update()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

def lost_game():
    font = pygame.font.SysFont(None, 84)
    surface = font.render("You Lost! ", True, (225, 0, 0))
    screen.blit(surface, (300, 100))
    surface = font.render("Press space to play again", True, (0, 105, 50))
    screen.blit(surface, (50, 200))
    pygame.display.update()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

def main():
    time = 0
    screen.fill((225, 225, 225))

    flags = Grid()
    background = generate_puzzle()
    foreground = Grid("")
    foreground.convert_grid()
    foreground.visual_set_up(screen)

    first_click = False

    while True:
        #print(time)
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
                                foreground.delete(background, flags, screen, (y, x))
                                if type(background.grid[y][x]) == Bomb:
                                    lost_game()
                    elif first_click == False:
                        while True: 
                            if type(background.grid[y][x]) == Bomb: 
                                background = generate_puzzle()
                            else:
                                foreground.delete(background, flags, screen, (y, x), 1)
                                first_click = True
                                break
                elif mouse_button[2]:
                    if background.grid[y][x].displayed == False: 
                        if flags.grid[y][x] == 0:
                            flags.grid[y][x] = Flag((y, x))
                            flags.grid[y][x].display(screen)
                        else:
                            foreground.remove_flag(flags, (y, x), screen)
        

        # background.visual_set_up(screen)


        
        #foreground.visual_set_up(screen)

        if check_win(background, flags):
            won_game(time)
            break

        pygame.display.update()
        time += clock.tick(30)

        

        # [print(pygame.mouse.get_pos())]
    


main()
#won_game()
# print(background)