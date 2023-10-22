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

3. Class for users, contains their rental history, current rentals (recommendations?)

4. Class for titles (data required: title, genre, actors, year, runtime, rating, plot)

5. Main will be responsible for: 
    - requesting username/password
    - displaying the menu
    - adding users
    - renting/returning titles
    
'''



# Main

def get_user_input():
    return input




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

user_response = ''

while user_response != '4':
    display_main_menu()

    match user_response:
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


