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
import json
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

'''
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
'''

users = []
current_user = ''

with open ('user_list.json') as f:
    users = json.load(f)


def username_check(email):
    result = False
    
    for user in users:
        if(email == user.get('email')):
            global current_user
            current_user = User(user.get('id'),user.get('email'),user.get('first'),user.get('last'),user.get('company'),user.get('created_at'),user.get('country'),user.get('password'))
            result = True
            break    # break is to stop the if statement once a match has been found
    print(type(current_user))
    return result


def password_check(password):
    result = False
    if (password == current_user.get_password()):
        result = True
    return result

input = ''

def get_user_input(prompt):
    input_value = input(prompt)
    return input_value

# print()
# username = input("Enter username (email address): ")

# print("Enter your password: ")
# password = input("Enter your password: ")

username = get_user_input('Enter username (email address): ')
if username_check(username) == True: # Check for valid username
    password = get_user_input('Enter your password: ')
    if password_check(password) == True:
        display_main_menu()
    else:
        print('Incorrect password, please try again')
else:
    print('Email address not recognised, please try again')