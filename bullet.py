import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """Uma classe que adiministra os projéteis disparados."""
    def __init__(self, ai_settings, screen, ship):
        """Cria um projétil na posição atual espaçonava."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.ship = ship
        
        # Cria um retângulo na posição (0, 0) e, em sequida define
        # Posição correta
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_heigth)
        # self.rect.centerx =  ship.rect.centerx
        # self.rect.top = ship.rect.top

        # Carregando a imagem na tela 
        self.bullet_image = pygame.image.load('./img/ships/bullet_ship00.bmp')
        self.rect = self.bullet_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Inicializa o projétil de acordo com a posição da espaçonave
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top
        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)
        
        # self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
         
    def update(self):
        """Move o projétil para cima da tela"""
        # Atualiza a posição decimal do projétil
        self.y -= self.speed_factor
        
        # Atualiza a posição de rect
        self.rect.y = self.y

    # def draw_bullet(self):
    #     """Desenha o projétil na tela"""
    #     pygame.draw.rect(self.screen, self.color, self.rect)

    def blit_bullet(self):
        self.screen.blit(self.bullet_image, self.rect)