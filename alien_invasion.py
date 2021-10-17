import pygame

from settings import Settings

from ship import Ship

import game_fuctions as gf

from pygame.sprite import Group

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')
    pygame.display.set_icon(ai_settings.icon)
    
    # Cria uma espaçoanave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # Cria uma frota de alienígnas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicializa o laço principal do jogo
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
