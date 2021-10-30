from pygame.display import update
from star import Star
from big_star import BigStar
from planet import Planet
import time

def init_background(screen, stars, big_stars, planets):
    area_x = (0, 800)
    area_y = (0, 600)

    for new_star in range(50):
        # Posicão inicial das estrelas
        new_star = Star(screen, area_x, area_y)
        stars.add(new_star)

    for new_big_star in range(5):
        new_big_star = BigStar(screen, area_x, area_y)
        big_stars.add(new_big_star)
    
    for new_planet in range(2):
        new_planet = Planet(screen, area_x, area_y)
        planets.add(new_planet)
        time.sleep(0.5)
    

def update_background(screen, stars, big_stars, planets):
    area_x = (0, 800)
    area_y = (-40, 0)

    stars.update()
    big_stars.update()
    planets.update()

    for star in stars.sprites():
        star.blitme()
    for planet in planets.sprites():
        planet.blitme()
    for big_star in big_stars.sprites():
        big_star.blitme()

    for star in stars.copy():
        if star.rect.y > 600:
            stars.remove(star)
            create_new_star(screen, stars, area_x, area_y)
    
    for big_star in big_stars.copy():
        if big_star.rect.y > 600:
            big_stars.remove(big_star)
            create_big_new_star(screen, big_stars, area_x, area_y)

    for planet in planets.copy():
        if planet.rect.y > 640:
            planets.remove(planet)
            create_new_planet(screen, planets, area_x, area_y)
            time.sleep(0.3)


def create_new_star(screen, stars, area_x, area_y):
    new_star = Star(screen, area_x, area_y)
    stars.add(new_star)

def create_big_new_star(screen, big_stars, area_x, area_y):
    new_big_star = BigStar(screen, area_x, area_y)
    big_stars.add(new_big_star)
    
def create_new_planet(screen, planets, area_x, area_y):
    new_planet = Planet(screen, area_x, area_y)
    planets.add(new_planet)

