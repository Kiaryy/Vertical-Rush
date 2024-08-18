import sys
import pygame
from pygame.locals import *
from plat import platform

def main():

    pygame.init()
    fps = 60
    fpsClock = pygame.time.Clock()
    width, height = 400, 600
    display = pygame.display.set_mode((width, height))
    plat1 = platform(display, 200, 500)
    plat2 = platform(display)
    plat3 = platform(display)
    plat4 = platform(display)
    plat5 = platform(display)
    plat6 = platform(display)


    # Game loop.
    while True:
        display.fill((255, 255, 255))        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # Update.
        
        pygame.draw.line(display, (0,0,0), (10, 0), (10, height))
        pygame.draw.line(display, (0,0,0), (width-10, 0), (width-10, height))
        plat1.draw()
        plat1.move()
        plat2.firstSpawn(plat1)
        plat2.draw()
        plat2.move()
        plat3.firstSpawn(plat2)
        plat3.draw()
        plat3.move()
        plat4.firstSpawn(plat3)
        plat4.draw()
        plat4.move()
        plat5.firstSpawn(plat4)
        plat5.draw()
        plat5.move()
        plat6.firstSpawn(plat5)
        plat6.draw()
        plat6.move()
        # Draw.
        
        pygame.display.flip()
        fpsClock.tick(fps)

main()