
from argument import Argument
from file import File
from word import Word


def main():
    args = Argument.get()

    file = File(args)
    file_string = file.read_input()

    word = Word(file_string)
    words_frequencies = word.create_words_frequencies()
    sorted_words_frequencies = word.sort_dict(words_frequencies)
    first_10_words = word.take_first(10, sorted_words_frequencies)

    print_console(first_10_words)
    file.write_output(first_10_words)


def print_console(words_dict):
    """
    Description: Print a dictionary of key value paris.
    :param words_dict: dict{str, int} a dictionary of key/value pairs which has word/frequency of the words
    :return: None
    """
    print('Most frequent words list:')
    for word in words_dict:
        print(word, f'({words_dict[word]})')
    print('')


if __name__ == "__main__":
    main()





