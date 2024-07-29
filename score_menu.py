import pygame
def scorepage(HIGHSCORE_label_nomes,HIGHSCORE_label_pontos,WINDOW_WIDTH, WINDOW_HEIGHT,fontebase):
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display_surface.fill((0, 0, 0,))
    print_y=80
    print_yp=80
    contador=0
    while True:
        menu=pygame.image.load('images/end/menu.png')
        menu=pygame.transform.scale(menu,(230,100))
        display_surface.blit(menu,(250,600))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if pygame.key.get_just_pressed()[pygame.K_m]:

                '''MENU PRINCIPAL'''
        if contador == 0:
            for i in HIGHSCORE_label_nomes:
                nomes = fontebase.render(f"{i}", False, (255, 125, 37))
                display_surface.blit(nomes, (150, print_y))
                print_y+=60
            for h in HIGHSCORE_label_pontos:
                pontos = fontebase.render(f"{h}", False, (255, 125, 37))
                display_surface.blit(pontos, (550, print_yp))
                print_yp += 60
        pygame.display.update()
        contador+=1