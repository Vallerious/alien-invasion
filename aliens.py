from alien import Alien
from pygame.sprite import Group


class Aliens:
    """ A sprite group of alien objects """

    def __init__(self):
        self.__aliens = Group()
        self.__direction = 1
        self.__drop_speed = 10

    def get_aliens(self):
        return self.__aliens

    def draw(self, screen):
        """ Iterates alien sprites and calls for every alien to draw itself """
        for alien in self.__aliens.sprites():
            alien.draw(screen)

    def add(self, alien):
        self.__aliens.add(alien)

    def update(self, screen):
        self.check_fleet_edges(screen)
        self.__aliens.update(self.__direction)

    def drop_whole_fleet(self):
        for alien in self.__aliens.sprites():
            alien.rect.y = alien.rect.y + self.__drop_speed

    def check_fleet_edges(self, screen):
        """ If some of the aliens has hit an edge change its direction """
        for alien in self.__aliens:
            if alien.check_if_hit_edge(screen):
                self.__direction *= -1
                self.drop_whole_fleet()
                break

    def size(self):
        return len(self.__aliens)

    def empty(self):
        self.__aliens.empty()

    def check_if_hit_bottom(self, screen):
        screen_rect = screen.get_rect()
        hit_bottom = False

        for alien in self.__aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                hit_bottom = True
                break

        return hit_bottom

    def increase_drop_rate(self, addition):
        self.__drop_speed = self.__drop_speed + addition
