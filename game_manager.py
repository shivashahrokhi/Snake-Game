import consts
from cell import Cell
import random


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        self.screen = screen
        self.alive = 1
        self.size = size
        self.cells = []
        self.sx = sx
        self.sy = sy
        self.snakes = list()
        self.turn = 0
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                tmp.append(Cell(screen, sx + i * consts.cell_size,
                                sy + j * consts.cell_size))
            self.cells.append(tmp)
        for cell in block_cells:
            self.get_cell(cell).set_color(consts.block_color)

    def add_snake(self, snake):
        self.snakes.append(snake)

    def get_cell(self, pos):
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def kill(self, killed_snake):
        self.snakes.remove(killed_snake)
        self.alive = 0
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].set_color([0, 0, 0])

    def get_next_fruit_pos(self):  # returns tuple (x, y) that is the fruit location

        x = random.randint(0, self.size-1)
        y = random.randint(0, self.size-1)
        while (self.get_cell((x, y)).color != consts.back_color):
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)

        ret = x, y

        return ret

    def handle(self, keys):
        for player in self.snakes:
            player.handle(keys)
            player.next_move()
        if self.turn == 0:
            pass
            self.cells[self.get_next_fruit_pos()[0]][self.get_next_fruit_pos()[
                1]].set_color(consts.fruit_color)
        self.turn += 1
        return self.alive
