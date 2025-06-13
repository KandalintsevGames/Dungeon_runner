import pygame
from asset_source import start_location_path


def start(screen):
    pygame.init()
    font = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',300)
    font1 = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',100)
    game_name =font.render('Game' , True ,(255,255,255) )
    start_button = font1.render('Start' , True ,(255,255,255) )
    text1_rect = start_button.get_rect(center = (150,500))
    text3 = font1.render('Options' , True ,(255,255,255) )
    text3_rect = text3.get_rect(center = (150,600))
    text2 = font1.render('quit' , True ,(255,255,255) )
    text2_rect = text2.get_rect(center = (150,700))
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
                
        screen.blit(game_name,(300,100))
        screen.blit(start_button,text1_rect)
        screen.blit(text2,text2_rect)
        screen.blit(text3,text3_rect)
        pygame.display.update()
def option(screen):
    pygame.init()
    font = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',300)
    font1 = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',100)
    options =font.render('Options' , True ,(255,255,255) )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        screen.blit(options,(300,100))
        pygame.display.update()