import os, sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The tested class
from bullet import Bullet


class BulletTestCase(unittest.TestCase):
    """ Tests for the class representing a bullet in the Alien Invaders game """

    def setUp(self):
        self.bullet = Bullet(0, 0)

    def test_initialization(self):
        self.assertIsNotNone(self.bullet.color)
        self.assertIsNotNone(self.bullet.speed)
        self.assertIsNotNone(self.bullet.rect)
        self.assertIsNotNone(self.bullet.y)

    def test_movement(self):
        current_y = self.bullet.y
        current_speed = self.bullet.speed

        self.bullet.update()

        self.assertEqual(current_y - current_speed, self.bullet.y)
        self.assertEqual(self.bullet.rect.y, self.bullet.y)


unittest.main()
