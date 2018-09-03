class SpaceObject:
    """ A generic class for a item representing an object in space """

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y

    def draw(self, screen):
        """ Draw the object at its current location """
        screen.blit(self.image, self.rect)
