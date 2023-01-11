import pygame
from objects import Board
from functions import *
from random import randint


def reg_screen(width, height):
    size = width, height
    screen = pygame.display.set_mode(size)

    # pygame.display.set_caption('Plants VS Zombies')
    # screen.fill((0, 0, 0))
    # pygame.display.flip()

    username = ''
    dx = -1
    x = 50
    radius1, radius2 = 10, 10
    checked = False

    im = pygame.image.load('textures/KrInGeZaStAvKaNoEyEs.png')
    imb = pygame.image.load('textures/KrInGeBaCkG.jfif')
    iml = pygame.image.load('textures/KrInGeChIcKL.png')
    imr = pygame.image.load('textures/KrInGeChIcKR.png')

    imb = pygame.transform.scale(imb, (1067, 600))
    imr = pygame.transform.scale(imr, (820 // 3, 548 // 3))
    iml = pygame.transform.scale(iml, (820 // 3, 548 // 3))

    running = True
    while running:
        screen.fill((0, 0, 255))
        screen.blit(imb, (0, 0))
        screen.blit(im, (0, 0))

        x += dx

        if x + dx > 600 - 820 // 3 or x + dx < 0:
            dx *= -1
        if dx == 1:
            screen.blit(imr, (x, 430))
        else:
            screen.blit(iml, (x, 430))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if CheckWhereClicked(mouse_position):
                    checked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if username != '':
                        return [username, addUser(username)]
                    checked = False
                elif checked:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if len(username) <= 10:
                            username += event.unicode

        color = (randint(100, 255), randint(100, 255), randint(100, 180))
        radius1 += (dx * 0.03)
        radius2 -= (dx * 0.02)

        draw(screen, color)
        DrawWheels(screen, radius1, radius2)
        Registration(screen)
        WriteText(screen, username, color)

        pygame.display.flip()
    pygame.quit()


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
    all_player_sprites = pygame.sprite.Group()

    board = Board(9, 5)
    board_left, board_top, cell_size = width // 4.4, height // 5, width // 13
    board.set_view(board_left, board_top, cell_size)
    dark_cell = pygame.Surface((cell_size - 1, cell_size - 1))
    dark_cell.fill((0, 0, 0))
    dark_cell.set_alpha(75)

    clock = pygame.time.Clock()

    is_motion_on_cell = False
    sun_counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not(board.check_if_occupied(event.pos)):
                    if sun_counter >= 50:
                        board.occupied(event.pos)
                        create_plant(board.get_cell(event.pos), (board_left, board_top), cell_size, all_player_sprites)
                        sun_counter -= 50

                # types: default, grass, woman
                create_zombie_column(1, 'default', board, cell_size, width,
                                     load_zombie_pic('default'), (6, 1), zombies_group)
                # create_zombie_column(1, 'grass', board, cell_size, width,
                #                      load_zombie_pic('grass'), (6, 1), zombies_group)
                # create_zombie_column(1, 'woman', board, cell_size, width,
                #                      load_zombie_pic('woman'), (6, 1), zombies_group)
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
        all_player_sprites.update()
        all_player_sprites.draw(screen)

        decorations(screen, width, height)

        set_sun_counter(screen, int(sun_counter))
        if sun_counter < 9999:
            sun_counter += 0.5

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
