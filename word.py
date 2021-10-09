from re import split
from itertools import islice


class Word:
    def __init__(self, file_string):
        self.words_array = file_string.lower().split()

    def create_words_frequencies(self):
        """
        Description: Read an array of strings then clean the strings thus it will be split on each special
        character except hyphen and apostrophe, then calculate their unique words frequencies
        and save in the dictionary as {word: str: occurrences: int}.
        :return dict{str, int}: A dictionary consist of words as key and its frequency as value. {str: int, ...}
        """
        words_frequencies = {}

        for non_cleaned_string in self.words_array:
            words_split_on_special_chars = self.clean_string(non_cleaned_string)

            for word in words_split_on_special_chars:
                if word in words_frequencies and not word == '':
                    words_frequencies[word] = words_frequencies[word] + 1
                else:
                    words_frequencies[word] = 1

        return words_frequencies

    def clean_string(self, string):
        """
        Description: take a string and split this string on special characters except hyphen and apostrophe.
        :param string: str - a string to be split on special characters.
        :return: array[str]: return an array of strings after split the original string.
        """
        return split(r'(?:[^-\'a-zA-Z0-9]|[.]\s)+', string)

    def sort_dict(self, words_frequencies, desc=True):
        """
        Description: sort a dictionary of key/value pairs ascendingly/descendingly based on the value which is an integer and 'desc' parameter.
        :param desc: bool - True means sort descendingly, False sort ascendingly.
        :param words_frequencies: dict{str: int} key/value pairs as {word: frequency}.
        :return: dict{str, int}: a stored dictionary descendingly.
        """
        sorted_tuple = sorted(words_frequencies.items(), key=lambda item: item[1], reverse=desc)
        return dict(sorted_tuple)

    def take_first(self, n_words, words_frequencies):
        """
        Description: take first 'n' items (key/value) pairs from a dictionary and return it.
        if the total size was smaller the required n_words then return the original size in total.
        :param n_words: int - number of elements you want to return from a dictionary.
        :param words_frequencies: dict{str, int} a dictionary to take key/value paris from.
        :return: dict{str, int} an 'n' values from a dictionary.
        """
        return words_frequencies if len(words_frequencies) <= n_words else self.take(n_words, words_frequencies.items())

    def take(self, num_items, iterable):
        """
        Description: Return first n items of the iterable as a dict
        :param num_items: number of items to take
        :param iterable:
        :return: dictionary
        """
        return dict(islice(iterable, num_items))
