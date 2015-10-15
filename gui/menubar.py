from PyQt4 import QtGui
import gui.dialogs as dialogs

def add_menu(menubar, GUI):
    """Populates the menubar of the main window."""
    
    exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', GUI)        
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)
    
    file_menu = menubar.addMenu('&File')
    file_menu.addAction(exitAction)
    
    addAction = QtGui.QAction('&Add profile', GUI)
    addAction.triggered.connect(dialogs.add_profile)
    
    profile_menu = menubar.addMenu('&Profiles')
    profile_menu.addAction(addAction)
    
    addSongAction = QtGui.QAction('&Add song', GUI)
    addSongAction.triggered.connect(dialogs.add_song)
    
    showDockAction = GUI.songs_dock.toggleViewAction()
    
    song_menu = menubar.addMenu('&Songs')
    song_menu.addAction(addSongAction)
    
    window_menu = menubar.addMenu('&Window')
    show = window_menu.addMenu('&Show')
    show.addAction(showDockAction)
    
    
    
    