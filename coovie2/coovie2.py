import os
import re
from movie import Movie


search_path = '/run/media/simon/emma'
movie_endings = ('.mkv', '.mp4')
movie_size_limit = 1500 * 1024 * 1024  # MegaBytes


def is_movie(file_name):
    '''
    Checks weather a handed file is a movie-file by validating its ending.
    '''
    if file_name.endswith(movie_endings):
        return True
    else:
        return False


def is_large(file_path):
    file_stat = os.stat(file_path)
    file_size = file_stat.st_size

    # convert predefined-settings to bytes and compare
    """compare_str = '{size} >= {limit}'.format(
        size=file_size,
        limit=movie_size_limit
    )
    print(compare_str)
    """
    if file_size >= movie_size_limit:
        return True
    else:
        return False


def extract_file_data(file, folder):
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


def main():
    movie_list = []
    longest_title = 0

    # look for all available files inside directory recursively
    for root, subs, files in os.walk(search_path):
        # do available files match a movie-file?
        for file in files:
            # is movie file?
            bool_movie = is_movie(file)
            if not bool_movie:
                break

            # is large enough?
            movie_path = os.path.join(root, file)
            movie_folder = os.path.basename(root)
            bool_large = is_large(movie_path)
            if not bool_large:
                break

            # is movie file and large enough, try to extract a valid movie name
            extracted_data = extract_file_data(file, movie_folder)

            """print("Extracted: " + extracted_data[0] + " | " +
                  str(extracted_data[1]))"""

            # if movie has valid data, create a new movie object
            if -1 in extracted_data:
                print("Problem with: " + extracted_data[0] + " " +
                      str(extracted_data[1]))
            else:
                # data valid, create object and append it
                movie_object = Movie(
                    extracted_data[0],
                    extracted_data[1],
                    movie_path,
                    root
                )
                movie_list.append(movie_object)

                # does the current movie have the longest title?
                if longest_title < len(movie_object.title):
                    longest_title = len(movie_object.title)

    result_str = 'Movies counted: {number}'.format(number=len(movie_list))
    print(result_str)

    # try to fetch imdb rating for each movie-object
    """for movie in movie_list:
        movie.fetch_rating()"""
    for i in range(len(movie_list)):
        movie_list[i].fetch_rating()

    movie_list.sort(key=lambda x: x.rating, reverse=True)

    for movie in movie_list:
        movie.print_data(longest_title)


if __name__ == '__main__':
    main()
