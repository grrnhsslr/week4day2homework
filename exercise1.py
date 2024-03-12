# Filter out all the empty strings from the list below
#
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ", "Argentina", " ", "San Diego", "", "  ", "", "Boston", "New York", "DC", "          "]

# Remove all the empty string
places = filter(lambda name: name.strip(), places)
print(list(places))
