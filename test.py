import textwrap
extract = "Harry Potter and the Philosopher's Stone is a 2001 fantasy film directed by Chris Columbus and produced by David Heyman, from a screenplay by Steve Kloves, based on the 1997 novel of the same name by J. K. Rowling. It is the first instalment in the Harry Potter film series. The film stars Daniel Radcliffe as Harry Potter, with Rupert Grint as Ron Weasley, and Emma Watson as Hermione Granger. Its story follows Harry's first year at Hogwarts School of Witchcraft and Wizardry as he discovers that he is a famous wizard and begins his formal wizarding education."



output = textwrap.wrap(extract, width = 100, break_long_words= False)


for line in output:
    print(line)    
print()

'''
i = 0
while (i < len(output)):
    print(output[i])
    i += 1
print()
'''
