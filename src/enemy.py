import pygame
import math
import random as r
pygame.init()

enemy_size = (100,100)

def init_enemy(enemy_size):
    x = r.randint(1,10)
    enemy_rect_dictionary = {"hi":"hallo"}
    enemy = pygame.image.load("enemy.png")
    enemy_img = pygame.transform.scale(enemy,enemy_size)
    for i in range(x):
        enemy_rect_dictionary[i]= enemy.get_rect(center = (0,r.randint(0,1080)))
    return enemy_img, enemy_rect_dictionary, x


def enemy_goto(player_rect,enemy_rect):
    x_cor_difference =  player_rect.x - enemy_rect.x
    y_cor_difference = player_rect.y - enemy_rect.y 
    #Koordinatendifferenz
    
    length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
    #Berechnung von der Länge vom Vektor durch Pythagoras
    if length <= 100:
         update_enemy_x = 0
         update_enemy_y  = 0
    #Falls Gegner zu nahe kommt, bewegt er nicht
    else:
        update_enemy_x = 5 * ((x_cor_difference / (length)))
        update_enemy_y = 5 *((y_cor_difference / (length)))
    #Berechnung vom Einheitswektor von vohrher
    return [round(update_enemy_x),round(update_enemy_y)]
    #Falls Gegner zu nahe kommt, bewegt er nicht