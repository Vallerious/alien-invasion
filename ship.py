class Ship:
    """ This class represents a ship """

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y

        self.__movement_step = 5
        self.__move_right = False
        self.__move_left = False

    def draw(self, screen):
        """ Draw the ship at its current location """
        screen.blit(self.image, self.rect)

    def move_right(self):
        """ Move to the right of the screen based on the movement step """
        self.rect.centerx = self.rect.centerx + self.__movement_step

    def move_left(self):
        """ Move to the left of the screen based on the movement step """
        self.rect.centerx = self.rect.centerx - self.__movement_step

    def init_move_right(self):
        """ Sets move right to true so that on update the x coordinate is incremented """
        self.__move_left = False
        self.__move_right = True

    def init_move_left(self):
        """ Sets move right to true so that on update the x coordinate is decremented """
        self.__move_right = False
        self.__move_left = True

    def stop_move_right(self):
        """ On update, the ship will not move further right """
        self.__move_right = False

    def stop_move_left(self):
        """ On update, the ship will not move further left """
        self.__move_left = False

    def update(self, screen_rect):
        """ Will move the ship according to its movement state """
        if self.__move_right:
            self.move_right()
        elif self.__move_left:
            self.move_left()

        if not self.is_in_bounds(screen_rect.left, screen_rect.right):
            self.stop_move_right()
            self.stop_move_left()

    def is_in_bounds(self, left: float, right: float):
        """ Checks if the ship is far of left or right on the screen """
        return left <= self.rect.centerx <= right

    def get_movement_step(self):
        return self.__movement_step


