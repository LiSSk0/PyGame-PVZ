import pygame
import os
import sys
from random import randint
from objects import *


def decorations(screen, width, height):
    # bushes:
    bush = pygame.image.load('textures/bush.png')

    rect_in = bush.get_rect()
    new_x = rect_in.width // 8
    new_y = rect_in.height // 8
    bush = pygame.transform.scale(bush, (new_x, new_y))

    bushes_count = 10
    step = height // bushes_count
    for i in range(bushes_count - 2):
        screen.blit(bush, [width - width // 10, step * i])

    # sun counter:
    suncounter_bg = pygame.image.load('textures/suncounter_bg.png')
    rect_in = suncounter_bg.get_rect()
    new_x = rect_in.width // 2
    new_y = rect_in.height // 2.5
    suncounter_bg = pygame.transform.scale(suncounter_bg, (new_x, new_y))
    screen.blit(suncounter_bg, [10, 5])

    sun = pygame.image.load('textures/sun.png')
    rect_in = sun.get_rect()
    new_x = rect_in.width // 5
    new_y = rect_in.height // 5
    sun = pygame.transform.scale(sun, (new_x, new_y))
    screen.blit(sun, [25, 15])

    # shovel:
    shovel = pygame.image.load('textures/shovel.png')
    rect_in = shovel.get_rect()
    new_x = rect_in.width // 5
    new_y = rect_in.height // 5
    shovel = pygame.transform.scale(shovel, (new_x, new_y))
    screen.blit(shovel, [width - new_x, height - new_y])


def set_sun_counter(screen, count):
    font = pygame.font.Font(None, 40)
    text = font.render(str(count), True, (175, 64, 50))
    screen.blit(text, (90, 20))


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


def create_zombie_column(count, type, board_pos, cell_size, width, sheet, sheet_xy, group):
    coords = generate_zombie_coords(board_pos[1], cell_size, width, count)
    for i in range(count):
        if type == 'default':
            zombie = ZombieDefault(sheet, sheet_xy[0], sheet_xy[1], coords[i], board_pos[0], group)
        elif type == 'grass':
            zombie = Zombie1(sheet, sheet_xy[0], sheet_xy[1], coords[i], board_pos[0], group)
        elif type == 'woman':
            zombie = ZombieWoman(sheet, sheet_xy[0], sheet_xy[1], coords[i], board_pos[0], group)
        else:
            print(f"WRONG PARAM {type}: at func create_zombie_column")
        print(zombie.hp)

def create_plant(pos, tops, cell_size, all_player_sprites):
    a = pos[0] * cell_size + tops[0]
    b = pos[1] * cell_size + tops[1]
    player = Player(load_image("textures\shooter3.png"), 5, 1, a, b)
    all_player_sprites.add(player)


def load_zombie_pic(type):
    if type == 'default':
        zombie = pygame.image.load('textures/zombiedefault_walk6.png')
        rect_in = zombie.get_rect()
        new_x, new_y = rect_in.width // 1.5, rect_in.height // 1.7
        zombie = pygame.transform.scale(zombie, (new_x, new_y))
    elif type == 'grass':
        zombie = pygame.image.load('textures/zombie1_walk7.png')
        rect_in = zombie.get_rect()
        new_x, new_y = rect_in.width // 1.5, rect_in.height // 1.5
        zombie = pygame.transform.scale(zombie, (new_x, new_y))
    elif type == 'woman':
        zombie = pygame.image.load('textures/zombiewoman_walk5.png')
        rect_in = zombie.get_rect()
        new_x, new_y = rect_in.width // 3, rect_in.height // 3
        zombie = pygame.transform.scale(zombie, (new_x, new_y))
    else:
        print(f"WRONG PARAM {type}: at func load_zombie_pic")
        return None
    return zombie


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
