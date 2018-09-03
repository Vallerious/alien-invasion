import pygame
import sys

from settings import Settings
from pygame_helper import PygameHelper
from ship import Ship
from bullets import Bullets
from alien import Alien
from aliens import Aliens

settings = Settings()
pg = PygameHelper(settings)


def run_game():
    pg.init()

    current_lives = settings.total_lives

    screen = pg.set_display_dimensions(settings.screen_dim)
    pg.set_caption(settings.caption)
    screen_rect = screen.get_rect()

    # Make a ship
    img = pg.load_img('img/ship.bmp')
    ship = Ship(screen_rect.centerx, screen_rect.bottom, img)

    bullets = Bullets()

    aliens = Aliens()

    while True:
        pg.watch_user_events(ship, bullets)

        screen.fill(settings.background_color)

        pg.check_collisions_aliens_ships(ship, aliens, bullets, settings, screen)

        if ship.is_dead():
            print('Sorry you are dead!')

        if aliens.size() == 0:
            bullets.empty()
            pg.create_alien_fleet(aliens, settings.screen_dim[0], settings.screen_dim[1])
            aliens.increase_drop_rate(10)

        ship.update(screen_rect)
        bullets.update()
        PygameHelper.check_collisions(bullets, aliens)
        aliens.update(screen)

        ship.draw(screen)
        aliens.draw(screen)
        bullets.draw(screen)

        pg.flip()


run_game()
