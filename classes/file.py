"""
Description: class meant to deal with files withing this small project, so it should read from files and write to others
:param: args arguemnts read from the CLi provided by the user to read the path to input file args.input and output file args.output
:method:
    + read_input
    + write_output
"""

class File:
    def __init__(self, args):
        self.input_path = args.input
        self.output_path = args.output

    def read_input(self):
        """
        Description: read a file at specific path, if existed and have permissions.
        :return: str - The string read from the file.
        """
        try:
            file = open(self.input_path, "r")
            str_file = file.read()
            if len(str_file) < 1:
                print(f'Exit, the provided file "{self.input_path}" is empty!')
                exit()
            return str_file
        except FileNotFoundError as err:
            print(f'Error input file, No such file or directory "{self.input_path}"')
        except PermissionError as err:
            print(f'Error input file, No permissions to read the file "{self.input_path}')
        except Exception as err:
            print('Something went wrong:', err)
        exit()

    def write_output(self, words_dict):
        """
        Description: Write list of words in a certain format on a file on a certain path,
        if the file not existed then create,
        the path directories and file itself should be existed and have permissions to overwrite it.
        :param words_dict: dict{str: int} - a dictionary represent a list of words and their frequencies.
        :return: None
        """
        try:
            with open(self.output_path, 'w') as file:
                for word in words_dict:
                    file.write(f'{word} ({words_dict[word]})\n')
            self.output_path = self.output_path if './' in self.output_path else './' + self.output_path
            print(f'results saved to: "{self.output_path}"')
        except FileNotFoundError as err:
            print(f'Error output file, No such directory "{self.output_path}"')
        except PermissionError as err:
            print(f'Error output file, No permissions to write over the file "{self.output_path}')
        except Exception as err:
            print('Error output file, Something went wrong:', err)
        exit()
