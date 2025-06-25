import pygame
from player import Blitzi
from asset_source import start_location_path
screen = pygame.display.set_mode((600,600))



def text(killcount):
    font = pygame.font.Font(f"{start_location_path()}assets/10Pixel-Bold.ttf",50)
    text = font.render(f"Kills: {killcount}",1, (255,255,255))
    return text