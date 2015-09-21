from imdbpie import Imdb
imdb = Imdb(anonymize=True)


class Movie(object):

    def __init__(self, title, year, path):
        self.title = title
        self.year = year
        self.path = path
        self.rating = 0

    def fetch_rating(self):
        search_results = imdb.search_for_title(self.title)

        # if we have more than one result, try to get the result by year
        for search in search_results:
            if search["year"] == self.year:
                # seems to be the searched movie, request rating
                title_result = imdb.get_title_by_id(search["imdb_id"])
                self.title = title_result.title
                self.rating = title_result.rating
                break

    def print_data(self):
        data_str = "{rating} | {title} ({year}) | {path}".format(
            rating=("%.1f" % self.rating),  # add floating number
            title=self.title,
            year=self.year,
            path=self.path
        )
        print(data_str)
