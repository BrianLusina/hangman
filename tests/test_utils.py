import unittest
from hangman.utils import join_guessed_letters


class UtilsTestCase(unittest.TestCase):
    def test_join_guessed_letters(self):
        letters = {"a", "b", "c", "d"}
        expected = 'a b c d'
        actual = join_guessed_letters(letters)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
