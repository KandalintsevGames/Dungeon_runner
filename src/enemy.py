#imports
import bosse
import pygame
import math
import random as r
from asset_source import start_location_path

pygame.init()


def init_enemy(enemy_size):
    x=r.randint(1,9)
    enemy_rect_dictionary = {"hi":"hallo"}
    enemy = pygame.image.load(f"{start_location_path()}assets/enemy.png").convert_alpha()
    enemy_life_red = pygame.image.load(f"{start_location_path()}assets/Lifebar_enemy.png").convert_alpha()
    enemy_life_black = pygame.image.load(f"{start_location_path()}assets/Lifebar_black_enemy.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy,enemy_size)
    enemy_life_red_img = pygame.transform.scale(enemy_life_red,(100,50))
    enemy_life_black_img = pygame.transform.scale(enemy_life_black,(100,50))
    
    for i in range(x):
        liste_positionen = [(0,r.randint(0,1080)),(r.randint(0,1920),0),(1920,r.randint(0,1080)),(r.randint(0,1920),1080)]
        enemy_rect_dictionary[i]= [enemy.get_rect(center = liste_positionen[r.randint(0,3)]),100,100,enemy_img,-10,100,100]
    return enemy_img, enemy_rect_dictionary, x,enemy_life_red_img,enemy_life_black_img


def enemy_goto(player_rect,enemy_rect,range_enemy,damage_möglich):
    damage = 0
    enemy_rect
    x_cor_difference =  player_rect.x - enemy_rect.x
    y_cor_difference = player_rect.y - enemy_rect.y 
    #Koordinatendifferenz
    
    length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
    #Berechnung von der Länge vom Vektor durch Pythagoras
    if length <= range_enemy:
         update_enemy_x = 0
         update_enemy_y  = 0
         damage = damage_möglich
    #Falls Gegner zu nahe kommt, bewegt er nicht
    else:
        update_enemy_x = 10 * ((x_cor_difference / (length)))
        update_enemy_y = 10 *((y_cor_difference / (length)))
    #Berechnung vom Einheitswektor von vohrher
    return [round(update_enemy_x),round(update_enemy_y),damage]
    #Falls Gegner zu nahe kommt, bewegt er nicht