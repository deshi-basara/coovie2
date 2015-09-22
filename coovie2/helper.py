from imdbpie import Imdb
imdb = Imdb(cache=True)


class Helper(object):

    def __init__(self):
        self.imdb_top = imdb.top_250()

    def is_imdb_top(self, movie):
        if movie.title in
