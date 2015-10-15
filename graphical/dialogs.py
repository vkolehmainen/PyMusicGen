'''
Created on 14.10.2015

@author: Niklas
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QMimeData

class AddSongDialog(QtGui.QDialog):
    
    def __init__(self):
        """Shows the song dialog"""
        
        super(AddSongDialog, self).__init__()
        self.fname = None
        self.init_layout()
        self.setWindowTitle('Add new song')
        self.exec()
        
    def open_file_dialog(self):
            """Shows file explorer"""
            fdialog = QtGui.QFileDialog.getOpenFileName(self, 'Select file', "", "Text files (*.txt)")
            self.fname = fdialog
            self.file_label.setText(self.fname)
    
    def init_layout(self): 
        """Initializes the layout."""
        grid = QtGui.QGridLayout()
        
        self.name_field = QtGui.QLineEdit()
        self.key_field = QtGui.QLineEdit()
        
        self.file_label = QtGui.QLabel()
        file_button = QtGui.QPushButton('Select')
        file_button.clicked.connect(self.open_file_dialog)
    
        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        grid.addWidget(QtGui.QLabel('Song name'), 0, 0)
        grid.addWidget(self.name_field, 0, 1)
        grid.addWidget(QtGui.QLabel('Key'), 1, 0)
        grid.addWidget(self.key_field,  1, 1)
        grid.addWidget(file_button, 2, 0, 1, 2)
        grid.addWidget(buttons, 3, 0)
        grid.addWidget(self.file_label, 3, 1)
        
        self.setLayout(grid)
        
class ProfileDialog(QtGui.QDialog):
    
    def __init__(self, parent = None):
        """Shows the profile dialog."""
             
        super(ProfileDialog, self).__init__(parent)
               
        self.init_layout()
        self.exec()
        
    def init_layout(self):
        """Initializes the layout."""     
        
        self.name_field = QtGui.QLineEdit(self)    
                     
        self.channel_field = QtGui.QComboBox(self)  
        for channels in range (1,17):
            self.channel_field.addItem(str(channels))
                        
        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        grid = QtGui.QGridLayout()    
        grid.addWidget(QtGui.QLabel("Name:"), 0, 0)
        grid.addWidget(self.name_field, 0, 1)
        grid.addWidget(QtGui.QLabel('MIDI Channel:'), 1, 0)
        grid.addWidget(self.channel_field,  1, 1)
        grid.addWidget(buttons, 3, 0)  
        self.setLayout(grid)
        
        self.setWindowTitle('Profile dialog')
        
class SelectSongDialog(QtGui.QDialog):
    """Shows select song dialog"""
    
    def __init__(self):
        super(QtGui.QDialog, self).__init__()
        self.init_layout()
        self.setWindowTitle('Select songs to add')
        self.exec()
    
    def init_layout(self):
        layout = QtGui.QVBoxLayout()
        
        list_view = self.init_view()
        list_view.setDragEnabled(True)
        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        layout.addWidget(list_view)
        layout.addWidget(buttons)
        
        self.setLayout(layout)
    
    def init_view(self):
        test_values = ["Test song " + str(i+1) for i in range(10)]
        test_model = QtGui.QStringListModel(test_values)
        list_view = QtGui.QListView()
        list_view.setModel(test_model)
        return list_view
    
def add_song(self):
    "Opens a dialog to add a new song."""
    
    dialog = AddSongDialog()
    name = dialog.name_field.text()
    key = dialog.key_field.text()
    fname = dialog.fname
    
    if not name or not key or not fname:
        pass
    else:
        try:
            with open(fname, 'r') as f:
                chords = f.read() 
                print(name + "\n" + key + "\n" + chords)
        except IOError as e:
            print(e)
            
def add_profile(self):
    """Opens a dialog to add a new profile."""
    
    dialog = ProfileDialog()
    name = dialog.name_field.text()
    key = dialog.channel_field.currentText()
    print(name, key)
    
def select_songs(self):
    """Opens a dialog to select new songs"""
    dialog = SelectSongDialog()
    
    
    
    #TODO: empty field handling
        