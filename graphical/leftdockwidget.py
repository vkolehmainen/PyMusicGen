'''
Created on 15.10.2015

@author: Niklas
'''
from PyQt4 import QtGui

class SongsDockWidget(QtGui.QDockWidget):
    """Handles DockWidget containing selected songs"""
    def __init__(self):
        super(QtGui.QDockWidget, self).__init__()
        self.setWindowTitle('Selected songs')
        container = self.init_layout()
        self.setWidget(container)
    
    def init_layout(self):
        """Initializes the layout."""
        container = QtGui.QWidget()
        layout = QtGui.QVBoxLayout()
        
        list_view = QtGui.QListView()
        list_view.setResizeMode(QtGui.QListView.Adjust)
        
        layout.addWidget(list_view)
        
        container.setLayout(layout)
        return container

    