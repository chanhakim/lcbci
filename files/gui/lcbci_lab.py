"""
lcbci_lab.py is a GUI for interacting with a BCI

@author : Chanha Kim
@date   : 07/06/2020
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from _widgets import *
import serial

class lcbci_lab(QMainWindow):

    def __init__(self):
        super(lcbci_lab, self).__init__()
        self.configure_ui()
        self.resize(1200, 900)
    
    def configure_ui(self):
        self.setWindowTitle('lcbci lab v0.1')
        self.main = MainWidget()
        self.buttons = ButtonsWidget()
        
        layout = QHBoxLayout()
        layout.addWidget(self.main)
        layout.addWidget(self.buttons)
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def connect_arduino(self):
        self.arduino = serial.Serial('')

    def _update_data(self):
        None

    def _save_data(self):
        None

    def _open_data_file(self):
        None

    def _start_data_stream(self):
        None

    def _stop_data_stream(self):
        None

        


def main():
    app = QApplication(sys.argv)
    main_window = lcbci_lab()
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
