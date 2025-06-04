import pygame
def game_over(screen):
    pygame.init()
    font = pygame.font.Font('src/assets/10Pixel-Bold.ttf',300)
    font1 = pygame.font.Font('src/assets/10Pixel-Bold.ttf',100)
    text =font.render('Game over' , True ,(255,255,255) )
    text1 = font1.render('retry' , True ,(255,255,255) )
    text1_rect = text1.get_rect(center = (960,500))
    text2 = font1.render('quit' , True ,(255,255,255) )
    text2_rect = text2.get_rect(center = (960,700))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse[0],mouse[1])
                if mouse[0] <= text1_rect.x + 300 and mouse[0] >= text1_rect.x - 300:
                    if mouse[1] <= text1_rect.y + 100 and mouse[1] >= text1_rect.y - 50:
                        running = True
                        return running
                elif mouse[0] <= text2_rect.x + 300 and mouse[0] >= text2_rect.x - 300:
                    if mouse[1] <= text2_rect.y + 100 and mouse[1] >= text2_rect.y - 100:
                        running = False
                        return running
        screen.blit(text,(300,100))
        screen.blit(text1,text1_rect)
        screen.blit(text2,text2_rect)
        
        pygame.display.update()
