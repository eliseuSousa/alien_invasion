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
    ship = Ship(ai_settings,screen)
    # Cria um grupo para armazenar os projéteis
    bullets = Group()

    # Inicializa o laço principal do jogo
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
