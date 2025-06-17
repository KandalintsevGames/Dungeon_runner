import pygame
from pygame.locals import *
from asset_source import start_location_path


def player_init():
    x_size = 100
    y_size = 100
    player_r = pygame.image.load(f"{start_location_path()}assets/player_right.png").convert_alpha()
    player_l = pygame.image.load(f"{start_location_path()}assets/player_left.png").convert_alpha()
    baterie_base  =pygame.image.load(f"{start_location_path()}assets/battery.png").convert_alpha()
    baterie_color = pygame.image.load(f"{start_location_path()}assets/battery_insides.png").convert_alpha()
    player_r = pygame.transform.scale(player_r,(x_size,y_size))
    player_l = pygame.transform.scale(player_l,(x_size,y_size))
    baterie_base_img = pygame.transform.scale(baterie_base,(500,100))
    baterie_color_img = pygame.transform.scale(baterie_color,(450,80))
    player_rect = player_r.get_rect(center = (960,540))
    return player_r, player_rect ,baterie_color_img ,baterie_base_img,player_l 


def damage(player_life,damage_made):
    player_life += damage_made
    return player_life

# def Waffe(player_rect):
#     mouse = pygame.mouse.get_pos()
#     x_cor_difference =  player_rect.x - enemy_rect.x
#     y_cor_difference = player_rect.y - enemy_rect.y 
    
    
#     length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
#     update_enemy_x = 10 * ((x_cor_difference / (length)))
#     update_enemy_y = 10 *((y_cor_difference / (length)))
#     return [int(update_enemy_x),int(update_enemy_y)]

#weapon
def Blitzi(enemy_position_dictionary,amount_enemy):
    if True:
        mouse_pos = pygame.mouse.get_pos()
        
        #for i in range(amount_enif MOUSEBUTTONDOWN:emy):
        #    enemy_pos = enemy_position_dictionary[i][0]
        
        for i in range(amount_enemy):
            if enemy_position_dictionary[i][0].x <= mouse_pos[0] + enemy_position_dictionary[i][-1] and enemy_position_dictionary[i][0].x >= mouse_pos[0] - enemy_position_dictionary[i][-1] and enemy_position_dictionary[i][0].y <= mouse_pos[1] + enemy_position_dictionary[i][-1] and enemy_position_dictionary[i][0].y >= mouse_pos[1] - enemy_position_dictionary[i][-1]: 
                enemy_position_dictionary[i][1] -= 20
    return enemy_position_dictionary


def movement(rect):
    speed = 5
    keys =pygame.key.get_pressed()
    rotation = 0
    if keys[K_w]:
        if rect.y >= 0:
            rect.y -= speed                
    if keys[K_s]:
        if rect.y <= 920:
            rect.y += speed                
    if keys[K_a]:
        if rect.x >= 0:
            rect.x -= speed
            rotation = 0
    if keys[K_d]:
        if rect.x <= 1820:
            rect.x += speed
            rotation = 1
    return rotation