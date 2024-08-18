import sys
import pygame
from pygame.locals import *
from plat import platform
from player import playerObj
from utils import collisions
from random import randint as rd

def main():

    pygame.init()
    fps = 60
    fpsClock = pygame.time.Clock()
    width, height = 400, 600
    display = pygame.display.set_mode((width, height))
    plat1 = platform(display, 200, 550)
    plat2 = platform(display)
    plat3 = platform(display)
    plat4 = platform(display)
    plat5 = platform(display)
    plat6 = platform(display)
    plat7 = platform(display)
    platforms = (plat1, plat2, plat3, plat4, plat5, plat6, plat7)
    player = playerObj(display)
    lowestY = player.y
    pygame.display.set_icon(player.sprite)


    # Game loop.
    while True:
        display.fill((255, 255, 255))        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_LEFT:
                player.left = True
            if event.type == pygame.KEYUP and event.key == K_LEFT:
                player.left = False
            if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
                player.right = True
            if event.type == pygame.KEYUP and event.key == K_RIGHT:
                player.right = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # Update.
        
        pygame.draw.line(display, (0,0,0), (10, 0), (10, height))
        pygame.draw.line(display, (0,0,0), (width-10, 0), (width-10, height))
        
        plat2.firstSpawn(plat1)
        plat3.firstSpawn(plat2)
        plat4.firstSpawn(plat3)
        plat5.firstSpawn(plat4)
        plat6.firstSpawn(plat5)
        plat7.firstSpawn(plat6)
        
        # Platforms
        for x in platforms:
            x.draw()
            if player.movePLatform:
                x.move()       
        
        # Player
        player.draw()
        player.move()
        if player.y < lowestY:
            lowestY = player.y
        print(f"{lowestY}")
        
        # Collisions
        for x in platforms:
            if collisions(player.x, player.y+player.sprite.get_height(), player.sprite.get_width(), 1, x.x, x.y, 50, 12) and player.velY > 0:
                player.jump = True
                player.yAtjump = player.y
                player.velY = 0
        
        # Draw.
        
        pygame.display.flip()
        fpsClock.tick(fps)

main()