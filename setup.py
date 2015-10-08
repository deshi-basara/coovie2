from distutils.core import setup
setup(
    name="coovie2",
    packages=["coovie2"],
    version="0.0.1",
    desciption="Cli tool for listing movies inside a path according to their" +
               "IMDb-rating",
    author="Deshi Basara",
    author_email="dorschbert@googlemail.com",
    url="https://github.com/deshi-basara/coovie2",
    install_requires=[
        "Click",
        "termcolor",
        "imdbpie",
        "requests",
        "BeautifulSoup"
    ],
    entry_points='''
        [console_scripts]
        coovie2=coovie2:main
    '''
)
