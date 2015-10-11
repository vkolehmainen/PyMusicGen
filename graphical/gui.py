import sys, os
from PyQt4 import QtGui, QtCore

from graphical.menubar import add_menu
from graphical.melodyview import MelodyView
from graphical.profileselect import ProfileSelect
from graphical.profileview import ProfileView
from graphical.rhythmview import RhythmView
from graphical.statusbar import StatusBar
from graphical.visualizer import Visualizer


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
        
        # left widgets
        self.status_bar = StatusBar()
        self.profile_view = ProfileView()
        self.visualizer = Visualizer()
        
        # right widgets
        self.profile_select = ProfileSelect()   
        self.rhythm_view = RhythmView()  
        self.melody_view = MelodyView()
            
        # left splitter
        self.splitter1 = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.splitter1.addWidget(self.status_bar)
        self.splitter1.addWidget(self.profile_view)
        self.splitter1.addWidget(self.visualizer)
        
        # right splitter
        self.splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.splitter2.addWidget(self.profile_select)
        self.splitter2.addWidget(self.rhythm_view)
        self.splitter2.addWidget(self.melody_view)
              
        # joins the left and right splitters together  
        self.splitter3 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter3.addWidget(self.splitter1)
        self.splitter3.addWidget(self.splitter2)
        
    
    def init_menu(self):
        """Initializes the menu bar."""
        
        add_menu(self.menuBar(), self)
    
    def init_layout(self):
        """Initializes the layout."""              

        self.statusBar().showMessage('Ready')
        
        self.setCentralWidget(self.splitter3)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

        self.setGeometry(150, 90, 1600, 900)
        self.setWindowTitle('PyMusicGen')
        self.setBackgroundRole(QtGui.QPalette.Base)  
        self.show()
        
    def init_core(self):
        """Initializes the core."""
        
        pass


if __name__ == '__main__':
    main()