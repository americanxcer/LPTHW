from sys import argv

script, filename = argv

txt = open(filename)

print "Here's the file you edited in ex16.py"
print txt.read()
