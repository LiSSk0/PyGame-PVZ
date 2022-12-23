import pygame


SIZE = WIDTH, HEIGHT = 1100, 600
BACK_COLOR = 'darkblue'
COLORS = {0: (0, 0, 0), 1: (255, 0, 0), 2: (0, 0, 255)}
FPS = 40

pygame.init()
screen = pygame.display.set_mode(SIZE)


def main():
    screen.fill(BACK_COLOR)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
