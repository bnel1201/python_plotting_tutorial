from pathlib import Path
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
        self.update(self.namesbutton)
        self.update(self.databutton)
        self.runbutton.clicked.connect(self.run)
        self.dlg = QFileDialog()
        self.dlg.setFileMode(QFileDialog.AnyFile)
        self.dlg.setNameFilter("CSV files (*.csv)")
        self.enter_filename.setText("untitled.xlsx")

    def filesfound(self):
        if not self.namesfile: 
            print("No namesfile found")
            return False

        if not Path(self.namesfile).exists():
            print("names file does not exist")
            return False

        if not Path(self.datafile).exists():
            print("Data file does not exist")
            return False

        if not self.datafile:
            print("No datafile found")
            return False
        return True

    def run(self):
        if not self.filesfound():
            return
        df = pd.read_csv(self.datafile)
        filename = self.enter_filename.toPlainText()
        to_excel_error_barchart(df, filename=filename, xlabel="Cytokine", ylabel="Normalized Intensity")
        self.runbutton.setText("Done!")

    def getnames(self):
        self.namesfile = self.getfile()
        self.nameslabel.setText(self.namesfile)
        self.update(self.nameslabel)

    def getdata(self):
        self.datafile = self.getfile()
        self.datalabel.setText(self.datafile)
        self.update(self.datalabel)

    def getfile(self):
        self.runbutton.setText("Run")
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