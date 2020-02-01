import pygame
import consts
import sys
from game_manager import GameManager
from snake import Snake


def main():
    pygame.init()
    screen = pygame.display.set_mode((consts.height, consts.width))
    screen.fill(consts.back_color)
    game = GameManager(consts.table_size, screen, consts.sx,
                       consts.sy, consts.block_cells)
    snakes = list()
    for snake in consts.snakes:
        print(snake)
        snakes.append(Snake(snake['keys'], game, (snake['sx'],
                                                  snake['sy']), snake['color'], snake['head_color'], snake['direction']))
    temp = True
    while temp:
        events = pygame.event.get()
        keys = []
        for event in events:
            if event.type == pygame.QUIT:
                temp = False
            if event.type == pygame.KEYDOWN:
                keys.append(event.unicode)
        if not game.handle(keys):
            font1 = pygame.font.SysFont("freesansbold", 100)
            text1 = font1.render("GAME OVER", True, (255, 0, 0))
            font2 = pygame.font.SysFont("comicsansms", 50)
            text2 = font2.render(
                "score: "+str(snakes[0].score), True, (0, 0, 155))
            screen.blit(text1, (390 - text1.get_width() //
                                2, 355 - text1.get_height() // 2))
            screen.blit(text2, (390 - text2.get_width() //
                                2, 425 - text2.get_height() // 2))
            pygame.display.flip()
        pygame.time.wait(250)


if __name__ == '__main__':
    main()
