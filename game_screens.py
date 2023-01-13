import pygame
import os
from objects import Board
from functions import *
from random import randint, choice


# Завершение программы
def terminate():
    pygame.quit()
    sys.exit()


# Экран регистрации
def reg_screen(width, height):
    size = width, height
    screen = pygame.display.set_mode(size)

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

    color_counter = 0
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
                terminate()
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

        if color_counter % 100 == 0:
            color = (randint(100, 255), randint(100, 255), randint(100, 180))
            color_counter //= 100
        color_counter += 1

        radius1 += (dx * 0.03)
        radius2 -= (dx * 0.02)

        draw(screen, color)
        DrawWheels(screen, radius1, radius2)
        Registration(screen)
        WriteText(screen, username, color)

        pygame.display.flip()


# Экран меню выбора уровней
def menu_screen(fps, username):
    size = width, height = 1100, 600
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode(size)

    screen.fill('darkblue')
    menu_bg = pygame.image.load('textures/menu_background.png')
    menu_bg = pygame.transform.scale(menu_bg, (width, height))
    screen.blit(menu_bg, [0, 0])

    button = pygame.image.load('textures/button.png')
    button_size = (275, 90)
    button = pygame.transform.scale(button, button_size)
    font = pygame.font.Font(None, 40)

    level = check_level(username)

    if level >= 1:
        text_lvl1 = font.render(str("Level 1"), True, (150, 0, 200))
        coords_lvl1 = (width // 2 - button_size[0] // 2, 0)
        screen.blit(button, [*coords_lvl1])
        screen.blit(text_lvl1, (width // 2 - text_lvl1.get_width() // 2, button_size[1] // 2.65))
    if level >= 2:
        text_lvl2 = font.render(str("Level 2"), True, (150, 0, 200))
        coords_lvl2 = (width // 2 - button_size[0] // 2, 125)
        screen.blit(button, [*coords_lvl2])
        screen.blit(text_lvl2, (width // 2 - text_lvl2.get_width() // 2, button_size[1] // 2.65 + 125))
    if level >= 3:
        text_lvl3 = font.render(str("Level 3"), True, (150, 0, 200))
        coords_lvl3 = (width // 2 - button_size[0] // 2, 250)
        screen.blit(button, [*coords_lvl3])
        screen.blit(text_lvl3, (width // 2 - text_lvl3.get_width() // 2, button_size[1] // 2.65 + 250))
    if level >= 4:
        text_lvl4 = font.render(str("Level 4"), True, (150, 0, 200))
        coords_lvl4 = (width // 2 - button_size[0] // 2, 375)
        screen.blit(button, [*coords_lvl4])
        screen.blit(text_lvl4, (width // 2 - text_lvl4.get_width() // 2, button_size[1] // 2.65 + 375))
    if level >= 5:
        text_lvl5 = font.render(str("Level 5"), True, (150, 0, 200))
        coords_lvl5 = (width // 2 - button_size[0] // 2, 500)
        screen.blit(button, [*coords_lvl5])
        screen.blit(text_lvl5, (width // 2 - text_lvl5.get_width() // 2, button_size[1] // 2.65 + 500))

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if level >= 1 and \
                   coords_lvl1[0] <= x <= coords_lvl1[0] + button_size[0] and \
                   coords_lvl1[1] <= y <= coords_lvl1[1] + button_size[1]:
                    return 1
                if level >= 2 and \
                   coords_lvl2[0] <= x <= coords_lvl2[0] + button_size[0] and \
                   coords_lvl2[1] <= y <= coords_lvl2[1] + button_size[1]:
                    return 2
                if level >= 3 and \
                   coords_lvl3[0] <= x <= coords_lvl3[0] + button_size[0] and \
                   coords_lvl3[1] <= y <= coords_lvl3[1] + button_size[1]:
                    return 3
                if level >= 4 and \
                   coords_lvl4[0] <= x <= coords_lvl4[0] + button_size[0] and \
                   coords_lvl4[1] <= y <= coords_lvl4[1] + button_size[1]:
                    return 4
                if level >= 5 and \
                   coords_lvl5[0] <= x <= coords_lvl5[0] + button_size[0] and \
                   coords_lvl5[1] <= y <= coords_lvl5[1] + button_size[1]:
                    return 5

            # if event.type == pygame.MOUSEMOTION:
            #     x, y = event.pos
            #     if coords_lvl1[0] <= x <= coords_lvl1[0] + button_size[0] and \
            #        coords_lvl1[1] <= y <= coords_lvl1[1] + button_size[1]:
            #         motion_on_button = 1

        clock.tick(fps)
        pygame.display.flip()


# Экран уровня
def level_screen(screen, width, height, fps, level):
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

    zombie_count = {
        'default': level.default_cnt,
        'woman': level.woman_cnt,
        'grass': level.grass_cnt
    }

    clock = pygame.time.Clock()

    is_motion_on_cell = False
    sun_counter = 0
    counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not(board.check_if_occupied(event.pos)):
                    if sun_counter >= 50:
                        board.occupied(event.pos)
                        create_plant(board.get_cell(event.pos), (board_left, board_top), cell_size, all_player_sprites)
                        sun_counter -= 50

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

        types = ['default', 'woman', 'grass']
        if counter % 500 == 0:
            if (zombie_count['default'] + zombie_count['woman'] + zombie_count['grass']) > 0:
                type = choice(types)
                while zombie_count[type] == 0:
                    type = choice(types)
                create_zombie_column(1, type, board, cell_size, width,
                                     load_zombie_pic(type), (6, 1), zombies_group)
                zombie_count[type] -= 1
            else:
                # when zombies had ended
                pass
            counter //= 500
        counter += 1

        decorations(screen, width, height)

        set_sun_counter(screen, int(sun_counter))
        if sun_counter < 9999:
            sun_counter += 0.1

        clock.tick(fps)
        pygame.display.flip()
