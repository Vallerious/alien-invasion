import pygame
import sys

from bullet import Bullet


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

