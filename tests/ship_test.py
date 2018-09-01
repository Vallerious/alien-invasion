import os, sys
import unittest
import pygame

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The tested class
from ship import Ship


class ShipTestCase(unittest.TestCase):
    """ Tests the Ship class of Alien Invaders game """

    def setUp(self):
        self.image = pygame.image.load('img/ship.bmp')
        self.ship = Ship(0, 0, self.image)

    def test_initialization(self):
        self.assertEqual(self.ship.rect.centerx, 0)
        self.assertEqual(self.ship.rect.bottom, 0)

    def test_move_right(self):
        current_center_x = self.ship.rect.centerx
        movement_step = self.ship.get_movement_step()

        self.ship.move_right()

        self.assertEqual(current_center_x + movement_step, self.ship.rect.centerx)

    def test_move_left(self):
        current_center_x = self.ship.rect.centerx
        movement_step = self.ship.get_movement_step()

        self.ship.move_left()

        self.assertEqual(current_center_x - movement_step, self.ship.rect.centerx)

    def test_is_in_bounds_left_ok(self):
        self.assertTrue(self.ship.is_in_bounds(0, 1000))

    def test_is_in_bounds_left_fail(self):
        self.assertFalse(self.ship.is_in_bounds(500, 1000))

    def test_is_in_bounds_right_ok(self):
        self.assertTrue(self.ship.is_in_bounds(0, 1000))

    def test_is_in_bounds_right_fail(self):
        self.assertFalse(self.ship.is_in_bounds(-4, -1))


unittest.main()
