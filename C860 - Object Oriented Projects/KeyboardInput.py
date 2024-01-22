import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((400,400))

WHITE = [255,255,255]
GREEN = [10,200,10]
BLUE = [10,10,200]
RED = [200,10,10]

myText = "start"

quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
    text = font.render(myText, True, GREEN)
    textRect = text.get_rect(center = (200, 200))
    screen.blit(text,textRect)

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
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                myText = "RIGHT"
    
    pygame.display.update()

pygame.quit()