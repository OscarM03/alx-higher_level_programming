"""Rectangle units tests"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """
    Test suite for the Rectangle class, a subclass of the Base class,
    which represents rectangles with width, height, and optional x,
    y coordinates.
    """

    def test_if_subclass(self):
        """
        Test if Rectangle is a subclass of Base.
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_2_args(self):
        """
        Test the creation of a Rectangle with two arguments
        (width and height).
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, Base._Base__nb_objects)

    def test_1_arg(self):
        """
        Test that a TypeError is raised when trying to create
        a Rectangle with only one argument.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10)

    def test_no_args(self):
        """
        Test that a TypeError is raised when trying to create
        a Rectangle with no arguments.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_many_args(self):
        """
        Test the creation of a Rectangle with multiple arguments
        (width, height, x, y, and id).
        """
        r1 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 9)

if __name__ == "__main__":
    unittest.main()
