import argparse

""" Documentation
    Description:
        Argument is a class with one static method get(), used to read all the arguments from the command line/terminal 
        and read the values and use it in this script, all the arguments related to connecting to the database.
        Verbose flag used to print to the console the status of the script (i.e connected to db, view updated,... etc)

        List of parameters:
            --input='path-to-input-file'
            --output='path-to-output-file'
        or you can use the shortcut
            -i='path-to-input-file'
            -o='path-to-output-file'

        All the parameters are required to run this script, except verbose flag.

    Returns:
      object: has the list of parsed argument from CMD/terminal so it will be used later in this script.
"""


class Argument:
    @staticmethod
    def get():
        parser = argparse.ArgumentParser(
            description="A program that counts unique words from an English text file, "
                        "treating hyphen and apostrophe as part of the word. "
                        "The program output the ten most frequent words "
                        "and mention the number of occurrences"
            # , exit_on_error=True
        )

        parser.add_argument(
            '-i',
            '--input',
            help='Path to the file to read from.',
            required=True
        )
        parser.add_argument(
            '-o',
            '--output',
            help='Path to the file to save result to, if not existed it will be created at the specified path '
                 'or at current directory',
            required=True
        )
        # parser.add_argument(
        #     '-v',
        #     '--verbose',
        #     help='it will print descriptive messages of the script status, if it was provided.',
        #     nargs='?',
        #     const=True,
        #     type=bool
        # )

        return parser.parse_args()

