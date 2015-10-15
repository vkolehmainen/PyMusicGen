'''
Created on 15.10.2015

@author: Niklas
'''
from PyQt4 import QtGui
import gui.dialogs as dialogs

class SongsDockWidget(QtGui.QDockWidget):
    def __init__(self):
        """Handles DockWidget containing selected songs"""
        super(QtGui.QDockWidget, self).__init__()
        self.setWindowTitle('Selected songs')
        container = self.init_layout()
        self.setWidget(container)
        
    
    def init_layout(self):
        """Initializes the layout."""
        container = QtGui.QWidget()
        layout = QtGui.QVBoxLayout()
        
        list_view = SongView().get_view()
        
        add_button = QtGui.QPushButton('add')
        add_button.clicked.connect(dialogs.select_songs)
        remove_button = QtGui.QPushButton('remove')
    
        layout.addWidget(list_view)
        layout.addWidget(add_button)
        layout.addWidget(remove_button)
        
        container.setLayout(layout)
        return container

class SongView(QtGui.QListView):
    
    def __init__(self, string_list = []):
        """ Implements custom QListView class with added drag&drop functionality"""
        
        super(QtGui.QListView, self).__init__()
        self.model = self.get_model(string_list)
        self.view = QtGui.QListView()
        self.view.setModel(self.model)
        self.setResizeMode(QtGui.QListView.Adjust)
      
    def get_model(self, string_list):
        return QtGui.QStringListModel(string_list)
  
    def dragEnterEvent(self, e):
        pass

    def dropEvent(self, e):
        pass
  
    def get_view(self):
        return self.view