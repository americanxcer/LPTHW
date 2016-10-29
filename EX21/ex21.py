# function is named "add(a,b)""
def add(a, b):
# when the function is called, the console will print this
    print "ADDING %d + %d" % (a, b)
# when asked to for the return of the function, the solution of this will be printed
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

# The variables are assigned to the functions
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# Only now are the results of the maths in the functions printed, according to their assigned variables
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, tupe it in anyway.
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
