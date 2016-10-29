# Inports modules
from sys import argv
# List including script and input file which are given in the command line
script, input_file = argv


# The function is given a name and told what it will do
# This function will read the file
def print_all(f):
    print f.read()

# This function will move to the start of the file
def rewind(f):
    f.seek(0)

# This function reads the number of the line and reads what is on it (?)
def print_a_line(line_count, f):
    print line_count, f.readline()

# Assigns the variable to open the file given in the command prompt
current_file = open(input_file)

print "First let's print the whole file:\n"

# Prints the function "print_all" -> reads the given file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Moves to the start of the file
rewind(current_file)

print "Let's print three lines:"


# Assigns the current line to 1
current_line = 1
# Prints the the line it's on (1) and the text given on that line from the file
print_a_line(current_line, current_file)

# Adds 1 to the last line, makeing it line 2
current_line = current_line + 1
# Prints the second line from the text
print_a_line(current_line, current_file)

# Adds 1 to the last line, makeing it line 3
current_line = current_line + 1
# Prints the thrid line form the text
print_a_line(current_line, current_file)
