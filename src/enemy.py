import pygame
import math

pygame.init()

enemy_size = (100,100)

def init_enemy(enemy_size):

    enemy = pygame.image.load("enemy.png")
    enemy_img = pygame.transform.scale(enemy,enemy_size)
    enemy_rect = enemy.get_rect(center = (500,500))
    return enemy_img, enemy_rect


def enemy_goto(player_rect,enemy_rect):
    x_cor_difference =  player_rect.x - enemy_rect.x
    y_cor_difference = player_rect.y - enemy_rect.y 
    #Koordinatendifferenz
    
    length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
    #Berechnung von der Länge vom Vektor durch Pythagoras
    # if length <= 100:
    #     update_enemy_x = 0
    #     update_enemy_y  = 0
    #Falls Gegner zu nahe kommt, bewegt er nicht
    print(length)

    # else: 
    update_enemy_x = 3 * ((x_cor_difference / (length)))
    update_enemy_y = 3 *((y_cor_difference / (length)))
    #Berechnung vom Einheitswektor von vohrher
    return [round(update_enemy_x),round(update_enemy_y)]
    #Falls Gegner zu nahe kommt, bewegt er nicht