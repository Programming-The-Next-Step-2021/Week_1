import unittest

class TestSum(unittest.TestCase):
#this one should pass the test
    def test_sum(self):
        self.assertEqual(sum([2, 2, 3]), 7, "Correct answer is 7")
#this one should not pass the test (testing the test in this case..)
    def test_sum_opposite(self):
        self.assertEqual(sum((1, 2, 3)), 7, "Correct answer is 7")

if __name__ == '__main__':
    unittest.main()
