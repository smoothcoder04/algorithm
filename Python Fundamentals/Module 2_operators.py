# Arithmatic operators

"""
The operatores who have same precedence when encountered will be execurted from left side first.
"""


def arith():
    print(3*4/5)
    print(3/4*5)


arith()


"""
Booleans - in bit terms True is 1 & False is 2
"""


def arith2():
    print((20+True)/(4-5*False))


arith2()


"""
Print a string multiple times
"""


def playstr():
    x = 3
    y = 4
    print("3"*3)
    print(str(x)*10 + str(y)*4)


playstr()

"""
Exercise = gravitational Force
"""


def gravforce():
    G = 6.67 * (10 ** -11)
    M = 6.0 * (10 ** 24)  # Mass of Earth
    m = 7.34 * (10 ** 22)  # Mass of the moon
    r = 3.84 * (10 ** 8)

    result = (G*M*m)/(r**2)
    return result


gravitationalForce = gravforce()
print(f"the gravitational force between earth & moon is {gravitationalForce}")
