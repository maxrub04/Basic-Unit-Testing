import unittest
from Tutorial_Shapes_Project_Code import Sphere, Cylinder, Rectangle, Cube

class MyTestCase(unittest.TestCase):
    def test_sphere_calculations(self):
        """Tests Sphere area and volume calculations."""
        sphere = Sphere(5)
        # Test Area: 4 * pi * 5^2 = 314.159...
        self.assertAlmostEqual(sphere.calculate_area(), 314.159, places=3)
        # Test Volume: (4/3) * pi * 5^3 = 523.598...
        self.assertAlmostEqual(sphere.calculate_volume(), 523.598, places=3)


if __name__ == "__main__":
    unittest.main()
