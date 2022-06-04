import unittest

from calculator import operations


class Test(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test
        """
        pass

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_add_numbers(self):
        result = operations.add_numbers(20, 20)
        self.assertEqual(result, 40)

    def test_add_numbers_strA(self):
        with self.assertRaises(Exception, msg='your exception message'):
            operations.add_numbers("text", 20)

    def test_add_numbers_strB(self):
        with self.assertRaises(Exception, msg='your exception message'):
            operations.add_numbers(20, "text")

    def test_sub_numbers(self):
        result = operations.sub_numbers(20, 10)
        self.assertEqual(result, 10)

    def test_sub_numbers_strA(self):
        with self.assertRaises(Exception, msg='your exception message'):
            operations.sub_numbers("text", 20)

    def test_sub_numbers_strB(self):
        with self.assertRaises(Exception, msg='your exception message'):
            operations.sub_numbers(20, "text")

    def test_public(self):
        self.assertRaises(TypeError, operations.add_numbers(10, 10))
        self.assertRaises(TypeError, operations.sub_numbers(10, 10))


if __name__ == '__main__':
    unittest.main()
