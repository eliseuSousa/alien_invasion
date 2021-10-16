import sys

import pygame

from bullet import Bullet

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

def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e altera para a nova tela"""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas

    for bullet in bullets.sprites():
        bullet.blit_bullet()

    ship.blitme()

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