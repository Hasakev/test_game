"""
Created on Tue Nov 22 10:13 2022

@author: Kevin Luo

A game...
"""

import pygame
from sys import exit

#Variables
framerate = 60
screenDimensions = (800, 400)
skyDimensions = (800, 270)
groundDimensions = (800, 130)

snailPosition = [600, 240]
snailImages = ["graphics/snail/snail1.png", "graphics/snail/snail2.png"]

#initialise display surface
pygame.init()
screen = pygame.display.set_mode(screenDimensions)
pygame.display.set_caption("Game")
#for framerate
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/skies.png")
sky_surface = pygame.transform.scale(sky_surface, skyDimensions).convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png")
ground_surface = pygame.transform.scale(ground_surface, groundDimensions).convert_alpha()
text_surface = font.render("Brice and Isaac Relationship", False, "black")
snail_surface = pygame.image.load(snailImages[1])

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,270))

while True:
    #To quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 270))
    screen.blit(text_surface, (150, 50))
    snail_surface = pygame.image.load(snailImages[0])
    screen.blit(snail_surface, (snailPosition[0], snailPosition[1]))
    player_rect.left += 1
    screen.blit(player_surface, player_rect)
    snailPosition[0] -= 1
    if snailPosition[0] < -50:
        snailPosition[0] = 800
    
    
    
    pygame.display.update()

    #for framerate managing
    clock.tick(framerate)