#!/usr/bin/env python
'''
flicker_lab.py is a serial UI interface

The program is adapted from ZetCode's tutorial
on Tkinter's layout management. The tutorial can
be found here: http://zetcode.com/tkinter/layout/

@author : Chanha Kim
@date   : 08/10/2020
'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import numpy as np

class grid:
    def __init__(self, canvas, fps):
        self.canvas = canvas
        self.fps = fps
        self.grid = []
        for x in range(0, 8):
            for y in range(0, 8):
                self.grid.append([self.canvas.create_rectangle(10+x*100, 10+y*100, 10+x*100+100, 10+y*100+100, fill='black' if ((y%2==0 and x%2==1) or (y%2==1 and x%2==0)) else 'white', outline='black'), True if ((y%2==0 and x%2==1) or (y%2==1 and x%2==0)) else False])
        self.active = False
        self.flicker_active()

    def update_grid(self):
        for i in range(len(self.grid)):
            if self.grid[i][1] == True:
                self.canvas.itemconfig(self.grid[i][0], fill='white')
                self.grid[i][1] = False
            else:
                self.canvas.itemconfig(self.grid[i][0], fill='black')
                self.grid[i][1] = True

    def flicker_active(self):
        if self.active:
            self.update_grid()
            if self.fps != 0:
                self.canvas.after(int(1000/self.fps), self.flicker_active)

    def update_fps(self, fps):
        if self.fps == float(0):
            self.fps = fps
            self.flicker_active()
        else:
            self.fps = fps
        # print('status:', 'on' if self.active else 'off', '|', 'fps:', self.fps)

    def start(self):
        self.active = True
        self.flicker_active()
        # print('status:', 'on' if self.active else 'off', '|', 'fps:', self.fps)

    def stop(self):
        self.active = False
        # print('status:', 'on' if self.active else 'off', '|', 'fps:', self.fps)


class flicker_lab(ttk.Frame):
    def __init__(self):
        self.fps = 0
        self.fps_values = {
            0:'0.00',
            1:'0.25',
            2:'0.50',
            3:'1.00',
            4:'2.00',
            5:'4.00',
            6:'8.00',
            7:'16.0',
            8:'32.0',
            9:'64.0',
            10:'128.'
        }
        self.initialize_root()
        self.configure_grid()
        self.create_main_frame()
        self.create_control_frame()

    def initialize_root(self):
        self.parent = tk.Tk()
        self.parent.geometry("900x900")
        self.parent.resizable(0,0)
        super().__init__(self.parent)
        self.parent.title("flicker_lab_v0.1")
        self.pack(fill=tk.BOTH, expand=True)

    def configure_grid(self):
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

    def create_main_frame(self):
        self.main_frame = tk.Frame(self, bg="white", width=810, height=810)
        self.main_frame.pack(side='top', pady=(10,5))
        self.canvas = tk.Canvas(self.main_frame, bg="white", width=810, height=810)
        self.canvas.pack(padx=(0,5), pady=(0,5))
        self.grid = grid(self.canvas, self.fps)

    def start_flicker(self):
        if self.grid.active == False:
            self.grid.start()
            # self.start_time = time.time()

    def stop_flicker(self):
        if self.grid.active == True:
            self.grid.stop()
            # self.stop_time = time.time()
            # print(str(int(self.stop_time - self.start_time))+'s')

    def update_fps(self, fps):
        self.fps = fps
        self.fps_var.set(self.fps_values[int(self.fps)])
        self.grid.update_fps(float(self.fps_values[int(self.fps)]))
            

    def create_control_frame(self):

        self.sub_frame = ttk.Frame(self)
        self.sub_frame.pack(side='top', pady=(5, 0))

        scale_label = ttk.Label(self.sub_frame, text='FPS')
        scale_label.pack(side='left')
        self.scale = tk.Scale(self.sub_frame, orient='horizontal', from_=0, to=9, resolution=1, length=300, showvalue=False, command=self.update_fps)
        self.scale.pack(side='left')
        self.fps_var = StringVar()
        self.fps_var.set(self.fps_values[self.fps])
        fps_label = ttk.Label(self.sub_frame, textvariable=self.fps_var)
        fps_label.pack(side='left')

        self.sub_frame = ttk.Frame(self)
        self.sub_frame.pack(side='top', pady=5)

        start = ttk.Button(self.sub_frame, text="Start", command=self.start_flicker)
        start.pack(side='left')

        stop = ttk.Button(self.sub_frame, text="Stop", command=self.stop_flicker)
        stop.pack(side='left')


def main():
    app = flicker_lab()
    try:
        app.mainloop() 
    # try:
    #     app.start_flicker()
    #     print('status:', 'on')
    #     app.update()
    #     time.sleep(3)
    #     beg = time.time()
    #     for i in range(10):
    #         app.scale.set(i)
    #         app.update()
    #         print('fps:', app.grid.fps)
    #         start = time.time()
    #         while int(time.time() - start) < 4:
    #             app.update()
    #         print('  time elapsed:', str(int(time.time() - beg))+'s')
    #     for i in range(9, -1, -1):
    #         app.scale.set(i)
    #         app.update()
    #         print('fps:', app.grid.fps)
    #         start = time.time()
    #         while int(time.time() - start) < 4:
    #             app.update()
    #         print('  time elapsed:', str(int(time.time() - beg))+'s')
    #     print('total time:', str(int(time.time()-beg))+'s')
    except TclError:
        pass # to avoid errors when the window is closed

if __name__ == '__main__':
    main()