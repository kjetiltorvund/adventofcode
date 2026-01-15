import unittest
from main import part1
from main import part2

class TestMainPar1(unittest.TestCase):

    def test_testinput(self):
        data_file = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

        data:list = data_file.split(",")

        actual = part1(data)

        self.assertEqual(actual, 1227775554)

    def test_testinput_for_part2(self):

        answer = 4174379265

        data_file = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

        data:list = data_file.split(",")

        actual = part2(data)

        self.assertEqual(actual, answer)


    def test_should_pick_99_and_111(self):

        data:list = ["95-115"]

        actual = part2(data)

        self.assertEqual(actual, 210)

    def test_should_pick_999_adn_1010(self):
        data:list = ["998-1012"]

        actual = part2(data=data)

        self.assertEqual(actual, 2009)

    def test_regex_for_1010(self):
        import re
        matches = re.findall("10", "1010")

        self.assertEqual(len(matches), 2) 

    def test_long_pattern_match(self):
        data:list = ["1188511880-1188511890"]

        actual = part2(data)

        self.assertEqual(actual, "1188511885")


#if __name__ == '__main__':
    #unittest.main()
    
    # tester = TestMainPar1(unittest.TestCase)
    # tester.test_should_pick_99_and_110()