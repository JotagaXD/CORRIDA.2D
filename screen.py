import pygame
from os.path import join

def init(display_surface, clock, WINDOW_WIDTH, WINDOW_HEIGHT):
    press = False
    show = True
    flash_timer = 0
    flash_interval = 300
    while not press:
        flash_timer += clock.get_rawtime()
        display_surface.fill('black')
        menu_surf = pygame.image.load(join('images', 'init', 'menunovao.png'))
        menu_surf = pygame.transform.scale(menu_surf, (700, 300))
        menu_rect = menu_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/3))
        init_surf = pygame.image.load(join('images', 'init', 'pressione r.png'))
        init_surf = pygame.transform.scale(init_surf, (500, 70))
        init_rect = init_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT*3/4))
        if flash_timer >= flash_interval:
            flash_timer = 0
            show = not show
            display_surface.fill('black')
        if show:
            display_surface.blit(init_surf, init_rect)
        display_surface.blit(menu_surf, menu_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                press = True
                return False
        if pygame.key.get_just_pressed()[pygame.K_r]:
            press = True
            return True
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def end(font_base, display_surface, WINDOW_WIDTH, WINDOW_HEIGHT):
    '''global highscore_name
    global highscore
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    display_surface.fill((0, 0, 0,))
    if pontuacao > highscore[-1]:
        texto_do_usuario = ""
        entrada_concluida = False
        while True:
            display_surface.fill((0, 0, 0))
            novorecorde = pygame.image.load(join('images', 'end', 'NOVORECORDE.png'))
            novorecorde = pygame.transform.scale(novorecorde, (600, 130))
            display_surface.blit(novorecorde, (100, 20))

            texto = fontebase.render(texto_do_usuario, False, (255, 125, 37))
            display_surface.blit(texto, (0, 0))

            # escrever aqui o nome do jogador
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        entrada_concluida = True
                        x = False
                    elif event.key == pygame.K_BACKSPACE:
                        texto_do_usuario = texto_do_usuario[:-1]
                    else:
                        texto_do_usuario += event.unicode

            pygame.display.update()

            if entrada_concluida:
                highscore.pop()
                highscore_name.pop()
                highscore.append(pontuacao)
                highscore.sort(reverse=True)
                index = highscore.index(pontuacao)
                highscore_name.insert(index, texto_do_usuario)
                print(highscore_name)
                print(highscore)
                entrada_concluida = False
            # print ranking
    else:'''
    display_surface.fill('black')
    while True:
        derrota_surf = pygame.image.load(join('images', 'end', 'voceperdeu.png'))
        derrota_surf = pygame.transform.scale(derrota_surf, (640, 180))
        derrota_rect = derrota_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/3))
        display_surface.blit(derrota_surf, derrota_rect)
        tentardnv_surf = pygame.image.load(join('images', 'end', 'pressionerpratentardenovo.png'))
        tentardnv_surf = pygame.transform.scale(tentardnv_surf, (500, 70))
        tentardnv_rect = tentardnv_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT*3/5))
        display_surface.blit(tentardnv_surf, tentardnv_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return False
                exit()

        if pygame.key.get_pressed()[pygame.K_r]:
            return True
            pass

        pygame.display.update()