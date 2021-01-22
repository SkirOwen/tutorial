
# This is a comment
"""
this is a block
of comment

if you put this first in a function, it is called a docstring,
and you can access it with help()


more about this later :)
"""

# Number type:
a = 17      # this is an int
print(a)

b = 3.14    # this is a float
c = 3.0     # so is this

d = float(17)   # is the same as 17.0, it convert int in float


# these are boolean, bool
e = True        # True is equivalent to 1
f = False       # False is equivalent to 0


# Convert to bool using bool()
bool_a = bool(a)
print(bool_a)


msg_0 = "Hello?"  # This is a string
msg_1 = 'Yes?'  # This is also a string

# try a string with an ' in it to see what is happening
msg_2 = ''


# lists
lst_0 = [5, -14, -16, -13]
lst_1 = [16, 14, 5, 3]
lst_2 = [16, "jazzy", 5, 3]
lst_3 = [17, 14, 5.0, 3]
lst_4 = [[16, 5], 14, 5.0, 3]

# index of list
lst_0 = [5, -14, -16, -13]
#        0    1    2    3

index_0 = lst_0[0]      # What is this?
# What is the length of the list? print it on the next line


# Operators
add = 5 + 3.0
sub = 5 - 17.0

mul = 17 * 6
div = 233 / 144

int_div = 233 // 144
mod = 233 % 144

mod2 = 233 % 2

power = 3 ** 2

# +=, -=, *=, /=
x = 17
x += 1  # same as doing x = x + 1

# What would this do?
msg_3 = msg_0 + msg_1

lst_0 *= 2

# this?  msg_3 + 2
