import pygame
from utils import resource_path
pygame.init()


class playerObj:
    def __init__(self, display):
        self.display = display
        self.x = 200
        self.y = 500
        self.velY = 0
        self.velX = 0
        self.jumpForce = 6
        self.jump = False
        self.movePLatform = False
        self.yAtjump = 0
        self.left = False
        self.right = False
        self.dead = False
        self.sprite = pygame.image.load(resource_path('assets\\player.png'))
        
    def draw(self):
        self.display.blit(self.sprite, (self.x, self.y))
        pygame.draw.rect(self.display, (255, 0, 0), (self.x, self.y+self.sprite.get_height(), 50, 2))
    def move(self):
        if not self.dead: # Movement math
            self.x += self.velX
            self.y += self.velY
            self.velY += 0.2
            self.velX = 0
        
        if self.right and not self.dead: 
            self.velX = 3
        
        if self.left and not self.dead:
            self.velX = -3
        
        # Edge teleportation (IDK how this mechanic is named lmao)
        if self.x >= 403:
            self.x = -20
        if self.x <=-22:
            self.x = 400
        
        if self.y >= 600:
            self.dead = True
        
        if self.jump and not self.dead:
            self.velY = 0.2 
            self.velY -= self.jumpForce
        
        # Stop the jump
        if self.y <450:
            self.jump = False
        # Move the platforms
        if self.y < 350:
            self.movePLatform = True
        else:
            self.movePLatform = False