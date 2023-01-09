import pygame
from objects import Board
from functions import *


def menu_screen(fps):
    size = width, height = 1100, 600
    screen = pygame.display.set_mode(size)

    screen.fill('darkblue')
    menu_bg = pygame.image.load('textures/menu_background.png')
    menu_bg = pygame.transform.scale(menu_bg, (width, height))
    screen.blit(menu_bg, [0, 0])

    button = pygame.image.load('textures/button.png')
    button_size = (275, 90)
    button = pygame.transform.scale(button, button_size)
    font = pygame.font.Font(None, 40)

    text_lvl1 = font.render(str("Level 1"), True, (150, 0, 200))
    coords_lvl1 = (width // 2 - button_size[0] // 2, 0)
    screen.blit(button, [*coords_lvl1])
    screen.blit(text_lvl1, (width // 2 - text_lvl1.get_width() // 2, button_size[1] // 2.65))

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if coords_lvl1[0] <= x <= coords_lvl1[0] + button_size[0] and \
                   coords_lvl1[1] <= y <= coords_lvl1[1] + button_size[1]:
                    return 1
            # if event.type == pygame.MOUSEMOTION:
            #     x, y = event.pos
            #     if coords_lvl1[0] <= x <= coords_lvl1[0] + button_size[0] and \
            #        coords_lvl1[1] <= y <= coords_lvl1[1] + button_size[1]:
            #         motion_on_button = 1

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


def level_screen(screen, width, height, fps):
    level_bg = pygame.image.load('textures/wallpaperlevel.png')
    screen.blit(level_bg, [0, 0])

    zombies_group = pygame.sprite.Group()

    board = Board(9, 5)
    board_left, board_top, cell_size = width // 4.4, height // 5, width // 13
    board.set_view(board_left, board_top, cell_size)
    dark_cell = pygame.Surface((cell_size - 1, cell_size - 1))
    dark_cell.fill((0, 0, 0))
    dark_cell.set_alpha(75)

    # zombie = pygame.image.load('textures/zombiedefault_walk5.png')
    # rect_in = zombie.get_rect()
    # new_x = rect_in.width // 1.5
    # new_y = rect_in.height // 1.5
    # zombie = pygame.transform.scale(zombie, (new_x, new_y))

    # zombie1 = ZombieSprite(zombie, 6, 1, coords[0], board_left, zombies_group)

    clock = pygame.time.Clock()

    is_motion_on_cell = False
    sun_counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # types: default, grass, woman
                create_zombie_column(1, 'default', (board_left, board_top), cell_size, width,
                                     load_zombie_pic('default'), (6, 1), zombies_group)
                create_zombie_column(1, 'grass', (board_left, board_top), cell_size, width,
                                     load_zombie_pic('grass'), (6, 1), zombies_group)
                create_zombie_column(1, 'woman', (board_left, board_top), cell_size, width,
                                     load_zombie_pic('woman'), (6, 1), zombies_group)
                # print(board.get_cell(event.pos))
            if event.type == pygame.MOUSEMOTION:
                cell_coord = board.get_cell(event.pos)
                if cell_coord is not None:
                    is_motion_on_cell = True
                else:
                    is_motion_on_cell = False

        screen.blit(level_bg, [0, 0])

        board.render(screen)
        if is_motion_on_cell:
            screen.blit(dark_cell, (board_left + cell_coord[0] * cell_size, board_top + cell_coord[1] * cell_size))

        zombies_group.update()
        zombies_group.draw(screen)

        decorations(screen, width, height)
        set_sun_counter(screen, int(sun_counter))
        if sun_counter < 9999:
            sun_counter += 0.1

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
