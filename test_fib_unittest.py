import unittest

from fibbo import fibbo


class TestFib(unittest.TestCase):

    def test_fib_9_is_34(self):
        self.assertEqual(fibbo(9), 34)

    def test_split(self):
        with self.assertRaises(ValueError):
            fibbo(-1)


if __name__ == '__main__':
    unittest.main()
