import pygame
import random
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen, area_x, area_y):
        super(Star, self).__init__()
        self.screen = screen
        # Carrega a imagem da estrela e pega seu rect
        self.star_image = pygame.image.load('./img/background/stars/star.bmp')
        self.rect = self.star_image.get_rect()
        
         # Posicão inicial das estrelas
        self.rect.x = random.randint(area_x[0], area_x[1])
        self.rect.y = random.randint(area_y[0], area_y[1])

        self.y = float(self.rect.y)

    def blitme(self):
         self.screen.blit(self.star_image, self.rect)

    
    def update(self):
        self.y += 0.07
        self.rect.y = self.y 
    