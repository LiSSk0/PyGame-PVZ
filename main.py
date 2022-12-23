import pygame
from objects import Board


SIZE = WIDTH, HEIGHT = 1100, 600
BACK_COLOR = 'darkblue'
COLORS = {0: (0, 0, 0), 1: (255, 0, 0), 2: (0, 0, 255)}
FPS = 40

pygame.init()
screen = pygame.display.set_mode(SIZE)

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


def main():
    screen.fill(BACK_COLOR)

    board = Board(9, 5)
    board.set_view(WIDTH // 4, HEIGHT // 7, 85)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     board.get_click(event.pos)

        board.render(screen)

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
