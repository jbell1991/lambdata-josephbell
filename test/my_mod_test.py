import unittest

from lambdata_jbell1991.my_mod import enlarge

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(enlarge(4), 400)


if __name__ == '__main__':
    unittest.main()