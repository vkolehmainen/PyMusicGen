import sys, os
from PyQt4 import QtGui
from graphical.menubar import add_menu

os.chdir(os.path.dirname(sys.argv[0]))

def main():

    app = QtGui.QApplication(sys.argv)
    main_window = GUI()
    sys.exit(app.exec_())

class GUI(QtGui.QMainWindow):

    def __init__(self):
        """Implements the game's user interface and its functionalities."""
        
        super(GUI, self).__init__()
        
        self.create_widgets()
        self.init_menu()
        self.init_layout()
        self.init_core()
        
    def create_widgets(self):
        """Creates the widgets."""
        
        pass
    
    def init_menu(self):
        """Initializes the menu bar."""
        
        add_menu(self.menuBar(), self)
    
    def init_layout(self):
        """Initializes the layout."""              

        self.statusBar().showMessage('Ready')

        self.setGeometry(150, 90, 1600, 900)
        self.setWindowTitle('PyMusicGen')    
        self.show()
        
    def init_core(self):
        """Initializes the core."""
        
        pass


if __name__ == '__main__':
    main()