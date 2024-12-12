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
    #Use fill for the back
    # img\backgroud_img.png
    screen.fill((225, 225, 225))


    background = Grid(0)
    background.generate_bombs()
    background.convert_grid()
    background.visual_set_up(screen)

    foreground = Grid(Cover)
    #print(foreground)
    #foreground.visual_set_up(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                y, x = pygame.mouse.get_pos()
                print(pygame.mouse.get_pos())
                y = (y - 50) / 100
                x = (x - 50) / 100
                print(y, x)
                # foreground.delete((int(y), int(x)))
        

        # background.visual_set_up(screen)


        pygame.display.update()
        clock.tick(30)

        

        # [print(pygame.mouse.get_pos())]
    


main()
# print(background)