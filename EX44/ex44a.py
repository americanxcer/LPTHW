# Actions on the child imply an action on the parent
# a function is defined in the parent, but not in the child
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()
# here's the code that runs and references what's written above
dad.implicit()
son.implicit()
