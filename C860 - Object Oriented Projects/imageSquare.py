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

quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    
    screen.blit(image,(x_image,y_image))
    if state == 0:
        x_image += velocity
        if(x_image > (400-image.get_width())):
            state = 1
    elif state == 1:
        y_image += velocity
        if(y_image > (400-image.get_height())):
            state = 2
    elif state == 2:
        x_image -= velocity
        if(x_image < 0):
            state = 3
    elif state == 3:
        y_image -= velocity
        if(y_image < 0):
            state = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()