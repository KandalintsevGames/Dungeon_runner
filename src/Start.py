import pygame
from asset_source import start_location_path
from pygame.locals import *

def start(screen):
    pygame.init()
    game_logo = pygame.image.load(f"{start_location_path()}assets/wallpaper logo.png")
    game_logo_rect = game_logo.get_rect()
    font1 = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',100)
    start_button = font1.render('Start' , True ,(255,255,255) )
    text1_rect = start_button.get_rect(center = (600,300))
    text3 = font1.render('Options' , True ,(255,255,255) )
    text3_rect = text3.get_rect(center = (600,500))
    text2 = font1.render('quit' , True ,(255,255,255) )
    text2_rect = text2.get_rect(center = (600,700))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse[0],mouse[1])
                if mouse[0] <= text1_rect.x + 300 and mouse[0] >= text1_rect.x - 300:
                    if mouse[1] <= text1_rect.y + 100 and mouse[1] >= text1_rect.y - 100:
                        running = True
                        return running, False
                if mouse[0] <= text3_rect.x + 300 and mouse[0] >= text3_rect.x - 300:
                    if mouse[1] <= text3_rect.y + 100 and mouse[1] >= text3_rect.y - 100:
                        running = False
                        return running, True
                if mouse[0] <= text2_rect.x + 300 and mouse[0] >= text2_rect.x - 300:
                    if mouse[1] <= text2_rect.y + 100 and mouse[1] >= text2_rect.y - 100:
                        running = False
                        return running, False
                    
        screen.blit(game_logo,(900,0))
        screen.blit(start_button,text1_rect)
        screen.blit(text2,text2_rect)
        screen.blit(text3,text3_rect)
        pygame.display.update()
def option(screen,amount_cat):
    pygame.init()

    font = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',300)
    font1 = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',100)
    options =font.render('Options' , True ,(255,255,255) )
    text1 = font1.render(str(amount_cat) , True ,(255,255,255) )
    text1_rect = text1.get_rect(center = (150,700))
    while True:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                while mouse[0] <= text1_rect.x + 300 and mouse[0] >= text1_rect.x - 300 and  mouse[1] <= text1_rect.y + 100 and mouse[1] >= text1_rect.y - 100:
                        
                    keys =pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    if keys[K_1]:
                        amount_cat = 1         
                    if keys[K_2]:
                        amount_cat = 2
                    if keys[K_3]:
                        amount_cat = 3 
                    if keys[K_4]:
                        amount_cat =  4
                    if keys[K_5]:
                        amount_cat =  5
                    if keys[K_6]:
                        amount_cat =  6
                    if keys[K_7]:
                        amount_cat =  7
                    if keys[K_8]:
                        amount_cat =  8
                    if keys[K_9]:
                        amount_cat =  9
                    text1 = font1.render(str(amount_cat) , True ,(255,255,255) )
                    text1_rect = text1.get_rect(center = (150,700))
                    screen.fill("black")
        screen.blit(options,(300,100))
        screen.blit(text1,text1_rect)

        pygame.display.update()
    return amount_cat