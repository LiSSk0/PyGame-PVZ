import pygame
from functions import load_image

from random import randint

SIZE = W, H = 600, 600
FPS = 1

def draw(screen, color):
    font = pygame.font.Font(None, 35)
    text = font.render("Plants VS Zombies", True, color)
    text_w = text.get_width()
    text_h = text.get_height()
    # text_x = W // 2 - text.get_width() // 2
    # text_y = H // 2 - text.get_height() // 2
    text_x, text_y = 25, 345
    pygame.draw.rect(screen, '#663300', (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20))
    pygame.draw.rect(screen, '#00CCCC', (text_x - 10, text_y - 10,
                                         text_w + 20, text_h + 20), 3)

    screen.blit(text, (text_x, text_y))

def RegLizzaLoh(screen):
    font = pygame.font.Font(None, 27)
    pygame.draw.rect(screen, '#663300', (20, 20, 100, 23))
    pygame.draw.rect(screen, '#000000', (20, 20, 100, 23), 3)
    pygame.draw.rect(screen, '#AE604D', (20, 50, 200, 30))
    pygame.draw.rect(screen, '#000000', (20, 50, 200, 30), 3)
    text = font.render("Username:", True, '#33FF00')
    screen.blit(text, (22, 22))


def WriteText(screen, name, color):
    x, y = 25, 55
    font = pygame.font.Font(None, 27)
    text = font.render(name, True, color)
    screen.blit(text, (x, y))



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Plants VS Zombies')
    running = True
    screen.fill((0, 0, 0))
    pygame.display.flip()
    userName = ''
    dx = -1
    x = 50
    im = load_image('KrInGeZaStAvKaNoEyEs.png')
    imb = load_image('KrInGeBaCkG.jfif')
    iml = load_image('KrInGeChIcKL.png')
    imr = load_image('KrInGeChIcKR.png')

    imb = pygame.transform.scale(imb, (1067, 600))
    imr = pygame.transform.scale(imr, (820 // 3, 548 // 3))
    iml = pygame.transform.scale(iml, (820 // 3, 548 // 3))

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
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                #print(mouse_position)
            if event.type == pygame.KEYDOWN:
                if True:
                    if event.key == pygame.K_KP_ENTER:
                        userName = ''
                    elif event.key == pygame.K_BACKSPACE:
                        userName = userName[:-1]
                    else:
                        if len(userName) <= 10:
                            userName += event.unicode

        color = (randint(100, 255), randint(100, 255), randint(100, 180))


        draw(screen, color)
        RegLizzaLoh(screen)
        WriteText(screen, userName, color)
        pygame.display.flip()
    pygame.quit()
