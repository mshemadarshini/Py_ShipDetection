import unittest
from Ship_Statistic import MyShip_DB


def fun(x):
    return x + 1

class MyTest_ship(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)