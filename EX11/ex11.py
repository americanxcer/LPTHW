# The "input" function converts the input you enter as if it were python code. "raw_input" doesn't convert the input and takes the input as it is given.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

print "What is your name?",
name = raw_input()
print "Who's your daddy?",
father = raw_input()
print "Is he rich like me?",
rich = raw_input()

print "So, %r, who's daddy, %r, is rich, %r?" % (
name, father, rich)
