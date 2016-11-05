i = 0
numbers = []

# adding a function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

age = add(4, 3)
fish = subtract(5, 2)

# replacing the '6' with a variable
while i < age:
    print "At the top i is %d" % i
    numbers.append(i)

# study drill 3
    i = i + fish
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
