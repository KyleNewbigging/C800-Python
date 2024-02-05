import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((400,400))

FPS = 30
fpsClock = pygame.time.Clock()


BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [10,200,10]
BLUE = [10,10,200]
RED = [200,10,10]
YELLOW = [255,225,0]

image = pygame.image.load("zebralogoCircle.png")
x_image = 0
y_image = 0

state = 0

velocity = 10

border_radius = 0

quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, GREEN, (150,150,100,100), 0, border_radius)

    border_radius += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()