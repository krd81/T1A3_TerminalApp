import json

# Program to run a loop to obtain all genres within the film listings
# Dictionary will be used as it does not allow duplicates

def get_data(filename):
    genres = []
    with open (filename) as f:
        movies = json.load(f)


    for i in movies:
        this_genre = i.get('genres')
        g = 0
        while g < len(this_genre):
            if this_genre[g] in genres:
                pass
            else:
                genres.append(this_genre[g])
            g += 1

    return genres


genres = get_data('movies.json')

with open ('genre_list.json', 'x') as f:
        json.dump(genres, f, indent = 2)


