# the function has a name and what it will contain
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# the following indented lines will be given
# everytime the name of the function is given
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# assigns these values to the variables in the function
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# assigns these values to the variables in the function
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# assigns these values to the variables in the function
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# assigns these values to the variables in the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
