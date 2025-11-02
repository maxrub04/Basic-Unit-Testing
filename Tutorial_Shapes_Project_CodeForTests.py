import unittest
from Tutorial_Shapes_Project_Code import Sphere, Cylinder, Rectangle, Cube

class MyTestCase(unittest.TestCase):
    def test_sphere_calculations(self):
        """Tests Sphere area and volume calculations."""
        sphere = Sphere(5)
        # Test Area: 4 * pi * 5^2 = 314.159...
        self.assertAlmostEqual(sphere.calculate_area(), 314.159, places=3)
        # Test Volume: (4/3) * pi * 5^3 = 523.598...
        self.assertAlmostEqual(sphere.calculate_volume(), 523.598, delta=0.001)

    def test_cylinder_calculations(self):
        """Tests Cylinder area and volume."""
        cylinder = Cylinder(3, 7)
        # Test Area: 2 * pi * 3 * (3 + 7) = 188.495...
        self.assertAlmostEqual(cylinder.calculate_area(), 188.496, places=3)
        # Test Volume: pi * 3^2 * 7 = 197.920...
        self.assertAlmostEqual(cylinder.calculate_volume(), 197.920, delta=0.001)

    def test_rectangle_calculations(self):
        """Tests Rectangle area and volume."""
        rectangle = Rectangle(4, 8)
        # Test Area: 4 * 8 = 32
        self.assertEqual(rectangle.calculate_area(), 32)
        # Test Volume: 2D shape is 0
        self.assertEqual(rectangle.calculate_volume(), 0)

    def test_cube_calculations(self):
        """Tests Cube area and volume."""
        cube = Cube(4)
        # Test Area: 6 * 4^2 = 96
        self.assertEqual(cube.calculate_area(), 96)
        # Test Volume: 4^3 = 64
        self.assertEqual(cube.calculate_volume(), 64)

    def test_invalid_inputs(self):
        """Tests for invalid (zero or negative) inputs. """
        with self.assertRaises(ValueError):
            Sphere(0)
        with self.assertRaises(ValueError):
            Sphere(-5)

        with self.assertRaises(ValueError):
            Cylinder(1, -1)
        with self.assertRaises(ValueError):
            Cylinder(-1, 1)
        with self.assertRaises(ValueError):
            Cylinder(0, 5)

        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(-5, 5)

        with self.assertRaises(ValueError):
            Cube(-10)


if __name__ == "__main__":
    unittest.main()
