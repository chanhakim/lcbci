"""
_backend.py handles the data streaming from pyserial

@author: chanhakim
@date: 08/12/2020 
"""

import serial
from serial.tools import list_ports
from _widgets import lcbci_widgets
from pathlib import Path
from PyQt5.QtGui import QFileDialog
import numpy as np

class lcbci_backend():
    
    def __init__(self):
        self.widgets = lcbci_widgets()
        self._connect_widgets()
        self.data = []
        self._refresh_comports()
        self.due = None
        self.port_id, self.baud_rate = None, None

    def _connect_widgets(self):
        """Connects all the buttons."""
        self.widgets.open.clicked.connect(self._open_data)
        self.widgets.save.clicked.connect(self._save_data)
        self.widgets.start.clicked.connect(self._start_stream)
        self.widgets.stop.clicked.connect(self._stop_stream)
        self.widgets.record.clicked.connect(self._record_data)
        self.widgets.play.clicked.connect(self._play_data)
        self.widgets.connect.clicked.connect(self._connect_arduino)
        self.widgets.refresh_ports.clicked.connect(self._refresh_comports)
        self.widgets.port.activated.connect(self._set_arduino_port)
        self.widgets.baud.activated.connect(self._set_arduino_baud_rate)
        self.widgets.record90s.clicked.connect(self._record_90s)

    def show_ui(self):
        self.widgets.show()

    def _refresh_comports(self):
        ports_list = ['Port ID']
        for port_object in list(serial.tools.list_ports.comports(True)):
            ports_list.append(port_object[0])
        self.widgets.port.clear()
        self.widgets.port.addItems(ports_list)
        print('Refreshing port options.')

    def _set_arduino_port(self):
        """Assumes that the Arduino is connected to port_id.
           Sets the port_id as a class variable."""
        self.port_id = self.widgets.port.currentText()
        print(self.port_id, 'was selected.')

    def _set_arduino_baud_rate(self):
        """Sets the baud_rate to the desired rate."""
        self.baud_rate = int(self.widgets.baud.currentText()) if self.widgets.baud.currentText() != 'Baud Rate' else None
        print(self.baud_rate, 'baud was selected.')

    def _connect_arduino(self):
        """Requires that port_id is a valid port
           Instantiates a serial.Serial object."""
        if self.due != None: self.due.close()
        try:
            self.due = serial.Serial(self.port_id, self.baud_rate, timeout=4)
            print('Arduino at', self.port_id, 'was succesfully connected.')
        except:
            print('An error occured while connecting to the Arduino.')

    def clear_data(self):
        """Clears the data."""
        self.data = []

    def _open_data(self):
        """Opens a csv file with data."""
        if self.data != None:
            #self.save_data()
            self.data = None
        self.data = None # this should be the loaded data
        file_name, _ = self.widgets.file_dg.getOpenFileName(self.widgets.file_dg, "Open file", str(Path.home()), '*.csv', options=QFileDialog.DontUseNativeDialog)
        print('Opening file:', file_name)

    def _save_data(self):
        """Saves the data at the output path."""
        self.widgets.exporter.export()

    def __update(self, record_all=False, record_time=None):
        while self.due.inWaiting() == 0:
            pass
        new_sample = due.readLine()

    def _start_stream(self):
        """Initiates the data stream."""
        self.widgets.timer.timeout.connect(self.__update)
        self.widgets.timer.start(0)
        print('Starting EEG stream.')

    def _stop_stream(self):
        """Stops the data stream."""
        self.widgets.timer.stop()
        print('Stopping EEG stream.')

    def _record_data(self):
        """Records the data stream."""
        # self.widgets.timer.timeout.connect(self.__update, True)
        # self.widgets.timer.start(0)
        print('Recording EEG.')

    def _record_90s(self):
        print('Recording 90 seconds of EEG.')

    def _play_data(self):
        """Plays back the recorded data."""
        print('Playing back EEG recording.')

