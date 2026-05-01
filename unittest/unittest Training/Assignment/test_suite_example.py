import unittest

class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)

class TestSubtract(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(5 - 2, 3)

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))

    runner = unittest.TextTestRunner()
    runner.run(suite)
