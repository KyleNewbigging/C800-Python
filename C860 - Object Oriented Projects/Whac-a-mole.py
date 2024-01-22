import pygame
import random

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((400,400))

image = pygame.image.load("diglett.png")
image = pygame.transform.scale(image,(50,50))


FPS = 30
fpsClock = pygame.time.Clock()

WHITE = [255,255,255]
GREEN = [10,200,10]
BLUE = [10,10,200]
RED = [200,10,10]


x = 200
y = 200
myText = "Score: "
score = 0
generated = False
quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
    text = font.render("Score: "+str(score), True, GREEN)
    textRect = text.get_rect(center = (200, 60))
    screen.blit(text,textRect)

    if(not generated):
        x = random.randint(30,370)
        y = random.randint(30,370)
        generated = True

    imageRect = image.get_rect()
    imageRect.center = (x,y)
    screen.blit(image,imageRect) 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myText = "SPACE"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                myText = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                myText = "DOWN"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                myText = "LEFT"
                green_x -= 6
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                myText = "RIGHT"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(imageRect.collidepoint(pygame.mouse.get_pos())):
                myText = "Clicked"
                generated = False
                score += 1
    
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()