from PyQt4 import QtGui

def add_menu(menubar, GUI):
    """Populates the menubar of the main window."""
    
    exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', GUI)        
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)
    
    file_menu = menubar.addMenu('&File')
    file_menu.addAction(exitAction)
    
    
    
    addAction = QtGui.QAction('&Add profile', GUI)
    addAction.triggered.connect(GUI.profile_view.profile_dialog)
    
    profile_menu = menubar.addMenu('&Profiles')
    profile_menu.addAction(addAction)
    
    
    