from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Volatility Calculator")
        self.setGeometry(100, 60, 600, 500)
        self.item_input = QLineEdit(self)
        self.item_input.move(50, 50)

    def calcForItem(self):
        pass


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
