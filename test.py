def get_user_input(prompt):
    user_response = input(prompt)

    
    return user_response

# Use number input method whenever a menu option is to be selected
def get_number_input(prompt):
    user_response = None
    while not (isinstance(user_response,int)):
        user_input = get_user_input(prompt)
        try:
            user_response = int(user_input)
            print(user_response)
        except ValueError:
            print('Invalid input. Please try again (value error thrown)')
        except TypeError:
            print('Type error thrown')
            break
    return user_response


get_number_input('Enter a number: ')