import pygame

PLANT_HP = 150
TILE_IMG = {
    'grass1': pygame.image.load('textures/grass1.png'),
    'grass2': pygame.image.load('textures/grass2.png')
}

ball_image = pygame.image.load('textures/ball.png')
ball_image = pygame.transform.scale(ball_image, (610 // 18, 527 // 18))

# Игровое поле
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for i in range(height):
            self.board.append([])
            for j in range(width):
                self.board[i].append([0, 0])

        self.left = 10
        self.top = 10
        self.cell_size = 85

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        grass1 = pygame.transform.scale(TILE_IMG['grass1'], (self.cell_size - 2, self.cell_size - 2))
        grass2 = pygame.transform.scale(TILE_IMG['grass2'], (self.cell_size - 2, self.cell_size - 2))

        # board borders
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, 'white', (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                   self.cell_size, self.cell_size), 1)

        # board cells
        swap = True
        for y in range(self.height):
            for x in range(self.width):
                if swap:
                    screen.blit(grass1, (self.left + x * self.cell_size + 1, self.top + y * self.cell_size + 1))
                    swap = False
                else:
                    screen.blit(grass2, (self.left + x * self.cell_size + 1, self.top + y * self.cell_size + 1))
                    swap = True

    # Занять клетку растением
    def occupied(self, pos):
        try:
            a, b = self.get_cell(pos)
        except Exception:
            return
        self.board[b][a][1] = PLANT_HP

    # Проверка свободна ли клетка
    def check_if_occupied(self, pos):
        try:
            a, b = self.get_cell(pos)
        except Exception:
            return False
        if self.board[b][a][1] == 0:
            return False
        return True

    # Нанести урон растению в клетке
    def do_damage(self, pos, damage):
        a, b = self.get_cell(pos)
        if self.board[b][a][1] < damage:
            self.board[b][a][1] = 0  # cell is occupied so no exceptions
        else:
            self.board[b][a][1] -= damage

    # Получить координаты клетки
    def get_cell(self, mouse_pos):
        x, y = mouse_pos[0] - self.left, mouse_pos[1] - self.top
        if (x < 0) or (x > self.width * self.cell_size - 1) or (y < 0) or (y > self.height * self.cell_size - 1):
            return None
        else:
            return int(x) // self.cell_size, y // self.cell_size


# Главный класс зомби
class ZombieDefault(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, pos, board, *group):
        super().__init__(*group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(pos[0], pos[1])
        self.board = board
        self.border = board.left
        self.counter = 0

        self.hp = 50
        self.damage = 5
        self.velocity = 3

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def count_return(self):
        if self.counter % 25 == 0:
            return True
        return False

    def killing(self):
        if self.counter % 15 == 0:
            if self.hp > 12:
                self.hp -= 12

            else:
                self.kill()


    def update(self):
        if self.rect.x <= self.border:
            self.kill()
        else:
            if self.counter % 10 == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                if not self.board.check_if_occupied((self.rect.x, self.rect.y + self.image.get_height() // 2)):
                    self.rect.x -= self.velocity
                else:
                    self.board.do_damage((self.rect.x, self.rect.y + self.image.get_height() // 2), self.damage)
            self.counter += 1


# Вид зомби 1
class Zombie1(ZombieDefault):
    def __init__(self, sheet, columns, rows, pos, board_left, *group):
        super().__init__(sheet, columns, rows, pos, board_left, *group)

        self.hp = 100
        self.damage = 8


# Вид зомби 2
class ZombieWoman(ZombieDefault):
    def __init__(self, sheet, columns, rows, pos, board_left, *group):
        super().__init__(sheet, columns, rows, pos, board_left, *group)

        self.hp = 75
        self.damage = 10


# Класс пуль-шариков
class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, board, row, col,  top, left, sz,  zombie, *group):
        super().__init__(*group)
        self.sz = sz
        self.x, self.y = row, col
        self.top, self.left = top, left
        self.board = board
        self.screen = screen
        self.zombie = zombie


    def check(self):
        if self.x - 15 <= self.zombie.rect.x <= self.x + 15:
            self.kill()

    def update(self):
        self.screen.blit(ball_image, [self.x, self.y])
        self.x += 5
        self.check()


# Класс игрока для выставления растений
class Player(pygame.sprite.Sprite):
    def __init__(self, board, sheet, columns, rows, x, y, *players):
        super().__init__(*players)
        self.counter = 0
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.board = board

        self.hp = PLANT_HP
        self.damage = 12

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))



    def update(self):
        if not self.board.check_if_occupied((self.rect.x, self.rect.y + self.image.get_height() // 2)):
            self.kill()

        if self.counter % 15 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        self.counter += 1


# Класс игрового уровня
class Level:
    def __init__(self, zombies):
        self.default_cnt = zombies[0]
        self.woman_cnt = zombies[1]
        self.grass_cnt = zombies[2]
