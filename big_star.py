import pygame
from pygame.sprite import Sprite
import random

class BigStar(Sprite):
    def __init__(self, screen, area_x, area_y):
        super(BigStar, self).__init__()
        self.screen = screen

        # Carrega a imagem e obtêm seu rect
        self.big_star_image = pygame.image.load('./img/background/stars/big_star.bmp')
        self.rect = self.big_star_image.get_rect()

        # Posição inicial das estrelas
        self.rect.x = random.randint(area_x[0], area_x[1])
        self.rect.y = random.randint(area_y[0], area_y[1])

        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.big_star_image, self.rect)

    def update(self):
        self.y += 0.2
        self.rect.y = self.y
