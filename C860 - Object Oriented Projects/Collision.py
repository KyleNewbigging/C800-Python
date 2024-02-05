import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((400,400))

FPS = 30
fpsClock = pygame.time.Clock()

WHITE = [255,255,255]
GREEN = [10,200,10]
BLUE = [10,10,200]
RED = [200,10,10]

myText = "start"

green_x = 80
show = True

quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
    text = font.render(myText, True, GREEN)
    textRect = text.get_rect(center = (200, 100))
    screen.blit(text,textRect)

    if show:
        red_rect = pygame.draw.rect(screen, RED, (250,300,50,50))
        green_rect = pygame.draw.rect(screen, GREEN, (green_x,315,30,30))

    if green_rect.colliderect(red_rect):
        show = False
    else:
        green_x +=2

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
    
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()