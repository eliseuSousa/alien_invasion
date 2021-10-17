import sys

import pygame
from pygame import rect

from bullet import Bullet

from alien import Alien

def check_events_keydown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Criando novos projéteis
        fire_bullets(ai_settings, screen, ship, bullets)

def check_events_keyup(event, ship):
    if event.key == pygame.K_k:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos do teclado e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Atualiza as imagens na tela e altera para a nova tela"""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas

    for bullet in bullets.sprites():
        bullet.blit_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Deixa a tela mais recente visível
    pygame.display.flip()

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_alien_x(ai_settings, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(available_space_x / alien_width)
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas com alienígenas na tela."""
    avaiable_space_x = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(avaiable_space_x / (2 * alien_height))
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
    """Cria uma flota completa de alienígenas"""

    # Cria um alienígena e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual à largura de um alienígena. Obs. Aqui não vamos usar essas medidas porque a
    # largura do alienígena já é grande o bastante

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    row_number = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Cria a frota de alienígenas
    for row_number in range(row_number):
        for alien_number in range(number_aliens_x):
        # Cria um alienígena e o posiciona na linha
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    print(len(aliens))
