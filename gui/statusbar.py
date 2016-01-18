from PyQt4 import Qt, QtGui, QtCore

class StatusBar(Qt.QWidget):
    
    def __init__(self, MainWindow):
        
        super(Qt.QWidget, self).__init__()
        
        self.MainWindow = MainWindow
        
        self.layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel("STATUSBAR")
        self.layout.addWidget(self.label)
        
        self.setAutoFillBackground(True)
        
        self.setLayout(self.layout)
        
        self.BPM_label = QtGui.QLabel(parent = self)
        self.BPM_label.setGeometry(30, 20, 100, 30)
        
        self.BPM_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.BPM_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.BPM_slider.setRange(1, 200)
        self.BPM_slider.setGeometry(30, 40, 100, 30)
        self.BPM_slider.valueChanged[int].connect(self.change_BPM_value)
        
    def change_BPM_value(self):
        
        self.BPM_label.setText("BPM: " + str(self.BPM_slider.value()))
        self.MainWindow.logic.set_BPM(self.BPM_slider.value())
        self.MainWindow.logic.set_timer_interval()