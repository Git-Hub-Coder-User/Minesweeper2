import pygame
import sys
from grid import Grid
from tile import(
    Tile, 
    Blank, 
    Number, 
    Cover, 
    Bomb
)

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


def main():
    screen.fill((225, 225, 225))


    background = Grid(0)
    #background.generate_bombs()
    #print(background.grid)
    background.convert_grid()
    #background.visual_set_up(screen)

    foreground = Grid("")
    #print(foreground)
    foreground.convert_grid()
    foreground.visual_set_up(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                #print(pygame.mouse.get_pos())
                y = y / 100
                x = x / 100
                #print(int(x), int(y), background.grid[y][x])
                foreground.delete(background, screen, (int(y), int(x)))
        

        # background.visual_set_up(screen)


        
        #foreground.visual_set_up(screen)

        pygame.display.update()
        clock.tick(30)

        

        # [print(pygame.mouse.get_pos())]
    


main()
# print(background)