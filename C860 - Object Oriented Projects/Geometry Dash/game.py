import pygame
from config import Config
from spike import Spike
class Game:
    def __init__(self,screen,screenState):
        self.screen = screen
        self.gameLoop = True
        self.screenState = screenState
    def loop(self):
        x_position= int(Config["game"]["width"])/2
        gameWidth = int(Config["game"]["width"])
        gameHeight = int(Config["game"]["height"])
        level = 1
        y_position = 430
        playerSpeed = 0
        playerAcceleration = 1
        scrollSpeed = 6
        scrollPosition = 0
        jumpForce = -15
        isGrounded = True
        obstaclesLvl1 = [Spike(self.screen,750,430),Spike(self.screen,1500,430),Spike(self.screen,2250,430),Spike(self.screen,2275,430)]
        portal1 = pygame.image.load("portal.png")
        direction = 0
        score = 0
        speed = int(Config['snake']['speed'])
        block = pygame.image.load("block.png")
        clock = pygame.time.Clock()
        #0 is start
        #1 is playing
        #2 is game over
        while self.gameLoop == True:
            clock.tick(60)
            if self.screenState == 0:
                buttonHeight =75
                buttonWidth = 200
                buttonX = 400-buttonWidth/2
                buttonY = 400-buttonHeight/2
                buttonColour = Config['colours']['black']
                buttonRect = pygame.Rect(buttonX,buttonY,buttonWidth,buttonHeight)
                self.screen.fill(Config['colours']['red'])
                title = "Geometry Dash"
                font = pygame.font.Font("./PressStart2P.ttf", 50)
                titleFont = font.render(title, True, Config["colours"]["black"])
                textRect = titleFont.get_rect(center = (int(Config['game']['width'])/2,int(Config['game']['width'])/4))
                #button = pygame.draw.rect(self.screen, Config["colours"]["black"],)
                self.screen.blit(titleFont, textRect)
                pygame.draw.rect(self.screen,buttonColour,buttonRect,5)
                pygame.draw.polygon(self.screen,buttonColour,[(385,380),(385,420),(420,400)])
                x, y = pygame.mouse.get_pos()
                if x > 300 and x < 500:
                    if y > 365 and y < 435:
                        if any(pygame.mouse.get_pressed()):
                            self.screenState = 1

            elif self.screenState == 1:
                keys_pressed = pygame.key.get_pressed()
                regular_block = pygame.transform.scale(block,(50,50))
                if level == 1:
                    self.screen.fill(Config['colours']['green'])
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,480 , 850, 120))
                    portal1 = pygame.transform.scale(portal1,(100,200))
                    for spike in obstaclesLvl1:
                        spike.draw(scrollPosition)
                        if spike.checkCollision(regular_block,scrollPosition,y_position):
                            scrollPosition = 0
                    self.screen.blit(portal1,(4000-scrollPosition,280))
                    if regular_block.get_rect(x=50,y=y_position).colliderect(portal1.get_rect(x=4000-scrollPosition,y=280)):
                            scrollPosition = 0
                            level = 2
                elif level == 2:
                    self.screen.fill(Config['colours']['apple-red'])
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,480 , 850, 120))
                    portal1 = pygame.transform.scale(portal1,(100,200))
                    for spike in obstaclesLvl1:
                        spike.draw(scrollPosition)
                        if spike.checkCollision(regular_block,scrollPosition,y_position):
                            scrollPosition = 0
                    self.screen.blit(portal1,(4000-scrollPosition,280))
                    if regular_block.get_rect(x=50,y=y_position).colliderect(portal1.get_rect(x=4000-scrollPosition,y=280)):
                            scrollPosition = 0
                            self.screenState = 2
                self.screen.blit(regular_block,(50,y_position))
                if (keys_pressed[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and isGrounded:
                    playerSpeed = jumpForce
                    isGrounded = False
                    print("jumped")
                if isGrounded == False:
                    playerSpeed += playerAcceleration
                else:
                    playerSpeed = 0
                y_position += playerSpeed
                if y_position >= 430:
                    y_position = 430
                    isGrounded = True
                scrollPosition += scrollSpeed
                print(y_position)
            elif self.screenState == 2:
                buttonHeight =75
                buttonWidth = 200
                buttonX = 400-buttonWidth/2
                buttonY = 315-buttonHeight/2
                buttonColour = Config['colours']['black']
                buttonRect = pygame.Rect(buttonX,buttonY,buttonWidth,buttonHeight)
                self.screen.fill(Config['colours']['red'])
                title = "Nice"
                font = pygame.font.Font("./PressStart2P.ttf", 50)
                titleFont = font.render(title, True, Config["colours"]["black"])
                textRect = titleFont.get_rect(center = (int(Config['game']['width'])/2,int(Config['game']['width'])/5))
                #button = pygame.draw.rect(self.screen, Config["colours"]["black"],)
                self.screen.blit(titleFont, textRect)
                pygame.draw.rect(self.screen,buttonColour,buttonRect,5)
                pygame.draw.polygon(self.screen,buttonColour,[(385,295),(385,335),(420,315)])
                buttonX = 400-buttonWidth/2
                buttonY = 435-buttonHeight/2
                buttonRect2 = pygame.Rect(buttonX,buttonY,buttonWidth,buttonHeight)
                pygame.draw.rect(self.screen,buttonColour,buttonRect2,5)
                title2 = "QUIT"
                font = pygame.font.Font("./PressStart2P.ttf", 25)
                titleFont2 = font.render(title2, True, Config["colours"]["black"])
                textRect2 = titleFont2.get_rect(center = (400,435))
                self.screen.blit(titleFont2, textRect2)
                x, y = pygame.mouse.get_pos()
                print(x,y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameLoop = False
            pygame.display.update()
        pygame.quit()
    def gameOver(self):
        self.screenState = 2