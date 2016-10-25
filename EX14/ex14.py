from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Where are you from %s?" % user_name
froms = raw_input(prompt)

print "Where have you been %s?" % user_name
beens = raw_input(prompt)

print "Where are you going?"
goins = raw_input(prompt)

print """
Alright, so you said you're from %r.
You've been to %r.  That must have been cool.
And you're planning on going %r.  Decent.
""" % (froms, beens, goins)
