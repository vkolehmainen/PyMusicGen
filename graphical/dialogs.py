'''
Created on 14.10.2015

@author: Niklas
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

class AddSongDialog(QtGui.QDialog):
    
    def __init__(self):
        super(AddSongDialog, self).__init__()
        self.init_layout()
    
    def init_layout(self):
        
        def open_file_dialog(self):
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')
            self.fname = fname
            
        grid = QtGui.QGridLayout()
        
        self.name_field = QtGui.QLineEdit()
        self.key_field = QtGui.QLineEdit()
        
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
    
def add_song(db_manager):
    dialog = AddSongDialog(db_manager)
    name = dialog.name_field.text()
    key = dialog.key_field.text()
    fname = dialog.fname
    
    if not name or not key:
        pass
    try:
        with open(fname, 'r') as f:
            chords = f.read() 
    except IOError as e:
        print(e)
        
    print(name + "\n", key + "\n", chords)