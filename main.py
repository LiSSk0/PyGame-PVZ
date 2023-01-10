import pygame
from objects import Board
from functions import *
from game_screens import level_screen, menu_screen, reg_screen


SIZE = WIDTH, HEIGHT = 1100, 600
BACK_COLOR = 'darkgreen'
FPS = 50

pygame.init()
screen = pygame.display.set_mode(SIZE)


def main():
    pygame.display.set_caption('Plants vs. Zombies')
    result = reg_screen()
    print('Hello,', result[0].capitalize(), 'welcome to the game!', result[1], 'level')
    result = menu_screen(FPS)
    if result == 1:
        level_screen(screen, WIDTH, HEIGHT, FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
