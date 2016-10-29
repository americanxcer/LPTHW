#inports moduels
from sys import argv

#argv is a list including the script and filename
script, filename = argv

#the variable is assigned to the name of the file given in the prompt
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#asking the user to choose
raw_input("?")


print "Opening the file..."
#opens the file and enables editing
target = open(filename, 'w')


print "Truncating the file.  Goodbye!"
#erases the contents of the file
target.truncate()


print "Now I'm going to ask you for three lines."


line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#adds what the user typed according to each line, then presse
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print "And finally, we close it."
#closes and saves the file
target.close()
