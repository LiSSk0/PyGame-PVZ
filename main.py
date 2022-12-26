import pygame
from objects import Board


SIZE = WIDTH, HEIGHT = 1100, 600
# SIZE = WIDTH, HEIGHT = 550, 300
BACK_COLOR = 'darkgreen'
COLORS = {0: (0, 0, 0), 1: (255, 0, 0), 2: (0, 0, 255)}
FPS = 40

pygame.init()
screen = pygame.display.set_mode(SIZE)

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


def decorations():
    bush = pygame.image.load('textures/bush.png')

    rect_in = bush.get_rect()
    new_x = rect_in.width // 8
    new_y = rect_in.height // 8
    bush = pygame.transform.scale(bush, (new_x, new_y))

    bushes_count = 10
    step = HEIGHT // bushes_count

    for i in range(bushes_count - 2):
        screen.blit(bush, [WIDTH - WIDTH // 10, step * i])


def main():
    screen.fill(BACK_COLOR)

    board = Board(9, 5)
    board_left, board_top, cell_size = WIDTH // 4.5, HEIGHT // 7, WIDTH // 13
    board.set_view(board_left, board_top, cell_size)
    dark_cell = pygame.Surface((cell_size - 1, cell_size - 1))
    dark_cell.fill((0, 0, 0))
    dark_cell.set_alpha(75)

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

        board.render(screen)
        if is_motion_on_cell:
            screen.blit(dark_cell, (board_left + cell_coord[0] * cell_size, board_top + cell_coord[1] * cell_size))

        decorations()

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
