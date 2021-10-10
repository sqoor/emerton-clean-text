import unittest
import os
from classes.file import File
from argparse import Namespace

'''
Testing methods in File class

to run the test cases in this file.
python -m unittest test/test_file.py
'''

INPUT_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'input-test-file.txt')
OUTPUT_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'output-test-file.txt')


class MyTest(unittest.TestCase):
    def setUp(self):
        self.input_testfile = open(INPUT_DATA_FILENAME)
        self.actual_str_file = self.input_testfile.read()

        args = Namespace(input=INPUT_DATA_FILENAME, output=OUTPUT_DATA_FILENAME)
        self.file = File(args)

        self.words = {
            'i': 3, 'here': 2, 'random': 2, 'are': 1
        }
        self.actual_words_from_file = '''
        i (3)
        here (2)
        random (2)
        are (1)
        '''

    def tearDown(self):
        self.input_testfile.close()
        # os.remove(OUTPUT_DATA_FILENAME)

    def test_read_input(self):
        method_str_file = self.file.read_input()
        self.assertEqual(self.actual_str_file, method_str_file)

    # def test_write_output(self):
    #     self.file.write_output(self.words)
    #     method_created_file = open(OUTPUT_DATA_FILENAME, "r")
    #     method_created_file_str = method_created_file.read()
    #     method_created_file.close()
    #     print(method_created_file_str, self.words)
    #     self.assertEqual(method_created_file_str, self.words)


if __name__ == '__main__':
    unittest.main()
