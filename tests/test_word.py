import unittest
from classes.word import Word


"""
Testing public methods in Word class

to run the test cases in this file.
python -m unittest test/test_word.py

"""


class TestWord(unittest.TestCase):
    def setUp(self):
        self.word = Word('''
            Here are some random words to test. 
            here that's were-been. 
            randomly!, random. and. I. I? I!
        ''')
        self.actual_word_freq = {
            'here': 2, 'are': 1, 'some': 1, 'random': 2, 'words': 1,
            'to': 1, 'test': 1, '': 1, "that's": 1, 'were-been': 1,
            'randomly': 1, 'and': 1, 'i': 3
        }
        self.actual_sorted_words = {
            'i': 3, 'here': 2, 'random': 2, 'are': 1, 'some': 1,
            'words': 1, 'to': 1, 'test': 1, '': 1, "that's": 1,
            'were-been': 1, 'randomly': 1, 'and': 1
        }
        self.actual_first_4_values = {
            'i': 3, 'here': 2, 'random': 2, 'are': 1
        }

    def test_create_words_frequencies(self):
        method_words_freq = self.word.create_words_frequencies()
        self.assertDictEqual(method_words_freq, self.actual_word_freq)

    def test_sort_dict(self):
        method_sorted_words = self.word.sort_dict(self.actual_word_freq)

        for (method_sorted_words_key, method_sorted_words_value), (actual_sorted_words_key, actual_sorted_words_value) \
                in zip(method_sorted_words.items(), self.actual_sorted_words.items()):
            if actual_sorted_words_value == 1 or method_sorted_words_key == 1:
                break
            self.assertEqual(method_sorted_words_key, actual_sorted_words_key)
            self.assertEqual(method_sorted_words_value, actual_sorted_words_value)

    def test_take_first(self):
        method_first_4_pairs = self.word.take_first(4, self.actual_sorted_words)
        self.assertDictEqual(self.actual_first_4_values, method_first_4_pairs)


if __name__ == '__main__':
    unittest.main()
