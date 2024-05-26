"""
note of basic section
"""
# pylint: disable-msg=C0103

# Fundamental Data Types
# int
# float
# bool
# str
# list
# tuple
# set
# dict
# complex

# Custom Type
# Classes

# Specialized Data Types
# extends of fundamental data types for specific use

# None

# TODO: how to apply arithmetic operations in python?

print(2 + 4)
# latex style: $2 + 4$

print(type(3 / 5))
# latex style: $\frac{3}{5}$

print(2**3)
# latex style: $2^3$

print(5 % 4)
# latex style: $5 \mod 4$

print(type(0))
print(type(0.0))
# the memory of float is larger than int
# so we should use int if we don't need the decimal point

# refs: https://docs.python.org/3/tutorial/floatingpoint.html

print(round(2.1))
print(abs(-20))
# refs: https://docs.python.org/3/library/math.html

# refs: https://docs.python.org/3/library/

print((20 - 3) * 4)

print(complex(2, 3))
# latex style: $2 + 3i$

print(bin(5))
print(int("0b101", 2))

IQ = 190

print(IQ)

my_name = "Chris"
_my_age = "29"  # private variable


def say_my_name(name: str) -> str:
    """
    say my name from breaking bad

    Args:
        name (str): your name

    Returns:
        str: say it
    """
    name = "heisenberg"
    return name


print(say_my_name(my_name))

# a = 1 + 2  # statement
# 1 + 2  # expression

str1 = "str1"
str2 = "str2"

str3 = f"{str1} {str2}"

print(str3)

print(type(int(str(100))))

weather = 'This\'s "kind of" rainy.\n Hope you have a good day!\n'

print(weather)
