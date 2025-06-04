import pygame
from player import Blitzi
screen = pygame.display.set_mode((600,600))

font = pygame.font.Font("src/assets/10Pixel-Bold.ttf",50)

def text(killcount):
    text = font.render(f"Kills: {killcount}",1, (255,255,255))
    return text