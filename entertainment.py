import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","This is toy story line",
                        "https://upload.wikimedia.org/wikipedia/commons/3/30/Anniversery_of_the_making_of_Toy_Story_%2826485403645%29.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

minions = media.Movie("Minions","Minions story line",
                      "https://upload.wikimedia.org/wikipedia/commons/2/2d/DHS_ToyStoryMidwayMania.jpg",
                      "https://www.youtube.com/watch?v=qTSDL94_Y7M")


movies = [toy_story,minions]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)

print(media.Movie.__module__)

print(media.Movie.__dict__)
print(media.Movie.__bases__)
