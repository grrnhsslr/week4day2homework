# Write an anonymous function that sorts this list by the last name *case insensitive*...
# Hint: Use the ".sort()" method or the sorted() function and access the key keyword argument"
#
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield", "David hassELHOFF", "Gary A.J. Bernstein"]

w = sorted(authors, key=lambda lastname: (lastname[0].split()[-1].lower()))

print(w)


# use .split()[-1] to get the last name
# use [0].lower() to get lowercase last initial
# use ord() to get a value to sort by
# test = 'Bob Ross'
# ord(test.split()[-1][0].lower())
# #>> returns 114 which corresponds to 'r'
# Creating a lambda function that does the same thing:
# (lambda author: ord(test.split()[-1][0].lower()))(test)
# Creating a lambda function that does the same thing:
# (lambda author: ord(test.split()[-1][0].lower()))(test)
