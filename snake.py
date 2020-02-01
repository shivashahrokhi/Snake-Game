import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, head_color, direction):
        self.score = 0
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.head_color = head_color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        x = [self.get_head()[0] + Snake.dx[self.direction],
             self.get_head()[1] + Snake.dy[self.direction]]
        x[0] = self.val(x[0])
        x[1] = self.val(x[1])
        if self.game.cells[x[0]][x[1]].color == consts.back_color:
            self.cells.append(tuple(x))
            for X in self.cells:
                self.game.cells[X[0]][X[1]].set_color(self.color)
            self.game.cells[self.cells[-1][0]
                            ][self.cells[-1][1]].set_color(self.head_color)
            self.game.cells[self.cells[0][0]][self.cells[0]
                                              [1]].set_color(consts.back_color)
            del self.cells[0]
        elif self.game.cells[x[0]][x[1]].color == consts.fruit_color:
            self.cells.append(tuple(x))
            for X in self.cells:
                self.game.cells[X[0]][X[1]].set_color(self.color)
            self.game.cells[self.cells[-1][0]
                            ][self.cells[-1][1]].set_color(self.head_color)
            self.game.cells[self.game.get_next_fruit_pos()[0]][self.game.get_next_fruit_pos()[
                1]].set_color(consts.fruit_color)
            self.score += 1
        else:
            self.game.kill(self)

    def handle(self, keys):
        D = {"UP": 1, "DOWN": -1, "RIGHT": 2, "LEFT": -2}
        for x in keys:
            if x in self.keys:
                if D[self.keys[x]] != (-1)*D[self.direction]:
                    self.direction = self.keys[x]
