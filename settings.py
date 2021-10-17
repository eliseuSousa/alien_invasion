import pygame

class Settings():
    def __init__(self):
        """Uma classe para armazenar as configurações da Invação Alienígena"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (40,29,43)
        self.icon = pygame.image.load('./img/arcade-game.bmp')

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # Configurções dos projétes 
        self.bullet_speed_factor = 3
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 15
        # fleet_direction  igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1 