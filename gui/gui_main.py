# from https://www.youtube.com/watch?v=-2uyzAqefyE
# to open designer `Scripts/pyqt5-tools.exe designer`
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow,  self).__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Cytokine Array Analysis")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Data")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Push my buttons!")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You clicked the button!")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = myWindow()

    win.show()
    sys.exit(app.exec_())

window()