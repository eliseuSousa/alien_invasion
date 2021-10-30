import pygame
from pygame import rect
from pygame.sprite import Sprite
import random

class Planet(Sprite):
    def __init__(self,screen, area_x, area_y):
        super(Planet, self).__init__()
        self.screen = screen
        planets = './img/background/planets/planet00.bmp ./img/background/planets/planet01.bmp ./img/background/planets/planet02.bmp ./img/background/planets/planet03.bmp ./img/background/planets/planet04.bmp'.split()

        lst_planets = planets

        # Carrega a imagem e obtem o seu rect
        self.image_planet = pygame.image.load(lst_planets[random.randint(0, len(lst_planets)-1)])
        self.rect = self.image_planet.get_rect()

        # Posição inicial do planeta
        self.rect.x = random.randint(area_x[0], area_x[1]) + self.rect.width
        self.rect.y = random.randint(area_y[0], area_y[1])

        self.y = float(self.rect.y)

    def update(self):
        self.y += 0.08
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image_planet, self.rect)
        