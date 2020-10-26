import pygame
import random
import time
import numpy as np
from pygame.locals import *

import serial

ser = serial.Serial('COM4', 9600)
time.sleep(3)
print(" Olha o que chegou ")
textoEntrada = ser.readline()
print(textoEntrada)
# ser.close()


def collision(c1, c2):
    return ((c1[0] == c2[0]) and (c1[1] == c2[1]))


mat = np.zeros((8, 8))

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

clock = pygame.time.Clock()

pygame.init(),
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")

snake = [(700, 700), (600, 00)]
my_direction = LEFT
snake_body = pygame.Surface((100, 100))
snake_body.fill((255, 255, 255))

point = pygame.Surface((100, 100))
point.fill((255, 255, 255))
point_pos = (random.randint(0, 7)*100, random.randint(0, 7)*100)

while True:
    clock.tick(3)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], point_pos):
        point_pos = (random.randint(0, 7)*100, random.randint(0, 7)*100)
        snake.append((0, 0))

# Collision with yourself
    for i in range(1, len(snake)):
        if(snake[0] == snake[i]):
            snake = []
            pygame.time.delay(1000)
            snake = [(700, 700), (600, 00)]
            my_direction = LEFT
            break
# End map
    if(snake[0][0] < 0 or snake[0][0] > 800 or snake[0][1] < 0 or snake[0][1] > 800):
        snake = []
        pygame.time.delay(1000)
        snake = [(700, 700), (600, 00)]
        my_direction = LEFT

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 100)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 100, snake[0][1])
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 100)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 100, snake[0][1])

    screen.fill((0, 0, 0))
    mat = np.zeros((8, 8))
    i = int(point_pos[0]/100)
    j = int(point_pos[1]/100)
    mat[j][i] = 1
    for pos in snake:
        screen.blit(snake_body, pos)
        screen.blit(point, point_pos)
        i = int(pos[0]/100)
        j = int(pos[1]/100)
        mat[j][i] = 1

    pygame.display.update()
    ser.write(b'0001000000010001000100000001000000010000000100010001000000010000')
    time.sleep(2)
