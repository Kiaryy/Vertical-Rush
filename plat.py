import pygame
from random import randint as rd
pygame.init()
class platform:
    def __init__(self, display, x=0, y=0):
        self.x = x
        self.y = y
        self.display = display
        self.flag = True
    
    def firstSpawn(self, platform=None):
        if platform != None and self.flag:
            while True:
                self.x = rd(25, 325)
                self.y = rd(platform.y-100, platform.y-50)
                if (self.x+50 <= 340 and self.y+25 <= 590) and (self.x >= 0):
                    break
            self.flag = False
            print(f"{self.x} {self.y}")
    
    def draw(self):
        pygame.draw.rect(self.display, (0, 155, 150), (self.x, self.y, 50, 10))
        pygame.draw.rect(self.display, (255, 0, 0), (self.x, self.y, 50, 2))
    
    def move(self):
        self.y += 2
        if self.y > 605:
            self.y = -25
            self.x = rd(25, 325)