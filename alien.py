import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Uma classe para administrar alienígena."""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define sua posição inicial"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem e define ser rect
        self.image = pygame.image.load('./img/aliens/alien00.bmp')
        self.rect = self.image.get_rect()

        # Inicializa cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienígena na sua posição atual."""
        self.screen.blit(self.image, self.rect)