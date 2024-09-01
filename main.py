import sys
import pygame
from pygame.locals import *
from plat import platform
from player import playerObj
from utils import collisions
from utils import resource_path
from random import randint as rd
from button import button



def main():
    # Initiation of modules
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    
    score_font = pygame.font.SysFont('Comic Sans MS', 15)
    score = 0
    high_score = 0
    menu_font = pygame.font.SysFont('Comic Sans MS', 30)
    
    
    jump_sound_effect = pygame.mixer.Sound(resource_path("assets\\jump.mp3"))
    
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
    plat8 = platform(display)
    platforms = (plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8)
    player = playerObj(display)
    lowestY = player.y
    pygame.display.set_icon(player.sprite)


    # Game loop.
    while True:
        display.fill((255, 255, 255))       
        text_surface = score_font.render(f'Score: {int(score)}', False, (0, 0, 0))
        display.blit(text_surface, (25,0))
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
        plat8.firstSpawn(plat7)
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
        
        if player.movePLatform:
            score +=0.1
        
        # Game over
        if player.dead:
            if score >= high_score:
                high_score = score
            game_over = menu_font.render("Game Over", False, (0, 0, 0))
            score_text = menu_font.render(f"Score: {int(score)}", False, (0, 0, 0))
            high_score_text = menu_font.render(f"High Score: {int(high_score)}", False, (0, 0, 0)) 
            background = pygame.Surface((1000,750))
            background.set_alpha(128)
            background.fill((0,0,0))
            display.blit(background, (0,0))
            display.blit(game_over, (100, 200))
            display.blit(score_text, (100, 250))
            display.blit(high_score_text, (100, 300))
            exit_button = button("Exit", 100, 350, 75, 37, (255,0,0), display)    
            play_again_button = button("Again", 200, 350, 75, 37, (0,255,0), display)    
            if exit_button.check():
                pygame.quit()
                sys.exit()
            if play_again_button.check():
                player.dead = False
                player.velY = 0
                player.velX = 0
                score = 0
                player.y = 400
                player.x = 200
                # Respawn platforms
                plat1.x =200
                plat1.y = 550
                for x in platforms:
                    x.flag = True
                plat2.firstSpawn(plat1)
                plat3.firstSpawn(plat2)
                plat4.firstSpawn(plat3)
                plat5.firstSpawn(plat4)
                plat6.firstSpawn(plat5)
                plat7.firstSpawn(plat6)
                plat8.firstSpawn(plat7)
        
        # Collisions
        for x in platforms:
            if collisions(player.x, player.y+player.sprite.get_height(), player.sprite.get_width(), 1, x.x, x.y, 50, 10) and player.velY > 0:
                player.jump = True
                jump_sound_effect.play()
                player.yAtjump = player.y
                player.velY = 0
        
        # Draw.
        
        pygame.display.flip()
        fpsClock.tick(fps)

main()