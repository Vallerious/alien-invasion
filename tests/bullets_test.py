import os, sys
import unittest
import pygame
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The tested class
from bullets import Bullets
from bullet import Bullet


class BulletsTestCase(unittest.TestCase):
    """ Tests the wrapper of sprite group of bullets """

    def setUp(self):
        self.bullets = Bullets()

    def test_initialization(self):
        self.assertIsNotNone(self.bullets.get_bullets())
        self.assertEqual(len(self.bullets.get_bullets()), 0)

    def test_maximum_threshold(self):
        for i in range(11):
            x = random.randint(0, 200)
            y = random.randint(0, 200)

            self.bullets.add(Bullet(x, y))

        self.assertEqual(len(self.bullets.get_bullets()), 10)

    def test_out_of_screen_bullet(self):
        bullets = Bullets()
        bullet_out_of_screen = Bullet(400, -1)

        bullets.add(bullet_out_of_screen)

        bullets.update()

        self.assertEqual(len(bullets.get_bullets()), 0)

unittest.main()
