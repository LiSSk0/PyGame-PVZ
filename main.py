import pygame
from objects import Board, Level
from functions import *
import os
from game_screens import level_screen, menu_screen, reg_screen

SIZE = WIDTH, HEIGHT = 1100, 600
BACK_COLOR = 'darkgreen'
FPS = 50

pygame.init()
screen = pygame.display.set_mode(SIZE)


def main():
    pygame.display.set_caption('Plants vs. Zombies')

    result = reg_screen(1100, 600)
    username = result[0]
    level = result[1]
    print('Hello,', username, 'welcome to the game!', level, 'level')
    # increase_level(username)

    result = menu_screen(FPS, username)
    print("opening level", result)
    if result == 1:
        level_screen(screen, WIDTH, HEIGHT, FPS, Level((10, 5, 3)))
    if result == 2:
        level_screen(screen, WIDTH, HEIGHT, FPS, Level((20, 10, 5)))
    if result == 3:
        level_screen(screen, WIDTH, HEIGHT, FPS, Level((25, 15, 10)))
    if result == 4:
        level_screen(screen, WIDTH, HEIGHT, FPS, Level((35, 25, 15)))
    if result == 5:
        level_screen(screen, WIDTH, HEIGHT, FPS, Level((40, 25, 35)))

    pygame.quit()


if __name__ == '__main__':
    main()
