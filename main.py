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
    - Menus need to keep cycling until user chooses to exit - use 'while != ' condition each time

3. Class for users, creates "users", updates their rental history, current rentals (recommendations?)

4. Class for titles (data required: title, genre, actors, year, runtime, rating, plot)

5. Main will be responsible for: 
    - requesting username/password
    - displaying the menu
    - adding users
    - renting/returning titles

6. Search feature
    - Back to return to earlier page
    - When returning to main menu, previous search is deleted ***FIXED***
    - When searching for actor 'Matt Damon' multiple pages were displayed automatically ***FIXED***
    - movie_list_control() method needs to be tidied
    
'''
import json, math, textwrap
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
        
  

 

    
    
    def get_firstname(self):
        return self.first

    def get_fullname(self):
        fullname = f'{self.first} {self.last}'
        return fullname
    
    def get_email(self):
        return self.email

    def get_password(self):
        return self.password
    
    def get_country(self):
        return self.country
      
    def update_current_rentals(self, action, movie):
        # action = ['rental', 'return']
        if (action == 'rental'):
            self.current_rentals.append(movie)
            self.all_rentals.append(movie)
        elif (action == 'return'):
            self.current_rentals.remove(movie)

    
    def get_current_rentals(self):
        return self.current_rentals


    def get_rental_history(self):
        return self.all_rentals

    # Writes data back to file when user exits
    def save_users(self):
        with open('user_list.json', 'w') as f:
            json.dumps(self.users, f, indent = 2)


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
    
    
     # cast_full() method prints all cast names when a title is displayed
    def cast_full(self):
        num_cast = len(self.cast) 
        print(f"Starring:") 
        # print('\t', end = '') # end argument removes the line break
        i = 0
        while i < num_cast:
            if(num_cast - i > 1):
                print(self.cast[i]+', ', end = '') # Loops through the cast list
            else:
                print(self.cast[i], end = '') # Omits the ',' for the last name
            i += 1
   



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

'''
class MovieCategory:

    genre = {}

    genre['Comedy'] = ['Comedy']
    genre['Romance'] = ['Romance']
    genre['Drama'] = ['Drama', 'Adventure', 'Mystery', 'Political', 'Legal']
    genre['Musical'] = ['Musical', 'Dance']
    genre['Kids'] = ['Family', 'Animated', 'Live Action']
    genre['Action'] = ['Action', 'Superhero', 'Crime', 'Spy', 'Disaster', 'War', 'Western']
    genre['Sci-Fi'] = ['Science Fiction', 'Fantasy']
    genre['Horror'] = ['Horror', 'Slasher']
    genre['Thriller'] = ['Thriller', 'Suspense']
    genre['Documentary'] = ['Documentary', 'Biography', 'Political', 'Historical', 'Sports']
    
    decade = {}
    
    decade['2020s'] = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029']
    decade['2010s'] = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    decade['2000s'] = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009']
    decade['1990s'] = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999']
    decade['1980s'] = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989']
