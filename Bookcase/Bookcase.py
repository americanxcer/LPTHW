# Blueprint for pumping out new bookcases
class Bookcase(object):
  # This is where you set up your new instance
  def __init__(self, w, h):
    print "Initializing a new bookcase"
    self.width = w
    self.height = h

    # Here's how you make a bookcase from the Blueprint
a = Bookcase(10, 200)
