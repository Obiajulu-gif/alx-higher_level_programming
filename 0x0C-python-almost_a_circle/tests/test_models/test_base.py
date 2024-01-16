import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        b1 = Base(id=5)
        self.assertEqual(b1.id, 5)

    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 4)

    def test_constructor_with_and_without_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_with_string(self):
        b1 = Base("Hello")
        self.assertEqual(b1.id, 'Hello')

    def test_with_bool(self):
        b1 = Base(True)
        self.assertEqual(b1.id, True)


if __name__ == '__main__':
    unittest.main()