"""
Custom widgets for lcbci_lab.py

@author: chanhakim
@date: 08/12/2020
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg


class _qline(QFrame):
    """Creates a line widget"""
    def __init__(self):
        super(_qline, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class _open_button(QPushButton):
    def __init__(self):
        super(_open_button, self).__init__('Open')

class _save_button(QPushButton):
    def __init__(self):
        super(_save_button, self).__init__('Save')

class _start_button(QPushButton):
    def __init__(self):
        super(_start_button, self).__init__('Start')

class _stop_button(QPushButton):
    def __init__(self):
        super(_stop_button, self).__init__('Stop')

class _record_button(QPushButton):
    def __init__(self):
        super(_record_button, self).__init__('Record')

class _play_button(QPushButton):
    def __init__(self):
        super(_play_button, self).__init__('Play')

class _eeg_graph(pg.PlotWidget):
    def __init__(self):
        super(_eeg_graph, self).__init__()




class ButtonsWidget(QWidget):
    """A class for holding the control buttons"""

    def __init__(self):
        super(ButtonsWidget, self).__init__()
        self._create_buttons()
        self._create_widget()

    def _create_buttons(self):
        self.file = {
            'open': _open_button(),
            'save': _save_button()
        }
        self.control = {
            'start': QPushButton('Start'),
            'stop': QPushButton('Stop'),
            'record': QPushButton('Record'),
            'play': QPushButton('Play'),
        }
        self.arduino = {
            'port': QComboBox(),
            'connect': QPushButton('Connect')
        }
        self.arduino['port'].addItem('Port ID')
        self.arduino['port'].setFixedWidth(100)

    def _create_widget(self):
        layout = QVBoxLayout()
        file_label = QLabel('File Options')
        file_label.setAlignment(Qt.AlignCenter)
        control_label = QLabel('Control Options')
        control_label.setAlignment(Qt.AlignCenter)
        arduino_label = QLabel('Arduino Options')
        arduino_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(QLabel(' '))
        layout.addWidget(file_label)
        for button in list(self.file.values()):
            layout.addWidget(button)
        layout.addWidget(_qline())
        layout.addWidget(control_label)
        for button in list(self.control.values()):
            layout.addWidget(button)
        layout.addWidget(_qline())
        layout.addWidget(arduino_label)
        for button in list(self.arduino.values()):
            layout.addWidget(button)

        layout.addStretch()
        self.setLayout(layout)
        

class MainWidget(QWidget):
    """A class for holding the graph and folder dialog"""
    def __init__(self):
        super(MainWidget, self).__init__()
        self._create_elements()
        self._place_elements()

    def _create_elements(self):
        self.graph = _eeg_graph()
        self.sub = None

    def _place_elements(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('lcbci lab v0.1'))
        layout.addWidget(self.graph)
        self.setLayout(layout)

        
