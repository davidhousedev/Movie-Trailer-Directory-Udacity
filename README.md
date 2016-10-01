# Movie-Trailer-Directory-Udacity
A simple python-based web page with dynamically generated movie listings and links to their trailers.

### Requirements:
So long as you plan to run the server locally, all you need is a working Python installation. The project was developed on Python 2.7.9 and has not been tested on any later versions.

### Configuration:
The site will display a list of movies or television shows populated within `movie_server.py`.
To customize this list, define either `Movie` or `TvShow` objects within `def doGET(self)`, then add them to the `videos` list.

Both `Movie` and `TvShow` classes are initialized with two inputs:
	1. the title of the movie or show as a plain text string
	2. the URL to the corresponding Youtube trailer

### Starting the server:
The server is started by running `movie_server.py`. Navigate to the folder containing it, then run:

```python movie_server.py```

You will see a confirmation: `serving at port 8000`. The server can then be accessed through your web at:

```http://localhost:8000```
