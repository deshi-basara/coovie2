
import os
import click
from movie import Movie
from scan import Scan
from helper import Helper


@click.command()
@click.option('--endings',
              default='mp4, mkv',
              help='File-endings that are accepted as valid movie-files. ' +
              'Default: [.mkv, .mp4]'
              )
@click.option('--size_limit',
              default="1500",
              help='Smaller files are excluded from search (in MegaBytes). ' +
              "Default: 1500")
@click.argument('search_path', required=True)
def main(endings, size_limit, search_path):
    # initiate global function variables
    movie_list = []
    longest_title = 0

    # initiate options & arguments from cli
    movie_endings = tuple(endings.split(", "))
    movie_size_limit = int(size_limit) * 1024 * 1024  # MegaBytes

    # initiate needed objects
    scanner = Scan(movie_endings, movie_size_limit)
    helper = Helper()

    # look for all available files inside directory recursively
    for root, subs, files in os.walk(search_path):
        # do available files match a movie-file?
        for file in files:
            # is movie file?
            bool_movie = scanner.is_movie(file)

            if not bool_movie:
                continue

            # is large enough?
            movie_path = os.path.join(root, file)
            movie_folder = os.path.basename(root)
            bool_large = scanner.is_large(movie_path)
            if not bool_large:
                continue

            # is movie file and large enough, try to extract a valid movie name
            extracted_data = scanner.extract_file_data(file, movie_folder)

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
    for movie in movie_list:
        movie.fetch_rating()
        # is current movie in top 250
        movie.imdb_top = helper.is_imdb_top(movie)

    # sort movies by their rating and print them
    print("")
    movie_list.sort(key=lambda x: x.rating, reverse=True)
    for movie in movie_list:
        movie.print_data(longest_title)

if __name__ == '__main__':
    main()
