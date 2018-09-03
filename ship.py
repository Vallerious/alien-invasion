from space_object import SpaceObject


class Ship(SpaceObject):
    """ This class represents a ship """

    def __init__(self, x, y, image):
        super(Ship, self).__init__(x, y, image)

        self.__movement_step = 5
        self.__move_right = False
        self.__move_left = False
        self.__lives = 3

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

    def die_a_little(self):
        self.__lives = self.__lives - 1

    def get_electro_cardio_graphy(self):
        return self.__lives

    def is_dead(self):
        return self.__lives == 0
