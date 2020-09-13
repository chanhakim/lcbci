import sys
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import ptime as time
import numpy as np
import pyqtgraph as pg
import serial

# due = serial.Serial('/dev/cu.usbmodem14101', 115200)
# while True:
#     while due.in_waiting == 0:
#         pass
#     lines = due.readlines(-1)
#     print(lines)

# """
# The following is adapted from JaFeKI's joystick_real_time_plot_with_pyqtgraph (on GitHub)
# """

class pyqt_serial(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(pyqt_serial, self).__init__(parent)

        # set up the GUI
        self.main_view = QtGui.QWidget()
        self.setCentralWidget(self.main_view)
        self.graph = pg.plot()
        self.fps_label = QtGui.QLabel()
        self.start = QtGui.QPushButton('Start')
        self.stop = QtGui.QPushButton('Stop')
        self.connect = QtGui.QPushButton('Due')
        button_widget = QtGui.QWidget()
        button_layout = QtGui.QHBoxLayout()
        button_layout.addWidget(self.start)
        button_layout.addWidget(self.stop)
        button_layout.addWidget(self.connect)
        button_widget.setLayout(button_layout)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.graph)
        layout.addWidget(self.fps_label)
        layout.addWidget(button_widget)
        self.main_view.setLayout(layout)

        # connect buttons
        self.start.clicked.connect(self._start_recording)
        self.stop.clicked.connect(self._stop_recording)
        self.connect.clicked.connect(self._connect_due)
        
        # set up the plot
        self.graph.setTitle('Real-time serial plotting')
        self.graph.setXRange(-100, 0)
        self.graph.setLimits(xMax=0)
        self.graph.setYRange(-1.2, 1.2)
        x_axis = self.graph.getAxis('bottom')
        y_axis = self.graph.getAxis('left')
        x_axis.setLabel(text='Time')
        y_axis.setLabel(text='Potentiometer Reading (Ohms)')

        # initializing sensor data
        self.numPoints = None
        self.data = np.empty(100)
        self.fps = 0.
        self.counter = 0
        self.lastupdate = time.time()

        # initialize the timer
        self.timer = QtCore.QTimer()
        self.drawplot = self.graph.plot()

    def _connect_due(self):
        self.due = serial.Serial('/dev/cu.usbmodem14101', 115200)
        print('Successfully connectd Arduino Due')

    def _start_recording(self):
        self.starttime = time.time()
        self.timer.timeout.connect(self._update)
        self.due.reset_input_buffer()
        self.ptr3 = 0
        self.timer.start(1)

    def _stop_recording(self):
        self.timer.stop()

    def _framerate(self):
        now = time.time()
        frame_seconds = (now - self.lastupdate)
        if frame_seconds <= 0: frame_seconds = 0.000000000001
        current_fps = 1.0 / frame_seconds
        self.lastupdate = now
        self.fps = self.fps * 0.9 + current_fps * 0.1
        self.fps_label.setText('Mean Frame Rate: {fps:.3f} FPS'.format(fps=self.fps))
        self.counter += 1

    def _update(self):
        while (self.due.in_waiting == 0):
            pass
        self.data[self.ptr3] = float(self.due.readline().decode('utf-8', 'backslashreplace').rstrip('\n'))
        self.ptr3 += 1
        if self.ptr3 >= self.data.shape[0]:
            temp = self.data
            self.data = np.empty(self.data.shape[0]*2)
            self.data[:temp.shape[0]] = temp
        self.drawplot.setData(self.data[:self.ptr3])
        self.drawplot.setPos(-self.ptr3, 0)
        self._framerate()


def main():
    app = QtGui.QApplication(sys.argv)
    plot = pyqt_serial()
    plot.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()