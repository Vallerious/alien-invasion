import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class that represents a bullet on the screen """

    def __init__(self, spawn_point_x: float, spawn_point_y: float):
        super(Bullet, self).__init__()

        # Initialize the bullet graphic properties
        self.__bullet_width = 3
        self.__bullet_height = 15
        self.color = (60, 60, 60)
        self.speed = 1

        # First create a bullet at 0, 0 and then set the correct position
        self.rect = pygame.Rect(0, 0, self.__bullet_width, self.__bullet_height)
        self.rect.centerx = spawn_point_x
        self.rect.top = spawn_point_y

        # Store the bullet as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """ Update the properties of the bullet so on redraw it appears moving """
        self.y = self.y - self.speed
        self.rect.y = self.y

    def draw_bullet(self, screen):
        """ Calls a native method to draw a rectangle representing a bullet """
        pygame.draw.rect(screen, self.color, self.rect)
