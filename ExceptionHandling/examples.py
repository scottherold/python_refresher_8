# practice with exceptions

# user input for testing
num = int(input("Please enter a number "))


# example of recursion error
def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# try/except (if you know the errortype)
# it's best to be explicit about exceptions that you are handling and it
# is good practice to have different try/except blocks for multiple
# potential exceptions
try:
    print(factorial(num))
# example of multiple exceptions handling simultaneously)
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")

print("Program terminating")