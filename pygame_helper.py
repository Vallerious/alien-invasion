import pygame
import sys
from time import sleep

from bullet import Bullet
from alien import Alien


class PygameHelper:
    """This class will wrap all the needed pygame methods"""

    def __init__(self, settings):
        self.pg = pygame
        self.settings = settings

    def init(self):
        self.pg.init()

    def set_display_dimensions(self, dim):
        """ Sets the width and height of the window and returns a screen"""
        return self.pg.display.set_mode(dim)

    def set_caption(self, caption):
        """ Sets the title at the top-center of the screen """
        self.pg.display.set_caption(caption)

    def watch_user_events(self, ship, bullets):
        """ Watch for keyboard and mouse events """
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT:
                sys.exit()
            elif event.type == self.pg.KEYDOWN:
                if event.key == self.pg.K_RIGHT:
                    ship.init_move_right()
                elif event.key == self.pg.K_LEFT:
                    ship.init_move_left()
                elif event.key == self.pg.K_SPACE:
                    # Shoot a new bullet
                    bullets.add(Bullet(
                        ship.rect.centerx,
                        ship.rect.top
                    ))
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == self.pg.KEYUP:
                if event.key == self.pg.K_RIGHT:
                    ship.stop_move_right()
                elif event.key == self.pg.K_LEFT:
                    ship.stop_move_left()

    def flip(self):
        """ Make the most recently drawn screen visible. """
        self.pg.display.flip()

    def load_img(self, path):
        """ Loads an image from the file system and returns it """
        return self.pg.image.load(path)

    @staticmethod
    def get_number_of_aliens_per_row(screen_width, alien_width):
        available_space_x = screen_width - (2 * alien_width)
        number_aliens_x = int(available_space_x / (2 * alien_width))

        return number_aliens_x

    @staticmethod
    def get_x_offset(alien_width, alien_number):
        return alien_width + (2 * alien_width) * alien_number

    @staticmethod
    def get_row_number(alien_height, screen_height):
        return (screen_height - (alien_height * 3)) / alien_height

    def create_alien_fleet(self, aliens, screen_width, screen_height):
        """ Populates the screen with aliens """

        # First let us create an alien to use as a measure
        img = self.load_img('img/alien.bmp')
        alien = Alien(img.get_rect().width, img.get_rect().height, img)

        alien_width = alien.rect.width
        number_aliens_x = PygameHelper.get_number_of_aliens_per_row(screen_width, alien_width)
        rows = int(PygameHelper.get_row_number(alien.rect.height, screen_height))

        for row in range(rows):
            for alien_number in range(number_aliens_x):
                x = PygameHelper.get_x_offset(alien_width, alien_number)
                alien = Alien(x, alien.rect.width * row, img)

                aliens.add(alien)

    @staticmethod
    def check_collisions(bullets, aliens):
        collisions = pygame.sprite.groupcollide(bullets.get_bullets(), aliens.get_aliens(), True, True)

    def check_collisions_aliens_ships(self, ship, aliens, bullets, settings, screen):
        # Check if some of the alien ships has collided with our ship
        if pygame.sprite.spritecollideany(ship, aliens.get_aliens()) or aliens.check_if_hit_bottom(screen):
            ship.die_a_little()
            sleep(0.5)
            aliens.empty()
            bullets.empty()
            self.create_alien_fleet(aliens, settings.screen_dim[0], settings.screen_dim[1])
