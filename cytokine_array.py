import sys
sys.path.append('..')

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from gui.cytokine_array_gui import Ui_MainWindow
from excel import to_excel_error_barchart

class CytokineArrayGui(Ui_MainWindow):
    def setupUi(self, MainWindow) -> None:
        super().setupUi(MainWindow)
        self.namesbutton.clicked.connect(self.getnames)
        self.databutton.clicked.connect(self.getdata)
        self.runbutton.clicked.connect(self.run)
        self.dlg = QFileDialog()
        self.dlg.setFileMode(QFileDialog.AnyFile)
        self.dlg.setNameFilter("CSV files (*.csv)")

    def filesfound(self):
        if not self.namesfile: 
            print("No namesfile found")
            return False
        if not self.datafile:
            print("No datafile found")
            return False
        return True

    def run(self):
        if not self.filesfound():
            return
        df = pd.read_csv(self.datafile)
        to_excel_error_barchart(df)

    def getnames(self):
        self.namesfile = self.getfile()
        self.nameslabel.setText(self.namesfile)
        self.update(self.nameslabel)

    def getdata(self):
        self.datafile = self.getfile()
        self.datalabel.setText(self.datafile)
        self.update(self.datalabel)

    def getfile(self):
        self.dlg.exec_()
        return self.dlg.selectedFiles()[0]

    def update(self, label):
        label.adjustSize()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = CytokineArrayGui()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())