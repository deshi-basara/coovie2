from imdbpie import Imdb
from bs4 import BeautifulSoup
from termcolor import colored
import requests
imdb = Imdb(cache=True)


class Movie(object):
    def __init__(self, title, year, path, folder):
        self.title = title
        self.original_title = ""
        self.year = year
        self.path = path
        self.folder = folder
        self.rating = 0
        self.imdb_top = False

    def fetch_rating(self):
        print("Fetching: " + self.title + " ...")
        search_results = imdb.search_for_title(self.title)

        # try to get the result by year
        for search in search_results:
            if search["year"] == self.year:
                # seems to be the searched movie, request rating
                title_result = imdb.get_title_by_id(search["imdb_id"])
                self.original_title = title_result.title
                self.rating = title_result.rating
            else:
                # use startpage.com to find the imdb-id
                self.fetch_rating_startpage()

    def fetch_rating_startpage(self):
        # no imdb entry found for title, try to find imdb-entry via search-
        # engines
        search_engine = "https://startpage.com/do/metasearch.pl"
        search_payload = {
            "hmb": "1",
            "cat": "web",
            "cmd": "process_search",
            "language": "deutsch",
            "engine0": "v1all",
            "abp": "-1",
            "nj": "0",
            "query": self.title + " " + self.year + " imdb",
            "pg": "0"
        }
        search_request = requests.post(search_engine, search_payload)

        # valid response?
        if search_request.status_code == 200:
            # parse html-result and get the best search result
            startpage_html = str(search_request.text)
            soup = BeautifulSoup(startpage_html, "lxml")
            first_result = soup.find(id="first-result").a["href"]

            # is valid imdb string?
            imdb_url = "http://www.imdb.com/title/"
            if imdb_url in first_result:
                imdb_id = first_result.replace(imdb_url, "")
                imdb_id = imdb_id.replace("/", "")

                # seems to be the searched movie, request rating
                title_result = imdb.get_title_by_id(imdb_id)
                self.original_title = title_result.title
                self.rating = title_result.rating

    def print_data(self, longest_title):
        data_str = "{rating} | {title} {year: <0{padding}} | {path}".format(
            rating=("%.1f" % self.rating),  # add floating number
            title=self.title,
            padding=longest_title - (len(self.title) - 6),
            year="("+self.year+")",
            path=self.folder
        )

        if self.imdb_top:
            data_str_colored = colored(data_str, "yellow")
            print(data_str_colored)
        else:
            print(data_str)
