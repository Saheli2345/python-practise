# Arithmetic Operators(+, -, *, /, %, **, //)
a=2
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) # a raised to the power of b
print(a//b) # floor division

# Assignment Operators(=, +=, -=, *=, /=, %=, **=, //=)
c=5
d=6
print(d-c) # d=d-c

e=9
d+=e # d=d+e
print(d)

# Comparison Operators(==, !=, <, >, <=, >=)
f=10
g=20
print(f==g)
print(f!=g)
print(f<g)
print(f>g)
print(f<=g)
print(f>=g)

# Logical Operators(and, or, not)
# and operator [both condition =True return True, Both condition =False return False, One condition =True and other =False return False]
age = 25
has_license = True

# Both conditions must evaluate to True
if age >= 18 and has_license:
    print("You are allowed to drive.")
else:
    print("You cannot drive.")

# or operator [both condition =True return True, Both condition =False return False, One condition =True and other =False return True]
is_weekend = True
is_holiday = False

# Evaluates to True because is_weekend is True
if is_weekend or is_holiday:
    print("You can sleep in today!")
else:
    print("Time to go to work.")

# not operator [if condition =True return False, if condition =False return True]
is_raining = False

# Checks if it is NOT raining (not False becomes True)
if not is_raining:
    print("Let's go for a walk outside.")
else:
    print("Stay indoors.")


# Bitwise Operators(&, |, ^, ~, <<, >>)
# AND operator (&): Compares each bit of two numbers and returns 1 if both bits are 1, otherwise returns 0.
ali=5
bat=7
print(ali & bat)

# OR operator (|): Compares each bit of two numbers and returns 1 if at least one of the bits is 1, otherwise returns 0.
print(ali | bat)

# XOR operator (^): Compares each bit of two numbers and returns 1 if the bits are different, otherwise returns 0.
print(ali ^ bat)

# NOT operator (~): Inverts the bits of a number, changing 1s to 0s and 0s to 1s.
print(~ali)

# Left Shift operator (<<): Shifts the bits of a number to the left by a specified number of positions, filling in with 0s on the right.
print(ali << 1)  # Shifts bits of ali (5) to the left by 1 position

# Right Shift operator (>>): Shifts the bits of a number to the right by a specified number of positions, discarding bits on the right.
print(ali >> 1)  # Shifts bits of ali (5) to the right by 1 position

