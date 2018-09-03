from pygame.sprite import Group

from bullet import Bullet


class Bullets:
    """ This class will encapsulate a bullets sprite group """

    def __init__(self):
        self.__bullets = Group()
        self.__max_bullets = 10

    def get_bullets(self):
        return self.__bullets

    def update(self):
        """ Removes bullets outside window and then calls native pygame update """
        self.remove_stray_bullets()
        self.__bullets.update()

    def draw(self, screen):
        """ Iterates bullet sprites and calls for every bullet to draw itself """
        for bullet in self.__bullets.sprites():
            bullet.draw_bullet(screen)

    def add(self, bullet: Bullet):
        """ Adds a bullet to the sprite group but first checks threshold """
        if len(self.__bullets) < self.__max_bullets:
            self.__bullets.add(bullet)

    def remove_stray_bullets(self):
        """ Deletes the bullets from the list which are out of the window top """
        for bullet in self.__bullets.copy():
            if bullet.rect.y < 0:
                self.__bullets.remove(bullet)

    def empty(self):
        self.__bullets.empty()
