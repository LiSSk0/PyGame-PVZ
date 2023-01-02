import pygame
import os
import sys


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
