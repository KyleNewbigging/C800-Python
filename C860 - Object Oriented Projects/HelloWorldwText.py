import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((400,400))

WHITE = [255,255,255]
GREEN = [10,200,10]

quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
    text = font.render('Hello World', True, GREEN)
    textRect = text.get_rect(center = (200, 200))
    screen.blit(text,textRect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    
    pygame.display.update()

pygame.quit()