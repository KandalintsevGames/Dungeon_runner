import pygame
from pygame.locals import *

player_image_loaction = "src/assets/player.gif"

player = pygame.image.load(player_image_loaction)
player_rect = player.get_rect()