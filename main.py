from classes.argument import Argument
from classes.file import File
from classes.word import Word


__author__ = "Sqoor"
__version__ = "0.1.0"
__license__ = "Emerton"


class Starter:
    def main(self):
        args = Argument.get()

        file = File(args)
        file_string = file.read_input()

        word = Word(file_string)
        words_frequencies = word.create_words_frequencies()
        sorted_words_frequencies = word.sort_dict(words_frequencies)
        first_10_words = word.take_first(10, sorted_words_frequencies)

        self.__print_console(first_10_words)
        file.write_output(first_10_words)

    def __print_console(self, words_dict):
        """
        Description: Print a dictionary of key value paris.
        :param words_dict: dict{str, int} a dictionary of key/value pairs which has word/frequency of the words
        :return: None
        """
        print('Most frequent words list:')
        for word in words_dict:
            print(word, f'({words_dict[word]})')
        print('')


if __name__ == '__main__':
    starter = Starter()
    starter.main()





