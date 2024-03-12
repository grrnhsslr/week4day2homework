# Create a generator that takes a number argument and yields that number squared down to 0, then call the generator
# and iterate through and print the result.

def square_down(n):
    while n >= 0:
        yield n * n
        n -= 1


for squared in square_down(5):
    print(squared, end=' ')
