import unittest
import calc

# Note: Tests can be executed using:
# python -m unittest test_calc.py


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
