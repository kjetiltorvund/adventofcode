import unittest
from main import part2

class TestDailRotationPart2(unittest.TestCase):
    def test_should_count_once_when_hitting_zero_once(self):
        data:list = ["L10"]

        actual = part2(data, 10, 100)

        self.assertEqual(actual, 1)

    def test_should_count_zero_when_stopping_in_zero(self):
        data:list = ["L10", "L5", "R5"]

        actual = part2(data, 10, 100)

        self.assertEqual(actual, 2)

    def test_should_count_zero_when_only_passing(self):
        data:list = ["L15", "R15", "L20", "R40"]

        actual = part2(data, 10, 100)

        self.assertEqual(actual, 4)


    def test_should_manage_test_case(self):
        data:list = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

        actual = part2(data, 50, 100)

        self.assertEqual(actual, 6)

    
    def test_should_rotate_thousand_times(self):
        data:list = ["L1000"]

        actual = part2(data, 50, 100)

        self.assertEqual(actual, 10)


    def test_should_count_when_landing_on_zero(self):
        data:list = ["L30", "R48", "L5", "R60", "L55"]

        actual = part2(data, 82, 100)

        self.assertEqual(actual, 3)

if __name__ == '__main__':
    unittest.main()