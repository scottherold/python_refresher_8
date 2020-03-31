import sys

print('Please enter two numbers to perform division. The first number will be \
divided by the second\n')


def getint(prompt):
    """ Generates a number to be used in division """
    while True:
        try:
            number = int(input(prompt))
            return number
        # order of exceptions matter. Code to exit should by higher in
        # the try/catch block to prevent endless loops
        except EOFError:
            print("\n")
            sys.exit(1)
        except ValueError:
            print("Invalid number entered, please try again\n")
        # finlly executes whether an exception was raised or not
        finally:
            print("The finally clause always executes.")


def divide_nums():
    """ Performs division on integers provided by getint()"""
    x = getint("Please enter the first number: ")
    y = getint("Please enter the second number: ")
    return [x, y, x / y]


while True:
    try:
        result = divide_nums()
        print("{} divided by {} results in {}".format(result[0], result[1],
        result[2]))
        break
    except ZeroDivisionError:
        print("Invalid operation, please try again\n")