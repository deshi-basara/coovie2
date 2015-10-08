coovie2
=======

Coovie is a python Cli-tool for listing movies inside a specified path according to their IMDb-rating. Movies that are inside the IMDb-Top 250 are highlighted.

Rankings are captured via imdbpie's iPhone api. If a movie title can't be found with the build-in iPhone-search, startpage.com is used to get the IMDb-id.


================
### Dependencies
The following dependencies are needed globally

* Python (3.4) ~ tested

Dev dependencies
* Virtualenv


=========
### Setup

Create a new virtualenv with Python 3.4 and activate
```Shell
$  virtualenv -p /usr/bin/python3.4 venv
$  . venv/bin/activate
```


Install coovie2 in your virtual environment (or globally)
```Shell
(venv)[coovie2]$  python setup.py install

or (if you want to modify the code)

(venv)[coovie2]$  pip install --editable .
```


=========
### Usage

To see all available arguments and options enter
```Shell
(venv)[coovie2]$ python coovie2.py --help

Usage: coovie2.py [OPTIONS] SEARCH_PATH

Options:
  --endings TEXT     File-endings that are accepted as valid movie-files.
                     Default: [.mkv, .mp4]
  --size_limit TEXT  Smaller files are excluded from search (in MegaBytes).
                     Default: 1500
  --help             Show this message and exit.
```

Example search
```Shell
(venv)[coovie2]$  python coovie2.py --size_limit 5000 --endings "mkv, mp4, ts" /run/media/user/1080p/
```


You should get a result-list like
```Shell
8.5 | Cinema Paradiso (1988)                 | /run/media/user/1080p/Cinema.Paradiso.1988.German.AC3D.DL.1080p.x264-xXx
8.5 | 3 Idiots (2009)                        | /run/media/user/1080p/3.Idiots.2009.1080p.BluRay.x264-xXx
8.1 | Nausicaae aus dem Tal der Winde (1984) | /run/media/user/1080p/Nausicaae.aus.dem.Tal.der.Winde.1984.1080p.BluRay.AC3.ML.x264-xXx
8.1 | Tenku no shiro Rapyuta (1986)          | /run/media/user/1080p/Das.Schloss.im.Himmel.1986.1080p.BluRay.AC3.DTS.ML.x264-xXx
7.7 | Fearless DC (2006)                     | /run/media/user/1080p/Fearless 1080p
7.5 | The Proposition (2005)                 | /run/media/user/1080p/The.Proposition.2005.German.AC3D.DL.1080p.BluRay.x264-xXx
```
