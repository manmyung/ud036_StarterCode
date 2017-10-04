class Movie:
    """Movie class for Movie trailer website

    Attributes:
        title: Movie title.
        poster_image_url: Front image.
        trailer_youtube_url: Video URL.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
