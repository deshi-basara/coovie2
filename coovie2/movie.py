from imdbpie import Imdb
imdb = Imdb(anonymize=True)


class Movie(object):

    def __init__(self, title, year, path, folder):
        self.title = title
        self.year = year
        self.path = path
        self.folder = folder
        self.rating = 0

    def fetch_rating(self):
        search_results = imdb.search_for_title(self.title)

        # try to get the result by year
        for search in search_results:
            if search["year"] == self.year:
                # seems to be the searched movie, request rating
                title_result = imdb.get_title_by_id(search["imdb_id"])
                self.title = title_result.title
                self.rating = title_result.rating
                break

    def print_data(self, longest_title):
        data_str = "{rating} | {title} {year: <0{padding}} | {path}".format(
            rating=("%.1f" % self.rating),  # add floating number
            title=self.title,
            padding=longest_title - (len(self.title) - 6),
            year="("+self.year+")",
            path=self.folder
        )
        print(data_str)
