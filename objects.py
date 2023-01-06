import pygame

tile_images = {
    'grass1': pygame.image.load('textures/grass1.png'),
    'grass2': pygame.image.load('textures/grass2.png')
}


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        self.left = 10
        self.top = 10
        self.cell_size = 85

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        # rect_in = image.get_rect()
        # new_x = rect_in.width * 2
        # new_y = rect_in.height // 2
        grass1 = pygame.transform.scale(tile_images['grass1'], (self.cell_size - 2, self.cell_size - 2))
        grass2 = pygame.transform.scale(tile_images['grass2'], (self.cell_size - 2, self.cell_size - 2))

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

    def get_cell(self, mouse_pos):
        x, y = mouse_pos[0] - self.left, mouse_pos[1] - self.top
        if (x < 0) or (x > self.width * self.cell_size) or (y < 0) or (y > self.height * self.cell_size):
            return None
        else:
            return int(x) // self.cell_size, y // self.cell_size

    # def get_motion(self, mouse_pos):
    #     cell_coords = self.get_cell(mouse_pos)
    #     if cell_coords is not None:
    #         self.on_click(cell_coords)
    #
    # def on_click(self, cell_coords):
    #     return cell_coords


class ZombieDefault(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, pos, board_left, *group):
        super().__init__(*group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(pos[0], pos[1])
        self.border = board_left
        self.counter = 0

        self.hp = 50
        self.velocity = 3

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        if self.rect.x <= self.border:
            self.kill()
        else:
            if self.counter % 10 == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.counter //= 10
                self.rect.x -= self.velocity
            self.counter += 1


class Zombie1(ZombieDefault):
    def __init__(self, sheet, columns, rows, pos, board_left, *group):
        super().__init__(sheet, columns, rows, pos, board_left, *group)

        self.hp = 100