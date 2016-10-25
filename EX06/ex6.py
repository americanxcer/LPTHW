# the variable of x including the variable of %d which is 10
x = "There are %d types of people." % 10
#The word binary will show as itself
binary = "binary"
#The word do_not will show as don't
do_not = "don't"
# the variable of y is including two variables %s, however these two are different, and are signaled in the parenthesis -> the first %s is "binary" and the second is "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#print the sentence: There are 10 types of people .
print x
#print the sentence: Those who know binary and those who don't.
print y

#Prints the sentence written above with an "I said" infornt
print "I said: %r." % x
#repeatz the second half of the joke
print "I also said: '%s'." % y

#the variable hilarious stands for the word false
hilarious = False
#teh variable joke_evaluation is this question (so the variable assumes its evaluating the joke which is what is intended with the question it represents)
joke_evaluation = "Isn't that joke so funny?! %r"

#prints "isn't that joke so funy?!" which is answered directly with "False"
print joke_evaluation % hilarious

#first half of the sentence
w = "This is the left side of..."
#second half of the sentence
e = "a string with a right side."

#two sentence halves put together
print w + e
