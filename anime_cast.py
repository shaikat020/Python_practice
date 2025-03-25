#pip install IMDbPY
from imdb import IMDb

def get_anime_cast_with_voice_actor():
    anime_name = input("Enter the name of the anime: ")
    ia = IMDb()
    
    # Search for the anime on IMDb
    movies = ia.search_movie(anime_name)

    if movies:
        movie = movies[0]  # Selecting the first search result
        ia.update(movie)
        if 'Animation' in movie.get('genres', []):
            cast = movie.get('cast', [])
        
            if cast:
                print(f"The main cast of '{anime_name}' is:")
                for actor in cast[:10]: 
                    character_name = actor.currentRole
                    actor_name = actor['name']
                    print(f"- {character_name}: {actor_name}")
            else:
                print(f"No cast information found for '{anime_name}'.")
        else:
            print(f"'{anime_name}' is not recognized as an anime!")
    else:
        print(f"Anime '{anime_name}' not found!")

get_anime_cast_with_voice_actor()
