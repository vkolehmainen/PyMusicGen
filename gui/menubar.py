from PyQt4 import QtGui

def add_menu(menubar, GUI):
    """Populates the menubar of the main window."""
    
    exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', GUI)        
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)
    
    file_menu = menubar.addMenu('&File')
    file_menu.addAction(exitAction)
    
    
    
    