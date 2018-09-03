from pygame.sprite import Sprite

from space_object import SpaceObject


class Alien(Sprite):
    """ This class represents the enemy alien """

    # def __init__(self, x, y, image):
    #     super(Alien, self).__init__(x, y, image)

    def __init__(self, x, y, image):
        super(Alien, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y

        self.__speed_factor = 1

    def draw(self, screen):
        """ Draw the object at its current location """
        screen.blit(self.image, self.rect)

    def update(self, direction):
        self.rect.centerx = self.rect.centerx + (self.__speed_factor * direction)

    def check_if_hit_edge(self, screen):
        screen_rect = screen.get_rect()

        return self.rect.right > screen_rect.right or self.rect.left < 0
