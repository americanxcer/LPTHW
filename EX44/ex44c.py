# Actions on the child alter the action on the parent
# Alter before or after
# first override the function (like ex44b.py)
#then use a super to get the Parent verison to call

class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
