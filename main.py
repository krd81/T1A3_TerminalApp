'''
1. Create login page
    - Enter email address / password
    - If incorrect, give message, allow repeat attempts
    - If correct, display welcome message

2. Create menu
    - Search for titles, by name, genre etc
    - Check for current rentals
    - Rent title
    - Return title
    - Confirmation

3. Class for users, creates "users", updates their rental history, current rentals (recommendations?)

4. Class for titles (data required: title, genre, actors, year, runtime, rating, plot)

5. Main will be responsible for: 
    - requesting username/password
    - displaying the menu
    - adding users
    - renting/returning titles
    
'''
import json, math
class User:
    def __init__(self, id, email, first, last, company, created_at, country, password) -> None:
        self.id = id
        self.email = email
        self.first = first
        self.last = last
        self.company = company
        self.created_at = created_at
        self.country = country
        self.password = password
        self.current_rentals = []
        self.all_rentals = []
        
  

 

    def get_password(self):
        return self.password
    
    def get_firstname(self):
        return self.first

    def get_fullname(self):
        fullname = f'{self.first} {self.last}'
        return fullname
      
    def update_users(self):
        # Add rental information to user list
        pass


    # Writes data back to file when user exits
    def save_users(self):
        with open('user_list.json', 'w') as f:
            json.dumps(self.users, f, indent = 2)

'''
"title": "Airplane!",
      "year": 1980,
      "cast": [
        "genres": [
        "Comedy",
        "Satire"
      ],
      "href": "Airplane!",
      "extract": "Airplane! is a 1980 American parody film written and directed by the brothers David and Jerry Zucker, and Jim Abrahams in their directorial debuts, and produced by Jon Davison. It stars Robert Hays and Julie Hagerty and features Leslie Nielsen, Robert Stack, Lloyd Bridges, Peter Graves, Kareem Abdul-Jabbar, and Lorna Patterson. It is a parody of the disaster film genre, particularly the 1957 Paramount film Zero Hour!, from which it borrows its plot, central characters, and some dialogue. It also draws many elements from Airport 1975 and other films in the Airport series. It is known for its use of surreal humor and fast-paced slapstick comedy, including visual and verbal puns, gags, running jokes, and obscure humor.",
      "thumbnail": "https://upload.wikimedia.org/wikipedia/en/2/21/Airplane%21_%281980_film%29.jpg",
      "thumbnail_width": 258,
      "thumbnail_height": 386

'''

class Movie:
    def __init__(self, title, year, cast, genres, href, extract, thumbnail, thumbnail_width, thumbnail_height):
        self.title = title 
        self.year = year
        self.cast = cast
        self.genres = genres
        self.href = href
        self.summary = extract
        self.image = thumbnail
        self.image_width = thumbnail_width
        self.image_height = thumbnail_height


    def get_title(self):
        return self.title
    
    def get_year(self):
        return self.year
    
    def get_cast(self):      
        return self.cast
    
    def get_genres(self):
        return self.genres
    
    def get_summary(self):
        return self.summary
    
    
    # cast_shortlist() method prints a maximum of 4 cast names when a title is displayed
    def cast_shortlist(self):
        num_cast = min(len(self.cast), 4) # Ensures a max of 4 names are printed
        print(f"Starring:") 
        print('\t', end = '') # end argument removes the line break
        i = 0
        while i < num_cast:
            if(num_cast - i > 1):
                print(self.cast[i]+', ', end = '') # Loops through the cast list
            else:
                print(self.cast[i], end = '') # Omits the ',' for the last name
            i += 1
        
        # If not all cast is shown '...' is printed to indicate some names are not shown
        if len(self.cast) > 4 :
            print('...')




# Main


# Display menu
def display_main_menu():
    print('Welcome to K-Star Video - the home of the latest movies and all time classics')
    print('******************************************************************************\n')
    print('1. Search for a title')
    print('2. Your account')
    print('3. Return items')
    print('4. Exit')

def display_search_menu():
    print('1. Search by title')
    print('2. Search by actor e.g. "Tom Hanks or Julia Roberts"')
    print('3. Search by genre')
    print('4. Return to main menu')

