import math
import numpy as np
from random import choice

import pygame

WHITE = 0xFFFFFF
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

pygame.draw.line(
    screen,
    (0xFF0000),
    (20, 450),
    (50, 500),
    10)
