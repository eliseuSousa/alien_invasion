import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep

def check_events_keydown(event, ai_settings, screen, ship, bullets):
    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_l):
        ship.moving_right = True
    elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_j):
        ship.moving_left = True
    elif (event.key == pygame.K_SPACE) or (event.key == pygame.K_k):
        # Criando novos projéteis
        fire_bullets(ai_settings, screen, ship, bullets)

def check_events_keyup(event, ship):
    if event.key == pygame.K_q:
        sys.exit()
    
    elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_l):
        ship.moving_right = False
    
    elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_j):
        ship.moving_left = False
    

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,  bullets):
    """Responde a eventos do teclado e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens, mouse_x, mouse_y):
    """Inicializa um novo jogo quando o jogador clicar Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reinicia as configurações do jogo
        ai_settings.initialize_dynamic_settings()
        # Ocultar o cursor do mouse
        pygame.mouse.set_visible(False)

        # Reinicia os dados estatísticos do jogo
        stats.reset_stats()
        stats.game_active = True

        # Reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçoanve
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Atualiza as imagens na tela e altera para a nova tela"""
    
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas

    for bullet in bullets.sprites():
        bullet.blit_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Desenha a informação sobre pontuação
    sb.show_score()

    # Dsenha o botão Play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_alien_x(ai_settings, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""
    available_space_x = ai_settings.screen_width -  1.5*alien_width
    number_aliens_x = int(available_space_x / alien_width)
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas com alienígenas na tela."""
    avaiable_space_y = (ai_settings.screen_height - (4*alien_height) - ship_height)
    number_rows = int(avaiable_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Cria um alienígena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_number * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de alienígenas"""

    # Cria um alienígena e calcula o número de alienígenas em uma linha

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    row_number = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Cria a frota de alienígenas
    for row_number in range(row_number):
        for alien_number in range(number_aliens_x):
        # Cria um alienígena e o posiciona na linha
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Reponde apropriadamente se algum alienígena alcançou uma borda"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Faz a frota descer e mudar a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena."""
    if stats.ships_left > 0:
        # Decrementa ships_left
        stats.ships_left -= 1
        
        # Atualiza o painel de pontuação
        sb.prep_ships()

        # Esvazia a lista de alienígenas e de projetéis
        aliens.empty()
        bullets.empty()
        
        # Faz uma pausa
        sleep(0.5)

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """ Verificar se a frota está em uma das bordas e então 
        atualizar as posições de todos os alienígenas da frota.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colisões entre o alienígena e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    # Verifica se há algum alienígena que atingiu a parte inferior da tela
    check_aliens_buttom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Livra-se dos projéteis antigos 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_high_score(stats, sb)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenham
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for values in collisions.values():
            stats.score += ai_settings.alien_point
            sb.prep_score()

    if len(aliens) == 0:
        # Destrói os projéteis existentes, aumenta a velocidade do jogo e cria uma nova frota
        # Se a frota for destruída, inicia um novo nível
        bullets.empty()
        ai_settings.increase_speed()

        # Aumanta o nivel
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def check_aliens_buttom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Verifica se algum alienígena alcnçou a parte inferior da tela."""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """Verifica se há uma nova pontução máxima."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()