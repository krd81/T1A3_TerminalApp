import random, json

'''
with open ('raw.json') as f:
    users = json.load(f)
    print(len(users))
'''

# Random Number will be between the from and to numbers
def generate_random_number(from_num: int, to_num: int):
    return random.randint(from_num,to_num)


# Index determines which letter is randomly selected
def alpha_key(index: int):
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    return alphabet[index]

# Index is either 0 or 1
def upper_case(index: int):
    upper = False #lowercase
    if index == 1:
        upper = True #uppercase
    return upper

# Password lengths must be between 8 and 16 characters long
def password_length():
    return generate_random_number(8, 16)



# This method takes an input of num characters then creates a string of that length
# It will use a loop function which will loop num_chars times to create the password

def create_password(num_chars: int):
    # For each character, the alpha_key() & upper_case methods will be called which will output a character in the correct case
    chars = []
    password = ''
    i = 0
    while i < num_chars:        
        char = alpha_key(generate_random_number(0,25))
        if (upper_case(generate_random_number(0,1)) == True):
            chars.append(char.upper())
        else:
            chars.append(char)
        i += 1

    for i in chars:
        password += i
    
    return password


print(create_password(10))


