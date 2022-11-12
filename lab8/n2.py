import pygame
import pygame.draw as draw
from random import randint
import numpy as np
pygame.init()

FPS = 24
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

list_of_balls = []


def new_ball():
    '''создает новый шарик'''
    global list_of_balls
    rc = np.array([
        randint(100, 1100),
        randint(100, 800)
    ])
    v = np.array([
        randint(100, 200),
        randint(100, 200)
    ])
    v *= np.random.choice([-1, 1], (2))
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    list_of_balls.append([rc, r, v, color])
    draw.circle(screen, color, tuple(rc), r)


def move_balls(dt):
    '''передвижение шариков'''
    for ball in list_of_balls:
        move_ball(ball, dt)


def move_ball(ball, dt):
    '''движение шарика'''
    if wall_left(ball):
        mirror_left(ball)
    if wall_up(ball):
        mirror_up(ball)
    if wall_right(ball):
        mirror_right(ball)
    if wall_down(ball):
        mirror_down(ball)
    else:
        dr = ball[2]*dt
        dr = dr.astype(np.int64)
        ball[0] += dr


def wall_left(ball):
    '''подлетел ли шарик к левой стенке'''
    x = ball[0][0]
    r = ball[1]
    vx = ball[2][0]
    return (x - r < 0 and vx < 0)


def wall_up(ball):
    '''подлетел ли шарик к потолку'''
    y = ball[0][1]
    r = ball[1]
    vy = ball[2][1]
    return (y - r < 0 and vy < 0)


def wall_right(ball):
    '''подлетел ли шарик к правой стенке'''
    x = ball[0][0]
    r = ball[1]
    vx = ball[2][0]
    return (x + r > 1200 and vx > 0)


def wall_down(ball):
    '''подлетел ли шарик к полу'''
    y = ball[0][1]
    r = ball[1]
    vy = ball[2][1]
    return (y + r > 900 and vy > 0)


def mirror_left(ball):
    '''отражение шарика слева'''
    rc = ball[0]
    v = ball[2]
    r = ball[1]
    v *= np.array([-1, 1])
    rc[0] = r


def mirror_up(ball):
    '''отражение шарика от потолка'''
    rc = ball[0]
    v = ball[2]
    r = ball[1]
    v *= np.array([1, -1])
    rc[1] = r


def mirror_right(ball):
    '''отражение шарика справа'''
    rc = ball[0]
    v = ball[2]
    r = ball[1]
    v *= np.array([-1, 1])
    rc[0] = 1200 - r


def mirror_down(ball):
    '''отражение шарика от потолка'''
    rc = ball[0]
    v = ball[2]
    r = ball[1]
    v *= np.array([1, -1])
    rc[1] = 900 - r


def draw_ball(ball):
    '''рисует шарик из списка шариков'''
    draw.circle(
        screen,
        ball[3],
        ball[0],
        ball[1])


def check(event):
    '''проверка попадания по шарику'''
    global count
    check = False
    position_of_catched = None
    for i in range(len(list_of_balls)):
        ball = list_of_balls[i]
        rc = ball[0]
        r = ball[1]
        if ro(np.array(event.pos), rc) < r:
            check = True
            position_of_catched = i
        else:
            pass
    if check:
        print("yes")
        list_of_balls.pop(position_of_catched)
        new_ball()
        count += 1
    else:
        print("misclick")


def ro(coord1, coord2):
    '''расстояние между точками
с координатами coord1 и coord2'''
    return np.linalg.norm(coord1 - coord2)


def new_step(dt):
    '''обновляет изображение на экране'''
    move_balls(dt/1000)
    for ball in list_of_balls:
        draw_ball(ball)
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


count = 0
clock = pygame.time.Clock()
finished = False
new_ball()
new_ball()
while not finished:
    dt = clock.tick(FPS)
    catch_event()
    new_step(dt)
pygame.quit()
print(count)
