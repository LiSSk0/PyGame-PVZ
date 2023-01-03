import pygame
from objects import Board
from functions import decorations, generate_zombie_coords, create_zombie_column


SIZE = WIDTH, HEIGHT = 1100, 600
# SIZE = WIDTH, HEIGHT = 550, 300
BACK_COLOR = 'darkgreen'
LEVEL_BG = pygame.image.load('textures/wallpaperlevel.png')
COLORS = {0: (0, 0, 0), 1: (255, 0, 0), 2: (0, 0, 255)}
FPS = 50

pygame.init()
screen = pygame.display.set_mode(SIZE)

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
zombies_group = pygame.sprite.Group()


def main():
    screen.fill(BACK_COLOR)
    screen.blit(LEVEL_BG, [0, 0])

    board = Board(9, 5)
    board_left, board_top, cell_size = WIDTH // 4.4, HEIGHT // 5, WIDTH // 13
    board.set_view(board_left, board_top, cell_size)
    dark_cell = pygame.Surface((cell_size - 1, cell_size - 1))
    dark_cell.fill((0, 0, 0))
    dark_cell.set_alpha(75)

    zombie = pygame.image.load('textures/zombie1_walk7.png')
    rect_in = zombie.get_rect()
    new_x = rect_in.width // 1.5
    new_y = rect_in.height // 1.5
    zombie = pygame.transform.scale(zombie, (new_x, new_y))

    # zombie1 = ZombieSprite(zombie, 6, 1, coords[0], board_left, zombies_group)
    # zombie2 = ZombieSprite(zombie, 6, 1, coords[1], board_left, zombies_group)
    # zombie3 = ZombieSprite(zombie, 6, 1, coords[2], board_left, zombies_group)
    create_zombie_column(2, board_top, board_left, cell_size, WIDTH, zombie, (6, 1), zombies_group)

    clock = pygame.time.Clock()

    is_motion_on_cell = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_cell(event.pos))
            if event.type == pygame.MOUSEMOTION:
                cell_coord = board.get_cell(event.pos)
                if cell_coord is not None:
                    is_motion_on_cell = True
                else:
                    is_motion_on_cell = False

        screen.fill(BACK_COLOR)
        screen.blit(LEVEL_BG, [0, 0])

        board.render(screen)
        if is_motion_on_cell:
            screen.blit(dark_cell, (board_left + cell_coord[0] * cell_size, board_top + cell_coord[1] * cell_size))

        zombies_group.update()
        zombies_group.draw(screen)

        decorations(screen, WIDTH, HEIGHT)

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
