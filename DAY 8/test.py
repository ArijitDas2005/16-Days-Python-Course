import unittest
import change_text


class TestChangeText(unittest.TestCase):

    def test_uppercase(self):
        word='study'
        result=change_text.all_capitals(word)
        self.assertEqual(result,'Study')


if __name__ == '__main__':
    unittest.main()
