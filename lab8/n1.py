import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((200, 200, 200))

circle(screen, (255, 255, 0), (200, 200), 150)
rect(screen, (0, 0, 0), (125, 275, 150, 25))

circle(screen, (255, 0, 0), (125, 160), 30)
circle(screen, (255, 0, 0), (275, 160), 25)

circle(screen, (0, 0, 0), (125, 160), 10)
circle(screen, (0, 0, 0), (275, 160), 10)

polygon(screen, (0, 0, 0), [(80,75), (170,165),
                            (180,155), (90,65)])

k = 0.434
polygon(screen, (0, 0, 0), [(350,100), (200,165),
                            (200 - k*10,165 - 10), (350-k*10,90)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
