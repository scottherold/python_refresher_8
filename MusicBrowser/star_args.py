# example of *args

# *args as a parameter in a function tells the function that it can take
# a variable number of arguments in the function.

# the __future__ module was created for Python2 to use Python3 fearures
# if you see this syntax, know that you are working on a Python 2 module
from __future__ import print_function

# example of a function using *args to take a variable number of
# arguments (as a tuple) and unpacking the tuple

# the parameter can be named anything, but needs to start with *,
# for example *params has the same functionality. But, use *args, unless
# you have a good reason

# *args must be the last parameter, unless it is a key-word parameter
def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))

# example of *args and args; *args takes a list, args is a tuples of the
# values of the values passed into *args
def build_tuple(*args):
    return args


print(build_tuple("bob", "steve", "chris"))