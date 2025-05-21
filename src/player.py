import pygame
from pygame.locals import *

player_image_loaction = "src/assets/player.png"
player = pygame.image.load(player_image_loaction)
player_rect = player.get_rect()

def movement():
    keys =pygame.key.get_pressed()
    if keys[K_w]:
        player_rect.y -= 1                
    if keys[K_s]:
        player_rect.y += 1                
    if keys[K_a]:
        player_rect.x -= 1                
    if keys[K_d]:
        player_rect.x += 1                
        

