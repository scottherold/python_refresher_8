# example of *kwargs

# *kwargs as a parameter in a function tells the function that there is 
# a variable number of 'k'ey 'w'ord arguments.

# **kwargs does not care about the order of the key word arguments,
# this is because, it is searching specifically for key word arguments

# kwargs is a dictionary, so dictionary methods work on kwargs
def print_backwards(*args, end=' ', **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]: # change the range
        print(word[::-1], end=sep_character, **kwargs)
    # print the first word separately
    print(args[0][::-1], end=end_character, **kwargs)


# another version
def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in ars[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another string")

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='',
                sep='\n**\n')
print("*" * 10)