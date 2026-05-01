import unittest

class TestListOperations(unittest.TestCase):
    def setUp(self):
        self.my_list = [1, 2, 3]

    def tearDown(self):
        print("Test completed")

    def test_list_length(self):
        self.assertEqual(len(self.my_list), 3)
