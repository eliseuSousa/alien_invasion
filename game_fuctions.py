import sys

import pygame

def check_events_keydown(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_events_keyup(event, ship):
    if event.key == pygame.K_k:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Responde a eventos do teclado e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ship)    
        
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ship)

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e altera para a nova tela"""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()