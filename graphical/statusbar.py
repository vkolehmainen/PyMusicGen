from PyQt4 import Qt, QtGui

class StatusBar(Qt.QWidget):
    
    def __init__(self):
        
        super(Qt.QWidget, self).__init__()
        
        self.layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel("STATUSBAR")
        self.layout.addWidget(self.label)
        
        self.setAutoFillBackground(True)
        
        self.setLayout(self.layout)