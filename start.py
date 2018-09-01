import pygame
import sys

from settings import Settings
from pygame_helper import PygameHelper
from ship import Ship
from bullets import Bullets

settings = Settings()
pg = PygameHelper(settings)


def run_game():
    pg.init()

    screen = pg.set_display_dimensions(settings.screen_dim)
    pg.set_caption(settings.caption)
    screen_rect = screen.get_rect()

    # Make a ship
    img = pg.load_img('img/ship.bmp')
    ship = Ship(screen_rect.centerx, screen_rect.bottom, img)

    bullets = Bullets()

    while True:
        pg.watch_user_events(ship, bullets)

        screen.fill(settings.background_color)

        ship.update(screen_rect)
        bullets.update()

        ship.draw(screen)
        bullets.draw(screen)

        pg.flip()


run_game()
