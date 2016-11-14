# Actions on the child override the action on the parent
# you want the child to behave differently
# override the function in the child, effectively replcing the functionality.
# define a function with the same name in Child
class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
