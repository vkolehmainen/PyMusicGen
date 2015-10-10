from PyQt4 import Qt, QtGui

class Visualizer(Qt.QWidget):
    
    def __init__(self):
        
        super(Qt.QWidget, self).__init__()
        
        self.layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel("VISUALIZER")
        self.layout.addWidget(self.label)
        
        self.setAutoFillBackground(True)

        self.setLayout(self.layout)