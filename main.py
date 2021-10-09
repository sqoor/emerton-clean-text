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
    write_file(first_10_words, args.output)


def read_file(input_path):
    """
    Description: read a file at specific path, if existed and have permissions.
    :param input_path:  str - The path to a file contains a string to be read.
    :return: str - The string read from the file.
    """
    try:
        file = open(input_path, "r")
        return file.read()
    except FileNotFoundError as err:
        print(f'Error input file, No such file or directory "{input_path}"')
    except PermissionError as err:
        print(f'Error input file, No permissions to read the file "{input_path}')
    except Exception as err:
        print('Something went wrong:', err)
    exit()


def create_words_frequencies(str_array):
    """
    Description: Read an array of strings then clean the strings thus it will be split on each special
    character except hyphen and apostrophe, then calculate their unique words frequencies
    and save in the dictionary as {word: str: occurrences: int}.
    :param str_array: str - An array of strings to be analysed.
    :return dict{str, int}: A dictionary consist of words as key and its frequency as value. {str: int, ...}
    """
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
    """
    Description: take a string and split this string on special characters except hyphen and apostrophe.
    :param string: str - a string to be split on special characters.
    :return: array[str]: return an array of strings after split the original string.
    """
    return re.split(r'(?:[^-\'a-zA-Z0-9]|[.]\s)+', string)


def sort_dict(words_frequencies):
    """
    Description: sort a dictionary of key/value pairs descendingly based on the value which is an integer.
    :param words_frequencies: dict{str: int} key/value pairs as {word: frequency}.
    :return: dict{str, int}: a stored dictionary descendingly.
    """
    sorted_tuple = sorted(words_frequencies.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_tuple)


def take_first(n_words, words_frequencies):
    """
    Description: take first 'n' items (key/value) pairs from a dictionary and return it. if the total size was smaller
    the required n_words then return the original size in total.
    :param n_words: int - number of elements you want to return from a dictionary.
    :param words_frequencies: dict{str, int} a dictionary to take key/value paris from.
    :return: dict{str, int} an 'n' values from a dictionary.
    """
    return words_frequencies if len(words_frequencies) <= n_words else take(n_words, words_frequencies.items())


def take(n, iterable):
    """
    Description: Return first n items of the iterable as a dict
    :param n: number of items to take
    :param iterable: 
    :return: dictionary
    """
    return dict(islice(iterable, n))


def print_console(words_dict):
    """
    Description: Print a dictionary of key value paris.
    :param words_dict: dict{str, int} a dictionary of key/value pairs which has word/frequency of the words
    :return: None
    """
    print('Most frequent words list:')
    for word in words_dict:
        print(word, f'({words_dict[word]})')


def write_file(words_dict, output_path):
    """
    Description: Write list of words in a certain format on a file on a certain path,
    if the file not existed then create,
    the path directories and file itself should be existed and have permissions to overwrite it.
    :param words_dict: dict{str: int} - a dictionary represent a list of words and their frequencies.
    :param output_path: str - string represents the path to an output path.
    :return: None
    """
    try:
        with open(output_path, 'w') as file:
            for word in words_dict:
                file.write(f'{word} ({words_dict[word]})\n')
        print(f'results saved to: "{output_path}"')
    except FileNotFoundError as err:
        print(f'Error output file, No such directory "{output_path}"')
    except PermissionError as err:
        print(f'Error output file, No permissions to write over the file "{output_path}')
    except Exception as err:
        print('Error output file, Something went wrong:', err)
    exit()


if __name__ == "__main__":
    main()





