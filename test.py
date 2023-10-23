import math
cast = ['Leonardo DiCaprio', 'Ken Watanabe', 'Joseph Gordon-Levitt', 'Marion Cotillard', 'Elliot Page', 'Tom Hardy', 'Cillian Murphy', 'Tom Berenger', 'Michael Caine', 'Dileep Rao', 'Pete Postlethwaite', 'Lukas Haas', 'Tim Kelleher', 'Talulah Riley', 'Michael Gaston', 'Felix Scott', 'Andrew Pleavin', 'Hélène Cardona', 'Matt Vogel']
cast2 = [
        "Tom Hanks",
        "John Candy",
        "Rita Wilson"
        
      ]

cast3 = ['Matt Damon', 'Ben Affleck', 'Jennifer Anniston']

cast2.append(cast3)

print(cast2)

num_cast = min(len(cast), 4)

print(f"Starring:") 
print('\t',end = '') 
i = 0
while i < num_cast:
    if(num_cast - i > 1):
        print(cast[i]+', ', end = '')
    else:
        print(cast[i], end = '')
    i += 1

if len(cast) > 4 :
    print('...')

num_movies = 33
answer = ((num_movies // 10) + math.ceil(num_movies % 10))
first_num = (num_movies // 10)
second_num = math.ceil(num_movies % 10)

# 3 + 1 = 4

print(f'the answer is {answer}. This is {first_num} + {second_num}')
