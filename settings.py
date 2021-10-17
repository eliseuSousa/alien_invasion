import pygame

class Settings():
    def __init__(self):
        """Uma classe para armazenar as configurações da Invação Alienígena"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (40,29,43)
        self.icon = pygame.image.load('./img/arcade-game.png')

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5

        # Configurções dos projétes 
        self.bullet_speed_factor = 3
        self.bullets_allowed = 3