def display_genre_menu():
    print('1. Comedy')
    print('2. Romance')
    print('3. Drama')
    print('4. Musical')
    print('5. Kids')
    print('6. Action')
    print('7. Sci-fi')
    print('8. Horror')
    print('9. Documentary')
    print('10. Biopic')
    print('11. TV Shows')

    print('n. Return to main menu')


with open ('user_list.json') as f:
    global users
    users = json.load(f)

with open ('movies.json') as f:
    movies = json.load(f)
    # movies = movies.reverse()

matching_movies = []


def get_user_input(prompt):
    input_value = input(prompt)
    print('\n')
    return input_value


def remainder_check(numerator, divisor):
    result = 0
    if(numerator % divisor) > 0:
        result = 1
    return result

# Need to know the search term (title, actor, genre??) - lambda? comprehension?
# Show a maximum of 10 results? Option to view next results if >10
# Need to be able to select a title once the list is populated
def search_movies():
    search_title = get_user_input('Enter a title: ')
    global matching_movies
    
    for movie in movies:       
        if (search_title in movie.get('title')):
            current_movie = Movie(movie.get('title'), movie.get('year'), movie.get('cast'), movie.get('genres'), movie.get('href'), movie.get('extract'), movie.get('thumbnail'), movie.get('thumbnail_width'), movie.get('thumbnail_height'))            
            matching_movies.append(current_movie)

    num_movies = len(matching_movies)
    
    i = 0
    '''
    i = 0 : movie 1 - 10
    i = 1 : movie 11 - 20
    i = 2 : movie 21 - 30
    i = 3 : movie 31 - 33 (31:)
    '''
    # 'pages' to cycle when displaying movies on screen
    pages = (num_movies // 10) + remainder_check(num_movies, 10)
    while (i < pages):
        if (i == 0): # First page
            display_movies(0, 10)
            if (pages > 1):
                print("More...")
                get_user_input("Press enter to continue")
        elif (i == pages-1): # Last page <--- THIS IS CAUSING AN ERROR!
            display_movies(i*10, -1)
        else: # All other pages
            display_movies(i*10, (i+1)*10)
            print("More...")
            get_user_input("Press enter to continue")
        i += 1


# Method to display 10 movies at a time
def display_movies(from_index, to_index):
    index = from_index
    count = 1
    while index < to_index:
        # For element 0 - 9 [10 - 19, 20 - 29 etc], print movie info
        print(f'{count}: {matching_movies[index].get_title()}: ({matching_movies[index].get_year()})')
        matching_movies[index].cast_shortlist() # prints cast names
        print('\n')
        index += 1
        count += 1
        





def menu_control():
    display_main_menu()
    choice = get_user_input('')
    if  choice == '1':
        display_search_menu()
        # 1 = title, 2 = actor, 3 = genre
        choice = get_user_input('')
        if choice == '1': 
            # choice = get_user_input('Enter title: ')
            search_movies()
        elif choice == '2': 
            choice = get_user_input('Enter actor: ')
        elif choice == '3':
            choice = get_user_input('Enter genre: ') 
        else:
            print('Invalid input - please try again')




current_user = ''

def username_check(email):
    result = False
    
    for user in users:
        if(email == user.get('email')):
            global current_user
            current_user = User(user.get('id'),user.get('email'),user.get('first'),user.get('last'),user.get('company'),user.get('created_at'),user.get('country'),user.get('password'))
            result = True
            break    # break is to stop the if statement once a match has been found    
    return result


def password_check(password):
    result = False
    if (password == current_user.get_password()):
        result = True
    return result




username = get_user_input('Enter username (email address): ')
if username_check(username) == True: # Check for valid username
    password = get_user_input('Enter your password: ') # If username check passes: check password
    if password_check(password) == True:
        menu_control()
    else:
        print('Incorrect password, please try again')
else:
    print('Email address not recognised, please try again')

'''
while get_user_input() != '4':
    display_main_menu()

    match get_user_input():
        case 1:
            print("yes")
        case 2:
            print("yes")
        case 3:
            print("yes")
        case 4:
            print("yes")
        case _:
            print("yes")
'''



