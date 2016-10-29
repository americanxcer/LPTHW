#inports modules
from sys import argv

#arg is a list conaining the script and filename
script = argv,

#study drill
#asks user to type in the filename
print "Type filename you'd like to open once:"
#allows user to decide which file is assigned to the variable
filename = raw_input("> ")

#open takes a prameter and returns a value set to the variable "the"
txt = open(filename)

#prints this sentence using a variable
print "Here's your file %r:" % filename
#takes the text and reads it -> opens it
print txt.read()


#prints this sentence
print "Type the filename again:"
#assigns the variable to a raw input which is signaled with an >
file_again = raw_input("> ")

#assigns the variable to open the file which was given in the raw input above
txt_again = open(file_again)

#prints the file mentioned above and opens it/reads it
print txt_again.read()
