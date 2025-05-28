import pygame
from pygame.locals import *
import math


def player_init():
    
    player_size = (100,100)
    player = pygame.image.load("src/assets/player_movement/movement1.png")
    player_img = pygame.transform.scale(player,player_size)
    player_rect = player.get_rect(center = (960,540))
    return player_img, player_rect


def damage(player_life,damage_made):
    player_life += damage_made
    if player_life <=0:
        pygame.quit()
    return player_life

# def Waffe(player_rect):
#     mouse = pygame.mouse.get_pos()
#     x_cor_difference =  player_rect.x - enemy_rect.x
#     y_cor_difference = player_rect.y - enemy_rect.y 
    
    
#     length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
#     update_enemy_x = 10 * ((x_cor_difference / (length)))
#     update_enemy_y = 10 *((y_cor_difference / (length)))
#     return [int(update_enemy_x),int(update_enemy_y)]
def Blitzi(enemy_position_dictionary,amount_enemy):
    keys =pygame.key.get_pressed()
    if keys[K_b]:
        mouse_pos = pygame.mouse.get_pos()
        
        #for i in range(amount_enemy):
        #    enemy_pos = enemy_position_dictionary[i][0]
        for i in range(amount_enemy):
            if enemy_position_dictionary[i][0].x <= mouse_pos[0] + 50 and enemy_position_dictionary[i][0].x >= mouse_pos[0] - 50 and enemy_position_dictionary[i][0].y <= mouse_pos[1] + 50 and enemy_position_dictionary[i][0].y >= mouse_pos[1] - 50: 
                enemy_position_dictionary[i][1] = enemy_position_dictionary[i][1] - 10
    return enemy_position_dictionary
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

