"""
gui01.py
The most basic Qt Program.
Opens an empty WIndow and moves it to the upper left corner of the screen.
"""

# PyQt5 is a master moduel that we downloaded
#and the Modules application and widget should be imported
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__() # super: let's you access methods of your superclass, you want the super class to do the things it usually does, but you also want to add the GUI stuff
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('A First Window')
        self.resize(250, 150) # these numbers are coordinates on your desktop

# boiler plate code
if __name__ == "__main__":
    app = QApplication(sys.argv) # create the application
    mywindow = MyWindow() # create an instance(mywindow) of your window, if there wer something in teh ()'s, it'd go into the __init__
    mywindow.move(0, 0) # potitioning the window in the top left corner
    mywindow.show() # tell Qt to make your window visible (not invisible like the default)
    sys.exit(app.exec_()) # start the event loop (exec: execute, start), the while loop is basicaly inside
