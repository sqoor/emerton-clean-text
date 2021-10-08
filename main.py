import json
import re
from itertools import islice

file = open("Tempest.txt", "r")
file_str = file.read()

arr_data = file_str.lower().split()
print('Total words count', len(arr_data))

dict_string = {}

for non_cleaned_string in arr_data:
    words_split_on_special_chars = re.split(r'(?:[^-\'a-zA-Z0-9]|[.]\s)+', non_cleaned_string)

    for word in words_split_on_special_chars:
        if word in dict_string and not word == '':
            dict_string[word] = dict_string[word] + 1
        else:
            dict_string[word] = 1

words_dict_sorted = dict(sorted(dict_string.items(), key=lambda item: item[1], reverse=True))

for word in words_dict_sorted:
    # you, to, and
    # to:   [to, stripe symbols from start and end of the words
    # and:  and's - How fares the king and's followers?
    # you:  you'ld - You'ld be king o' the isle, sirrah?
    # you,-- if you remove lines 12-19
    # graces!--and
    # so!-- and
    # and,--do
    if 'to' in word: # and output[word] == 1
        print(word, f'\t\t({words_dict_sorted[word]})')
        print('______________________________')


def take(n, iterable):
    "Return first n items of the iterable as a dict"
    return dict(islice(iterable, n))


if len(words_dict_sorted) <= 10:
    print(words_dict_sorted)
else:
    first_10_items = take(10, words_dict_sorted.items())
    for word in first_10_items:
        print(word, f'({words_dict_sorted[word]})')

# with open('output.txt', 'w') as file:
#     file.write(json.dumps(output))
