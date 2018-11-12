import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class CashBookForm(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Dòng Tiền")
        self.setFixedSize(500, 500)
