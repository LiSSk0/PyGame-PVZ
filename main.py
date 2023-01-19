import pygame
from functions import *
from game_screens import level_screen, menu_screen, reg_screen

SIZE = WIDTH, HEIGHT = 1100, 600
BACK_COLOR = 'darkgreen'
FPS = 50


def main():
    pygame.init()
    pygame.display.set_caption('Plants vs. Zombies')

    open_reg = False
    result = reg_screen()
    username = result[0]

    while True:
        if open_reg:
            result = reg_screen()
            username = result[0]
            open_reg = False

        level = menu_screen(FPS, username)

        if level == 0:
            open_reg = True
        if level == 1:
            level_screen(FPS, Level((3, 2, 2)), username, level)
        if level == 2:
            level_screen(FPS, Level((8, 5, 4)), username, level)
        if level == 3:
            level_screen(FPS, Level((15, 8, 5)), username, level)
        if level == 4:
            level_screen(FPS, Level((20, 10, 8)), username, level)
        if level == 5:
            level_screen(FPS, Level((30, 15, 10)), username, level)


if __name__ == '__main__':
    main()
