import pygame

class Settings():
    def __init__(self):
        """Inicialza as configurações estáticas do jogo."""
        # Configurações da tela
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (40,29,43)
        self.icon = pygame.image.load('./img/arcade-game.bmp')

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configurções dos projétes 
        self.bullet_speed_factor = 3
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 15
        
        # fleet_direction  igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1 

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        # A taxa com que os pontos para cada alienígenas aumenta
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam no decorrer do jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction igual a 1 representa a direita, -1 representa a esquerda
        self.fleet_direction = 1 
        
        # Pontuação
        self.alien_point = 50

    def increase_speed(self):
        """Aumanta as configurações de velocidade e os pontos para cada alienígena."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
