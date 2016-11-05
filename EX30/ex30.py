people = 30
cars = 40
trucks = 15

# if statement is true, then print designated sentence.
# if 40 > 30 or 15 < 40 [[True]]
if cars > people or trucks < cars:
    print "We should take the cars."
# if 40 < 30 or 15 > 40 [[False]]
elif cars < people or trucks > cars:
    print "We should not take the cars."
else:
    # if both staeements above are False, print this
    print "We can't decide."


# if 15 > 40 and 30 > 40 [[False]]
if trucks > cars and people > cars:
    print "That's too may trucks."
# if 15 < 40 and 40 > 30 [[True]]
elif trucks < cars and cars > people:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."


# if 30 > 15 and (15 doesn't equal 40) [[True]]
if people > trucks and (trucks != cars):
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
