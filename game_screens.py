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
def reg_screen():
    size = width, height = 1100, 600
    screen = pygame.display.set_mode(size)

    username = ''
    dx = -1
    x = 50
    radius1, radius2 = 10, 10
    checked = False

    im = pygame.image.load('textures/reg_zombie.png')
    imb = pygame.image.load('textures/reg_bg.jfif')
    iml = pygame.image.load('textures/zombiebird_left.png')
    imr = pygame.image.load('textures/zombiebird_right.png')

    imb = pygame.transform.scale(imb, (1067, 600))
    imr = pygame.transform.scale(imr, (820 // 3, 548 // 3))
    iml = pygame.transform.scale(iml, (820 // 3, 548 // 3))

    color_counter = 0
    color = (0, 0, 0)
    top5 = top5users()

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
        top5Table(screen, width, height, top5)

        pygame.display.flip()


# Экран меню выбора уровней
def menu_screen(fps, username):
    size = width, height = 1100, 600
    screen = pygame.display.set_mode(size)

    screen.fill('darkblue')
    menu_bg = pygame.image.load('textures/menu_background.png')
    menu_bg = pygame.transform.scale(menu_bg, (width, height))
    screen.blit(menu_bg, [0, 0])

    zombie_pic = pygame.image.load('textures/zombiebird_left.png')
    zombie_pic = pygame.transform.scale(zombie_pic, (450, 300))
    zombie_pic.set_alpha(125)
    screen.blit(zombie_pic, (width - zombie_pic.get_width() + 50, height - zombie_pic.get_height()))
    tree_pic = pygame.image.load('textures/creepy_tree.png')
    tree_pic = pygame.transform.scale(tree_pic, (300, 550))
    screen.blit(tree_pic, (25, height // 6))

    button = pygame.image.load('textures/button.png')
    button_size = (275, 90)
    button = pygame.transform.scale(button, button_size)

    font = pygame.font.Font(None, 40)
    level = check_level(username) + 1
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

    nickname = str(username)
    if len(nickname) > 9:
        nickname = nickname[:8] + "..."
    text_username = font.render(str("Username: '" + nickname + "'"), True, (150, 0, 200))
    screen.blit(text_username, (10, 10))
    text_username = font.render(str("Completed levels: " + str(level - 1)), True, (150, 0, 200))
    screen.blit(text_username, (10, 50))

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

        clock.tick(fps)
        pygame.display.flip()


# Экран уровня
def level_screen(fps, level, username, cur_level):
    size = width, height = 1100, 600
    screen = pygame.display.set_mode(size)

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

    user_level = check_level(username)
    is_motion_on_cell = False
    is_level_already_increased = False
    end = 1  # -1 - ongoing, 0 - loss, 1 - win
    sun_counter = 0
    counter = 0

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end == -1:
                    if not(board.check_if_occupied(event.pos)):
                        if sun_counter >= 50:
                            board.occupied(event.pos)
                            create_plant(board.get_cell(event.pos), (board_left, board_top),
                                         cell_size, all_player_sprites)
                            sun_counter -= 50
                else:
                    return

            if event.type == pygame.MOUSEMOTION and end == -1:
                cell_coord = board.get_cell(event.pos)
                if cell_coord is not None:
                    is_motion_on_cell = True
                else:
                    is_motion_on_cell = False

        screen.blit(level_bg, [0, 0])

        if end == -1:
            board.render(screen)
            if is_motion_on_cell:
                screen.blit(dark_cell, (board_left + cell_coord[0] * cell_size, board_top + cell_coord[1] * cell_size))

            zombies_group.update()
            zombies_group.draw(screen)
            all_player_sprites.update()
            all_player_sprites.draw(screen)
            decorations(screen, width, height)

            types = ['default', 'woman', 'grass']
            if counter % 500 == 0:
                if (zombie_count['default'] + zombie_count['woman'] + zombie_count['grass']) > 0:
                    type = choice(types)
                    while zombie_count[type] == 0:
                        type = choice(types)
                    create_zombie_column(1, type, board, cell_size, width,
                                         load_zombie_pic(type), (6, 1), zombies_group)
                    zombie_count[type] -= 1
                else:  # when zombies have ended
                    if zombies_group.__len__() == 0:
                        end = 1
                counter //= 500
            counter += 1

            set_sun_counter(screen, int(sun_counter))
            if sun_counter < 9999:
                sun_counter += 0.1
        else:
            if end == 1:
                end_rect_color = (0, 200, 50)
                end_text = f"Win! Level {cur_level} completed."
                if not is_level_already_increased and cur_level > user_level:
                    increase_level(username)
                    is_level_already_increased = True
            elif end == 0:
                end_rect_color = (200, 0, 0)
                end_text = f"Loose! Level {cur_level} not completed."

            pygame.draw.rect(screen, end_rect_color, (0, height // 3, width, height // 3), 0)
            pygame.draw.rect(screen, (0, 0, 0), (0, height // 3, width, 5), 0)
            pygame.draw.rect(screen, (0, 0, 0), (0, height // 1.5, width, 5), 0)

            font1 = pygame.font.Font(None, 80)
            text1 = font1.render(str(end_text), True, (0, 0, 0))
            screen.blit(text1, (width // 2 - text1.get_width() // 2, height // 2 - text1.get_height() // 2 - 20))

            font2 = pygame.font.Font(None, 25)
            text2 = font2.render(str(f"*Click anywhere to continue*"), True, (0, 0, 0))
            screen.blit(text2, (width // 2 - text2.get_width() // 2, height // 2 - text2.get_height() // 2 + 50))

        clock.tick(fps)
        pygame.display.flip()
