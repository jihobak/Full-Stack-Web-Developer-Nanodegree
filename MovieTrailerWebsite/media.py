import webbrowser


class Movie():
    """This class provides a way to store movie related information

    Attributes:
        movie_title (str): the title of movie
        movie_storyline (str): plot of the movie
        poster_image (str): URL of image that used for movie poster
        trailer_youtube (str): URl of movie trailer in Youtube
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Inits class Movie with Attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ open the movie trailer in Youtube"""
        webbrowser.open(self.trailer_youtube_url)
