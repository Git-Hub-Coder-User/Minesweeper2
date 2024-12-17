import pygame
import sys
from grid import Grid
from tile import(
    Bomb,
    Flag
)


pygame.init()
screen = pygame.display.set_mode((800, 850))
clock = pygame.time.Clock()

def generate_puzzle(bombs): 
    background = Grid()
    background.generate_bombs(bombs)
    print(background)
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

def won_game(time, font):
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

def lost_game(font):
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

def bottom_bar_flags(flags, screen):
    font = pygame.font.SysFont(None, 36)
    flag_num = font.render(f"{flags}", True, (225, 225, 225))
    if flags == 16: 
        flag = pygame.image.load("img/flag_img.png")
        flag = pygame.transform.scale(flag, (40, 40))
        screen.blit(flag, (200, 810))
    pygame.draw.rect(screen, (0, 105, 0), (250, 815, 50, 50))
    screen.blit(flag_num, (250, 815))

def bottom_bar_time(time, screen):
    font = pygame.font.SysFont(None, 36)
    time = font.render(f"{int(time / 1000)} seconds", True, (225, 225, 225))
    pygame.draw.rect(screen, (0, 105, 0), (550, 815, 500, 500))
    screen.blit(time, (550, 815))
    #second = font.render(f"seconds", True, (225, 225, 225))
    #screen.blit(second, (585, 815))

def main():
    time = 0
    num_flags = 1
    font = pygame.font.SysFont(None, 84)
    screen.fill((0, 105, 0))

    flags = Grid()
    background = generate_puzzle(num_flags)
    foreground = Grid("")
    foreground.convert_grid()
    foreground.visual_set_up(screen)

    first_click = False
    #first_click = True

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
                try: 
                    if mouse_button[0] == True:
                        if first_click == True:
                            if type(flags.grid[y][x]) == int:
                                if background.grid[y][x].displayed == False:
                                    foreground.delete(background, flags, screen, (y, x))
                                    if type(background.grid[y][x]) == Bomb:
                                        lost_game(font)
                        elif first_click == False:
                            while True: 
                                if type(background.grid[y][x]) == Bomb: 
                                    background = generate_puzzle(num_flags)
                                else:
                                    foreground.delete(background, flags, screen, (y, x), 1)
                                    first_click = True
                                    time = 0
                                    break
                    elif mouse_button[2]:
                        if background.grid[y][x].displayed == False: 
                            if flags.grid[y][x] == 0:
                                flags.grid[y][x] = Flag((y, x))
                                flags.grid[y][x].display(screen)
                                num_flags -= 1
                            else:
                                foreground.remove_flag(flags, (y, x), screen)
                                num_flags += 1
                except:
                    pass
                finally: 
                    bottom_bar_flags(num_flags, screen)
        

        # background.visual_set_up(screen)


        
        #foreground.visual_set_up(screen)
        if first_click == True:
            bottom_bar_time(time, screen)

        #if check_win(background, flags):
        #    won_game(time, font)
        #    break

        pygame.display.update()
        time += clock.tick(30)

        

        # [print(pygame.mouse.get_pos())]
    


main()
#won_game()
# print(background)