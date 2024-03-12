# Write a recursion function to perform the fibonacci sequence up to the number passed in.
#
# More information on the Fibonacci Sequence here. Start the sequence with `0,1,1,...`.


def fibonacci(num):
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1

    while count <= num:
        print(next_number, end=' ')
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2


fib = input('pick a number: ')
print(fibonacci(int(fib)))
