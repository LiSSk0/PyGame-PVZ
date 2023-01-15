import pygame
from functions import *
from game_screens import level_screen, menu_screen, reg_screen

SIZE = WIDTH, HEIGHT = 1100, 600
BACK_COLOR = 'darkgreen'
FPS = 50


def main():
    pygame.init()
    pygame.display.set_caption('Plants vs. Zombies')

    result = reg_screen()
    username = result[0]

    while True:
        level = menu_screen(FPS, username)

        if level == 1:
            level_screen(FPS, Level((10, 5, 3)), username, level)
        if level == 2:
            level_screen(FPS, Level((20, 10, 5)), username, level)
        if level == 3:
            level_screen(FPS, Level((25, 15, 10)), username, level)
        if level == 4:
            level_screen(FPS, Level((35, 25, 15)), username, level)
        if level == 5:
            level_screen(FPS, Level((40, 25, 35)), username, level)

    # pygame.quit()


if __name__ == '__main__':
    main()
