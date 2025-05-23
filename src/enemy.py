import pygame
import math

pygame.init()

enemy_size = (100,100)

enemy = pygame.image.load("enemy.png")
enemy1 = pygame.transform.scale(enemy,enemy_size)
enemy_rect = enemy.get_rect(center = (0,0))


def enemy_goto(player_rect,enemy_rect):
    x_cor_difference =  player_rect.x - enemy_rect.x
    y_cor_difference = player_rect.y - enemy_rect.y 
    #Koordinatendifferenz
    
    length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
    #Berechnung von der Länge vom Vektor durch Pythagoras
    print(length)
    # if length <= 100:
    #     update_enemy_x = 0
    #     update_enemy_y  = 0
    #Falls Gegner zu nahe kommt, bewegt er nicht

    # else: 
    update_enemy_x = 10 * ((x_cor_difference / (length)))
    update_enemy_y = 10 *((y_cor_difference / (length)))
    #Berechnung vom Einheitswektor von vohrher
    print(length,x_cor_difference,y_cor_difference,update_enemy_x,update_enemy_y)
    return [int(update_enemy_x),int(update_enemy_y)]
    #Falls Gegner zu nahe kommt, bewegt er nicht