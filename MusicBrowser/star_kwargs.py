# example of *kwargs

# *kwargs as a parameter in a function tells the function that there is 
# a variable number of 'k'ey 'w'ord arguments.
def print_backwards(*args, **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", 
                    file=backwards)