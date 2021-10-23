import pygame

from settings import Settings

from ship import Ship

import game_fuctions as gf

from pygame.sprite import Group

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')
    pygame.display.set_icon(ai_settings.icon)

    # Criando um botão play
    play_button = Button(ai_settings, screen, 'Play')
    
    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings) 
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçoanave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # Cria uma frota de alienígnas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicializa o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            bullets.update()
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
