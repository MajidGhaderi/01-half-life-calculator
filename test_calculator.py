import unittest

from calculator import (calculate_half_life, calculate_elimination_rate_constant, calculate_concentration, calculate_concentration_over_time)


class TestCalculator(unittest.TestCase):

    def test_calculate_half_life(self):
        result = calculate_half_life(0.2)

        self.assertAlmostEqual(result, 3.4657, places=4)

    def test_half_life_invalid_k(self):
        with self.assertRaises(ValueError):
            calculate_half_life(-0.2)

    def test_calculate_elimination_rate_constant(self):
        result = calculate_elimination_rate_constant(4)

        self.assertAlmostEqual(result, 0.1733, places=4)

    def test_elimination_rate_constant_invalid_half_life(self):
        with self.assertRaises(ValueError):
            calculate_elimination_rate_constant(-4)

    def test_calculate_concentration(self):
        result = calculate_concentration(100, 0.2, 5)

        self.assertAlmostEqual(result, 36.7879, places=4)

    def test_concentration_invalid_initial_concentration(self):
        with self.assertRaises(ValueError):
            calculate_concentration(-100, 0.2, 5)

    def test_concentration_invalid_k(self):
        with self.assertRaises(ValueError):
            calculate_concentration(100, -0.2, 5)

    def test_concentration_negative_time(self):
        with self.assertRaises(ValueError):
            calculate_concentration(100, 2, -5)

    def test_calculate_concentration_over_time(self):
        times = [0, 1, 2]

        result = calculate_concentration_over_time(100, 0.2, times)

        self.assertEqual(len(result), 3)

        self.assertAlmostEqual(result[0], 100, places=2)
        self.assertAlmostEqual(result[1], 81.87, places=2)
        self.assertAlmostEqual(result[2], 67.03, places=2)

if __name__ == "__main__":
    unittest.main()
        


