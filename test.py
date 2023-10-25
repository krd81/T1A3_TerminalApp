# // "password": "WhvjdnWE"

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


print(genre[3][1])

print(genre.keys())
print(genre.values())
print(genre.items())


'''
From movie rental confirmation: go back to search list didn't work **Check this is fixed**
From movie rental confirmation: go back to main menu works

When search list is displayed, next page works
When search list is displayed, strange result for previous page: lists previous 10 movies 
but then starts printing the next set
- Seem to have fixed previous page display - but unable to select movie once previous list is shown
  Should have taken choice as per line 362


From the movie list page: go back to search list does work
From search menu, return to main menu works

Type 4 for exit is no longer working


'''