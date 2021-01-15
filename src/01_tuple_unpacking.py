# swap example

# wrong way
a = 3
b = 45

temp = a
a = b
b = temp

# right way
c = 23
d = 45

c, d = d, c


# catch all

def fruits():
    return 'apple', 'banana', 'cheery', 'grape'

# wrong way


fa = fruits()[0]
fa, fb, _, _ = fruits()


# right way

fa, fb, *_ = fruits()
fa, *_, fb = fruits()
*_, fa, fb = fruits()
