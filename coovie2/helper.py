from imdbpie import Imdb
imdb = Imdb(cache=True)


class Helper(object):

    def __init__(self):
        self.imdb_top = imdb.top_250()
        self.extract_titles()

    def extract_titles(self):
        self.top_titles = []
        for top_movie in self.imdb_top:
            self.top_titles.append(top_movie["title"])

    def is_imdb_top(self, movie):
        if movie.original_title in self.top_titles:
            print(movie.title + " is in 250")
            return True
        else:
            return False
