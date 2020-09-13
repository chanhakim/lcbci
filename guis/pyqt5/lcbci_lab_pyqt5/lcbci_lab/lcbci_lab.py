"""
lcbci_lab.py is a GUI for interacting with a BCI

@author : Chanha Kim
@date   : 07/06/2020
"""

import sys
from PyQt5.QtWidgets import QApplication, QShortcut
from PyQt5.QtGui import QKeySequence

from _backend import lcbci_backend

class lcbci_lab(QApplication):

    def __init__(self):
        super(lcbci_lab, self).__init__(sys.argv)
        self.backend = lcbci_backend()
        self.backend.show_ui()

    def start_gui(self):
        sys.exit(self.exec_())

def main():
    app = lcbci_lab()
    #print(app.backend.data)
    app.start_gui()

if __name__ == '__main__':
    main()