import pygame
import random as r
from asset_source import start_location_path
def bosse_init(enemy_rect_dictionay):
    
   
    dictionary_bosse = {10:["assets/enemy.png",(500,500),500,"non",-50]}
    return dictionary_bosse
def bosse_load(enemy_rect_dictionary,dictionary_bosse,amount_enemy,welle):
    liste_positionen = [(0,r.randint(0,1080)),(r.randint(0,1920),0),(1920,r.randint(0,1080)),(r.randint(0,1920),1080)]
    boss = pygame.image.load(f"{start_location_path()}assets/enemy.png").convert_alpha()
    bosse_img = pygame.transform.scale(boss,dictionary_bosse[welle][1])
    
    enemy_rect_dictionary[amount_enemy]= [bosse_img.get_rect(center = liste_positionen[r.randint(0,3)]),dictionary_bosse[welle][2],100,bosse_img,dictionary_bosse[welle][4],dictionary_bosse[welle][2],500]
    amount_enemy +=1
    return enemy_rect_dictionary,amount_enemy
