import pygame
import random
pygame.init()
pygame.display.set_caption("Game TITLE")
screen = pygame.display.set_mode(((800,800)))
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
x_position= 300
y_position = 300
speed = 2
direction = 1
quitVar = True
while quitVar == True:
    screen.fill(GREEN)
    red_rect = pygame.draw.rect(screen, RED,(x_position,y_position,50,50))
    keys_pressed = pygame.key.get_pressed()
    if direction == 0:
        if keys_pressed[pygame.K_a]:
            direction = 3
        elif keys_pressed[pygame.K_d]:
            direction = 1
        y_position -= speed
    elif direction == 1:
        if keys_pressed[pygame.K_w]:
            direction = 0
        elif keys_pressed[pygame.K_s]:
            direction = 2
        x_position += speed
    elif direction == 2:
        if keys_pressed[pygame.K_d]:
            direction = 1
        elif keys_pressed[pygame.K_a]:
            direction = 3
        y_position += speed
    elif direction == 3:
        if keys_pressed[pygame.K_w]:
            direction = 0
        elif keys_pressed[pygame.K_s]:
            direction = 2
        x_position -= speed
    print(direction)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
pygame.quit()