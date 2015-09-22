import os
import re


class Scan(object):

    def __init__(self, endings, size_limit):
        self.movie_endings = endings
        self.movie_size_limit = size_limit

    def is_movie(self, file_name):
        '''
        Checks weather a handed file is a movie-file by validating its ending.
        '''
        if file_name.endswith(self.movie_endings):
            return True
        else:
            return False

    def is_large(self, file_path):
        file_stat = os.stat(file_path)
        file_size = file_stat.st_size

        # convert predefined-settings to bytes and compare
        """compare_str = '{size} >= {limit}'.format(
            size=file_size,
            limit=movie_size_limit
        )
        print(compare_str)
        """
        if file_size >= self.movie_size_limit:
            return True
        else:
            return False

    def extract_file_data(self, file, folder):
        '''
        Extract a movie name and year from folder or file
        '''

        # shall we use folder-name or file-name (-4 characters for file-
        # extension)
        base_name = folder
        if len(base_name) < (len(file) - 4):
            base_name = file

        # find first digit and use it for extracting movie name
        first_digit = -1
        first_regex = (re.search('\d{4}', base_name))
        if first_regex:
            first_digit = first_regex.start()

        # extract name and year
        if first_digit != -1:
            extracted_name = base_name[:first_digit-1]  # remove dot
            extracted_year = base_name[first_digit:first_digit+4]
        else:
            extracted_name = base_name
            extracted_year = -1

        name = extracted_name.replace('.', ' ')
        year = extracted_year
        return [name, year]
