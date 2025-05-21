import pygame
import time
from pygame.locals import *

player_size = (100,100)

player = pygame.image.load("src/assets/player_movement/movement1.png")
player = pygame.transform.scale(player,player_size)
player_rect = player.get_rect()

  


def movement():
    speed = 4
    keys =pygame.key.get_pressed()
    if keys[K_w]:
        player_rect.y -= speed                
    if keys[K_s]:
        player_rect.y += speed                
    if keys[K_a]:
        player_rect.x -= speed                
    if keys[K_d]:
        player_rect.x += speed

