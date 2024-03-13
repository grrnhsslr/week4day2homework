# Write a recursion function to perform the fibonacci sequence up to the number passed in.
#
# More information on the Fibonacci Sequence here. Start the sequence with `0,1,1,...`.


def fibonacci(n):
    # num1 = 0
    # num2 = 1
    # next_number = num2
    # count = 1
    #
    # while count <= num:
    #     print(next_number, end=' ')
    #     count += 1
    #     num1, num2 = num2, next_number
    #     next_number = num1 + num2
    if n < 0:
        print("Incorrect input")

        # Check if n is 0
        # then it will return 0
    elif n == 0:
        return 0

        # Check if n is 1,2
        # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fib = input('pick a number: ')

print(fibonacci(int(fib)))
