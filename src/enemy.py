import pygame
import math
import random as r
pygame.init()

enemy_size = (100,100)

def init_enemy(enemy_size):
    x = r.randint(1,10)
    enemy_rect_dictionary = {"hi":"hallo"}
    enemy = pygame.image.load("src/assets/enemy.png")
    enemy_life_red = pygame.image.load("src/assets/Lifebar_enemy.png")
    enemy_life_black = pygame.image.load("src/assets/Lifebar_black_enemy.png")
    enemy_img = pygame.transform.scale(enemy,enemy_size)
    enemy_life_red_img = pygame.transform.scale(enemy_life_red,(100,50))
    enemy_life_black_img = pygame.transform.scale(enemy_life_black,(100,50))
    for i in range(x):
        enemy_rect_dictionary[i]= [enemy.get_rect(center = (0,r.randint(0,1080))),100]
    return enemy_img, enemy_rect_dictionary, x,enemy_life_red_img,enemy_life_black_img


def enemy_goto(player_rect,enemy_rect):
    damage = 0
    x_cor_difference =  player_rect.x - enemy_rect.x
    y_cor_difference = player_rect.y - enemy_rect.y 
    #Koordinatendifferenz
    
    length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
    #Berechnung von der Länge vom Vektor durch Pythagoras
    if length <= 100:
         update_enemy_x = 0
         update_enemy_y  = 0
         damage = -1
    #Falls Gegner zu nahe kommt, bewegt er nicht
    else:
        update_enemy_x = 5 * ((x_cor_difference / (length)))
        update_enemy_y = 5 *((y_cor_difference / (length)))
    #Berechnung vom Einheitswektor von vohrher
    return [round(update_enemy_x),round(update_enemy_y),damage]
    #Falls Gegner zu nahe kommt, bewegt er nicht