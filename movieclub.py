import fresh_tomatoes
import movie

rangdebasnati  = movie.Movie('Rang De Basanti',
                             'Movie about the revolution against system',
                             'https: // www.amazon. in / Posterboy - Basanti - Poster - 30 - 48 - 45 - 72 / dp / B00GQVQXM6',
                             'https://www.youtube.com/watch?v=QHhnhqxB4E8')
aedilheymushkil = movie.Movie('Ae dil hey mushkil',
                             'Movie about the Love',
                             'https://www.google.com/search?q=ae+dil+hai+mushkil+poster&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjvvZPGl6fcAhVm7oMKHYFwAO0Q_AUICigB&biw=1920&bih=1072#imgrc=plS2mq2jWsPmrM:',
                             'https://www.youtube.com/watch?v=Z_PODraXg4E')

# rangdebasnati.playTrailer()
# rangdebasnati.displayPoster()

movies = [rangdebasnati,aedilheymushkil]
fresh_tomatoes.open_movies_page(movies)