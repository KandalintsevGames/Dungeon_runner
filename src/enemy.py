import pygame
import math

pygame.init()

enemy_size = (100,100)

enemy = pygame.image.load("enemy.png")
enemy1 = pygame.transform.scale(enemy,enemy_size)
enemy_rect = enemy.get_rect(center = (500,500))


def enemy_goto(player_rect,enemy_rect):
    x_cor_difference = enemy_rect.x -player_rect.x 
    y_cor_difference =enemy_rect.y -player_rect.y
    #Koordinatendifferenz

    length  = math.sqrt(y_cor_difference**2+x_cor_difference**2)
    #Berechnung von der Länge vom Vektor durch Pythagoras

    if length <= 100:
        x3 = 0
        y3  = 0
    #Falls Gegner zu nahe kommt, bewegt er nicht

    else: 
        x3 = x_cor_difference / (length)
        y3 = y_cor_difference / (length)
    #Berechnung vom Einheitswektor von vohrher
    return [x3,y3]