import pygame
import pygame.draw as draw
from random import randint
pygame.init()

FPS = 0.5
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    draw.circle(screen, color, (x, y), r)


def ball_coord():
    '''координаты круга'''
    return (([x, y], r))


def check(event):
    '''проверка попадания'''
    x, y = ball_coord()[0]
    r = ball_coord()[1]
    if ro(event.pos, [x, y]) < r:
        print('yes')
    else:
        print('misclick')


def ro(coord1, coord2):
    '''расстояние между точками
с координатами coord1 и coord2'''
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1-x2)**2+(y1-y2)**2)**0.5


def game():
    global finished
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        catch_event()
        new_step()
    pygame.quit()


def new_step():
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)


def catch_event():
    '''проверяет, какое случилось событие
и принимает соответствующее решение'''
    global finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check(event)


game()
