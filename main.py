import json
import re
from itertools import islice
from argument import Argument


def main():
    args = Argument.get()

    file_string = read_file(args.input)
    words_array = file_string.lower().split()

    words_frequencies = create_words_frequencies(words_array)
    sorted_words_frequencies = sort_dict(words_frequencies)
    first_10_words = take_first(10, sorted_words_frequencies)

    print_console(first_10_words)
    write_file(args.output, first_10_words)


def read_file(path):
    """
        path: str
            The path to a file contains a string to be read
        Return str
            The string read from the file
    """
    file = open(path, "r")
    return file.read()


def create_words_frequencies(str_array):
    words_frequencies = {}

    for non_cleaned_string in str_array:
        words_split_on_special_chars = clean_string(non_cleaned_string)

        for word in words_split_on_special_chars:
            if word in words_frequencies and not word == '':
                words_frequencies[word] = words_frequencies[word] + 1
            else:
                words_frequencies[word] = 1

    return words_frequencies


def clean_string(string):
    return re.split(r'(?:[^-\'a-zA-Z0-9]|[.]\s)+', string)


def sort_dict(words_frequencies):
    sorted_tuple = sorted(words_frequencies.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_tuple)


def take_first(n_words, words_frequencies):
    return words_frequencies if len(words_frequencies) <= n_words else take(n_words, words_frequencies.items())


def take(n, iterable):
    """Return first n items of the iterable as a dict"""
    return dict(islice(iterable, n))


def print_console(words_dict):
    for word in words_dict:
        print(word, f'({words_dict[word]})')


def write_file(output_path, words_dict):
    with open(output_path, 'w') as file:
        for word in words_dict:
            file.write(f'{word} ({words_dict[word]})\n')


if __name__ == "__main__":
    main()





