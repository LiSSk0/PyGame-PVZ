import pygame
import os
import sys
from random import randint
from objects import ZombieSprite


def decorations(screen, width, height):
    bush = pygame.image.load('textures/bush.png')

    rect_in = bush.get_rect()
    new_x = rect_in.width // 8
    new_y = rect_in.height // 8
    bush = pygame.transform.scale(bush, (new_x, new_y))

    bushes_count = 10
    step = height // bushes_count
    for i in range(bushes_count - 2):
        screen.blit(bush, [width - width // 10, step * i])


def generate_zombie_coords(board_top, cell_size, width, count):
    coords = []

    if count > 5:
        count = 5
        for line in range(count):
            coords.append((width, board_top + line * cell_size))
    else:
        i = 0
        # print("CYCLE: Started in func 'generate_zombie_coords'")
        while i < count:
            line = randint(0, 4)
            coord = (width, board_top + line * cell_size)
            if coord not in coords:
                coords.append(coord)
                i += 1
        # print("CYCLE: Finished in func 'generate_zombie_coords'")

    return sorted(coords)


def create_zombie_column(count, board_top, board_left, cell_size, width, sheet, sheet_xy, group):
    coords = generate_zombie_coords(board_top, cell_size, width, count)
    for i in range(count):
        zombie = ZombieSprite(sheet, sheet_xy[0], sheet_xy[1], coords[i], board_left, group)


def load_image(name, colorkey=None):
    fullname = os.path.join(name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image