'''


# Main

matching_movies = [] # global variable to be used by different methods, method required to re-set it once new search begins

# Display menu
def display_main_menu():
    global matching_movies
    matching_movies = []
    print('1. Search for a title')
    print('2. Your account/history')
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
    print('3. Drama') # "Adventure", "Mystery", "Political", "Legal"
    print('4. Musical') # "Dance"
    print('5. Kids') # Search "Family", "Animated", "Live Action"
    print('6. Action') # Search "Crime" "War", "Disaster", "Spy", "Superhero", "Western", 
    print('7. Sci-fi') # Search  "Science Fiction", "Fantasy"
    print('8. Horror') # "Slasher"
    print('9. Thriller')
    print('10. Documentary') # Search "Biography","Political","Historical", "Sports", 
    print('11. Return to main menu')


genre = {}

genre[1] = ['Comedy']
genre[2] = ['Romance']
genre[3] = ['Drama', 'Adventure', 'Mystery', 'Political', 'Legal']
genre[4] = ['Musical', 'Dance']
genre[5] = ['Family', 'Animated', 'Live Action']
genre[6] = ['Action', 'Superhero', 'Crime', 'Spy', 'Disaster', 'War', 'Western']
genre[7] = ['Science Fiction', 'Fantasy']
genre[8] = ['Horror', 'Slasher']
genre[9] = ['Thriller', 'Suspense']
genre[10] = ['Documentary', 'Biography', 'Political', 'Historical', 'Sports']

decade = {}

decade['2020s'] = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029']
decade['2010s'] = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
decade['2000s'] = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009']
decade['1990s'] = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999']
decade['1980s'] = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989']


with open ('user_list.json') as f:
    global users
    users = json.load(f)

with open ('movies.json') as f:
    movies = json.load(f)
    # movies = movies.reverse()


current_user = None


def get_user_input(prompt):
    user_response = input(prompt)

    # print('\n')
    return user_response

# Use number input method whenever a menu option is to be selected
def get_number_input(prompt):
    user_response = None
    while not (isinstance(user_response,int)):
        user_input = get_user_input(prompt)
        try:
            user_response = int(user_input)
        except ValueError:
            print('Invalid input. Please try again (value error thrown)')
        except TypeError:
            print('Type error thrown')
    return user_response


# If no other uses for this method, incorporate into movie_list_control() method
def remainder_check(numerator, divisor):
    result = 0
    if(numerator % divisor) > 0:
        result = 1
    return result

# Need to know the search term (title, actor, genre??) - lambda? comprehension?
# Show a maximum of 10 results? Option to view next results if >10
# Need to be able to select a title once the list is populated
def search_movies(search_type, search_term):
    # search_type = ['title', 'actor', 'genre']
    global matching_movies
    
    for movie in movies:
        if (search_type == 'title'):
            if (search_term in movie.get('title').lower()):
                current_movie = Movie(movie.get('title'), movie.get('year'), movie.get('cast'), movie.get('genres'), movie.get('href'), movie.get('extract'), movie.get('thumbnail'), movie.get('thumbnail_width'), movie.get('thumbnail_height'))            
                matching_movies.append(current_movie)

        elif (search_type == 'actor'):
            # num_cast = len(movie.get('cast'))
            for cast in movie.get('cast'):
                if (search_term in cast.lower()):
                    current_movie = Movie(movie.get('title'), movie.get('year'), movie.get('cast'), movie.get('genres'), movie.get('href'), movie.get('extract'), movie.get('thumbnail'), movie.get('thumbnail_width'), movie.get('thumbnail_height'))            
                    matching_movies.append(current_movie)

        elif (search_type == 'genre'):
            global genre
            # Search_term in this case is a number from 1-10 representing all genre categories
            search_genre = genre[search_term]
            # search_genre = 'Romance'
            for search_genre in genre[search_term]:
                for movie_genre in movie.get('genres'):
                    if (search_genre in movie_genre):
                        current_movie = Movie(movie.get('title'), movie.get('year'), movie.get('cast'), movie.get('genres'), movie.get('href'), movie.get('extract'), movie.get('thumbnail'), movie.get('thumbnail_width'), movie.get('thumbnail_height'))            
                        matching_movies.append(current_movie)       

    movie_list_control(len(matching_movies))
   


# Can this code be re-factored to be more DRY?
# Once a selection is made the search should be cleared
# Add navigation options: previous / next / select / back to search menu
def movie_list_control(num_movies):
    exit_request = False
    def selection_text():
        print('1. Select movie\t\t2. Go back to search menu\t\t')
    
    def choice_response(selection, page_index):
        match selection:
            case 1:
                # display selected movie
                choice = get_number_input('\nEnter number of movie: ')
                print('\n')
                display_selected_movie(choice-1, page_index*10, (page_index+1)*10)
                exit_request = True
                return exit_request               
            case 2:
                search_menu_control()
                exit_request = True
                return exit_request
            case 3:
                # display previous page - update i / page number to go back 1
                display_movie_list((page_index-1)*10, (page_index)*10)
                i = page_index-1
                return i
            # case 4:
                # display next page
                # pass
            case _:
                pass

    
    
    partial_page = 0
    if (num_movies % 10) > 0:
        partial_page = 1
    i = 0
    # 'pages' to cycle when displaying movies on screen
    pages = (num_movies // 10) + partial_page
    # Selection options will vary:
    # all pages need option to select movie and go back to previous menu - **ALWAYS**
    # all pages except last need NEXT
    # all pages except first need PREVIOUS    
    # most pages need NEXT/PREVIOUS **MOST COMMON = ELSE**
    while (i < pages) and exit_request == False :
        if (i == 0):
            # First page  
            display_movie_list(i*10, min((i+1)*10, num_movies))
            selection_text()
            print('4. Next page')        
            choice = get_number_input('\nEnter number choice to continue: ')
            choice_response(choice, i)
        elif (i == pages-1): 
            # Last page
            display_movie_list(i*10, num_movies-1)
            selection_text()
            print('3. Previous page')        
            choice = get_number_input('\nEnter number choice to continue: ')
            choice_response(choice, i)
        else:
            # All other pages
            display_movie_list(i*10, (i+1)*10)
            selection_text()
            print('3. Previous page\t\t4. Next page')        
            choice = get_number_input('\nEnter number choice to continue: ')
            choice_response(choice, i)


        i += 1



'''
def movie_list_control(num_movies):
    i = 0
    # 'pages' to cycle when displaying movies on screen
    pages = (num_movies // 10) + remainder_check(num_movies, 10)
    while (i < pages-1):
        # Prints movie info for all but the last page   
        display_movie_list(i*10, (i+1)*10)
        print("More...")
        try:
            choice = int(get_user_input("\nPress enter to continue or select movie "))
            if (isinstance(choice, int)):
                print('\n\n')
                # Passes as arguments the selected title and the indexes currently being displayed
                # So that the user can return to this list, if desired
                display_selected_movie(choice-1, i*10, (i+1)*10)
        except:
            pass

        i += 1

    if (i == pages-1): # The last page
        display_movie_list(i*10, num_movies-1)
    
    try:
        choice = int(get_user_input('\nPress enter to continue or select movie '))
        if (isinstance(choice, int)):
            print('\n\n')
            # Passes as arguments the selected title and the indexes currently being displayed
            # So that the user can return to this list, if desired
            display_selected_movie(choice-1, i*10, (i+1)*10)
    except:
        pass

'''



# Method to display max 10 movies at a time
def display_movie_list(from_index, to_index):
    index = from_index
    # count = 1
    while index < to_index:
        # For element 0 - 9 [10 - 19, 20 - 29 etc], print movie info
        print(f'{index+1}: {matching_movies[index].get_title()} ({matching_movies[index].get_year()})')
        matching_movies[index].cast_shortlist() # prints cast names
        print('\n')
        index += 1
        # count += 1


def display_selected_movie(index, from_index, to_index):
    print(f'{matching_movies[index].get_title()} ({matching_movies[index].get_year()})')
    matching_movies[index].cast_full() # prints all cast names
    print('\n')
    # Print wrapped lines for better readability
    plot_summary = textwrap.wrap((matching_movies[index].get_summary()), width = 100, break_long_words= False)
    for line in plot_summary:
        print(line)    
    print()

    print('\n')
    print(f'1. Rent Movie\t\t2. Back to list\t\t3. Back to menu')
    choice = get_number_input('\nEnter number to select option: ')

    match choice:
        case 1:
            rent_movie(matching_movies[index])
            # Rent movie screen
            # What should happen once user has confirmed rental?
            print('[title name successfully rented]')
            choice = get_number_input('\n1. Back to search list\t\t2. Back to main menu\t\t etc')
            # --> options for choice
        case 2:
            display_movie_list(from_index, to_index)
        case 3:
            main_menu_control()
        case _:
            print('Invalid entry - please try again')

   


def rent_movie(movie):
    print(f'Title: {movie.get_title()} ({movie.get_year()})')
    choice = get_user_input('\nWould you like to rent this movie? Enter "Y" or "N": ').upper()
    if (choice == 'Y'):
        # Call method to add title to user's list of current rentals
        current_user.update_current_rentals('rental', movie)


def return_movie():    
    show_user_movies(current_user.get_current_rentals())
    print('***************************************************************************')
    choice = get_number_input('\nEnter the movie number you\'re returning: ')
    # Call update_rental method, with the 'return' parameter
    current_user.update_current_rentals('return', current_user.get_current_rentals()[choice-1])
    print('Item returned')
    print('CURRENT RENTALS:')
    show_user_movies(current_user.get_current_rentals())
    print('***************************************************************************')


def show_user_movies(movie_list):
    if (len(movie_list) > 0):
        print('Here are your current/previous rentals:')
        i = 0
        while (i < len(movie_list)):
            print(f'{i+1}. {movie_list[i].get_title()} ({movie_list[i].get_year()})')            
            i += 1
    else:
        print('No rentals to show')



def diplay_account_control():
    print(f'Hi, {current_user.get_firstname()}! Here\'s your account info:')
    print(f'Name: {current_user.get_fullname()}')
    print(f'Username: {current_user.get_email()}')
    print(f'Country: {current_user.get_country()}')
    print('***************************************************************************')
    print('CURRENT RENTALS:')
    show_user_movies(current_user.get_current_rentals())
    '''
    if (len(current_user.get_current_rentals()) > 0):
        i = 0
        while (i < len(current_user.get_current_rentals())):
            print(f'{i+1}. {current_user.get_current_rentals()[i].get_title()} ({current_user.get_current_rentals()[i].get_year()})')
            print('\n')
            i += 1
    else:
        print('You have no rentals at this time')     
    '''
    print('***************************************************************************')
    print('RENTAL HISTORY:')
    show_user_movies(current_user.get_rental_history())
    '''
    if (len(current_user.get_rental_history()) > 0):
        i = 0
        while (i < len(current_user.get_rental_history())):
            print(f'{i+1}. {current_user.get_rental_history()[i].get_title()} ({current_user.get_rental_history()[i].get_year()})')
            print('\n')
            i += 1
    else:
        print('Looks like you\'re still looking for your first movie rental!')
        print('Select the option below to search our huge list of movies!')
    '''
    print('***************************************************************************')
    print(f'1. Return Movie\t\t2. Back to main menu')
    choice = get_number_input('\nEnter number to select option: ')
    if (choice == 1): # Return movie
        # Show list of current rentals again
        return_movie()
    elif (choice == 2):
        main_menu_control()
    else:
        print('Invalid entry - please try again')





def search_menu_control():
    display_search_menu()
        # 1 = title, 2 = actor, 3 = genre
    choice = get_number_input('\nEnter number to select menu option: ')
    if choice == 1: 
        choice = get_user_input('\nEnter title: ').lower()
        search_movies('title', choice)
    elif choice == 2: 
        choice = get_user_input('\nEnter actor: ').lower()
        search_movies('actor', choice)
    elif choice == 3:
        display_genre_menu()
        choice = get_number_input('\nEnter selected genre number: ')   
        # Each genre number represents one or more genre categories
        # The search_movies() method will search for films which
        # include the specified genre   
        search_movies('genre', choice)
        
    elif choice == 4:
        main_menu_control()
    else:
        pass
        # print('Invalid input - please try again')

def main_menu_control():    
    choice = None
    while choice != 4:
        display_main_menu()
        # 1 = search, 2 = account, 3 = return items
        choice = get_number_input('\nEnter number to select menu option: ')
        if  choice == 1:
            search_menu_control()
            '''
            display_search_menu()
            # 1 = title, 2 = actor, 3 = genre
            choice = get_number_input('Enter number to select menu option: ')
            if choice == 1: 
                choice = get_user_input('Enter title: ').lower()
                search_movies('title', choice)
            elif choice == 2: 
                choice = get_user_input('Enter actor: ').lower()
                search_movies('actor', choice)
            elif choice == 3:
                # List genres
                choice = get_number_input('Enter number to select genre: ')
                # Matching system to match genre to number - pass genre to search method
                search_movies('genre', choice)
            elif choice == 4:
                pass
            else:
                pass
                # print('Invalid input - please try again')
            '''
        elif choice == 2:
            diplay_account_control()
            
        elif choice == 3:
            return_movie()
        elif choice == 4: # Exit
            break

        





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
        # Initial welcome message
        print('Welcome to K-Star Video - the home of the latest movies and all time classics')
        print('*****************************************************************************\n')
        main_menu_control()
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



