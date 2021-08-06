import os
import sys
import subprocess
import traceback
import ctypes
import tempfile as tmp
from pathlib import Path

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QGuiApplication
import pyperclip


class lunch_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(lunch_ui, self).__init__()
        uic.loadUi("main.ui", self)
        self.trim_nl.clicked.connect(self.trimLine)
        self.copy.clicked.connect(self.copyTxt)
        self.input_text = self.input.toPlainText()
        self.input.setText("Put yout Text here")
        self.output_text = self.output.toPlainText()
        self.output.setText("Output Text")
        self.clipboard = QGuiApplication.clipboard()

    def trimLine(self):
        self.input_text = self.input.toPlainText().replace('\n', ' ')
        self.output.setText(self.input_text)
        pyperclip.copy(self.input_text)

    def copyTxt(self):
        self.output.clear()
        self.input.clear()


app = QtWidgets.QApplication([])
win = lunch_ui()
win.show()
sys.exit(app.exec())
