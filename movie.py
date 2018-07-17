import webbrowser


class Movie():
    def __init__(self,movie_name,movie_desc, movie_poster, movie_trailer):
        self.moviename = movie_name
        self.moviedesc = movie_desc
        self.movieposter = movie_poster
        self.movietrailer = movie_trailer

    def playTrailer(self):
        webbrowser.open(self.movietrailer, new=1)
    def displayPoster(self):
        webbrowser.open(self.movieposter, new=1)

