import pygame
from pygame.locals import *
import math


def player_init():
    
    player_size = (100,100)
    player = pygame.image.load("src/assets/player_movement/movement1.png")
    player_img = pygame.transform.scale(player,player_size)
    player_rect = player.get_rect()
    return player_img, player_rect


# def Waffe(player_rect):
#     mouse = pygame.mouse.get_pos()
#     x_cor_difference =  player_rect.x - enemy_rect.x
#     y_cor_difference = player_rect.y - enemy_rect.y 
    
    
#     length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
#     update_enemy_x = 10 * ((x_cor_difference / (length)))
#     update_enemy_y = 10 *((y_cor_difference / (length)))
#     return [int(update_enemy_x),int(update_enemy_y)]


def movement(rect):
    speed = 5
    keys =pygame.key.get_pressed()
    if keys[K_w]:
        rect.y -= speed                
    if keys[K_s]:
        rect.y += speed                
    if keys[K_a]:
        rect.x -= speed                
    if keys[K_d]:
        rect.x += speed

