# J Reus-Brodsky
# An example of Class Definitions with Inheritance

# Define the classes
# Bookcase is the child class to object, which is the parent class
class Bookcase(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return self.prettyprint()

    def prettyprint(self):
        return "A Generic Bookcase"
# billy is the child class, bookcase is the parent class
class Billy(Bookcase):
    def __init__(self, width, height):
        #super -> gives the super class of billy, then call the __init__ value of that.
        super(Billy, self).__init__(width, height)

    # Overridden method
    def prettyprint(self):
        pretty = "A Billy Bookcase with dimensions %d x %d cm"
        return pretty % (self.width, self.height)

class Hemnes(Bookcase):
    def __int__(self, width, height):
        super(Hemnes, self).__init__(width, height)

    # Overridden method
    def prettyprint(self):
        pretty = "A Fancy Hemnes Bookcase with dimensions %d x %d cm"
        return pretty % (self.width, self.height)

# Make an instance of the classes
gen = Bookcase(50, 100)
bil = Billy(80, 120)
hem = Hemnes(200, 180)

# Call one of the functions (methods) inseide the instance
print hem.prettyprint()

# Other useful things
# %r is showing us the raw data, which is good for debugging
# it shows us what kind of what object it is and where
# pretty is using %s more readable
print "Type: \n %r \n %r \n %r" % (type(gen), type(bil), type(hem))
print "Raw: \n %r \n %r \n %r" % (gen, bil, hem)
print "Pretty:\n %s \n %s \n %s" % (gen, bil, hem)
print "Is Instance of Billy: ", isinstance(gen, Billy)
print "Is Instance of Billy: ", isinstance(bil, Billy)
print "Is Instance of Billy: ", isinstance(hem, Billy)
