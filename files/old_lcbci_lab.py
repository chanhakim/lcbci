'''
lcbci_lab.py is a serial UI interface

The program is adapted from ZetCode's tutorial
on Tkinter's layout management. The tutorial can
be found here: http://zetcode.com/tkinter/layout/

@author : Chanha Kim
@date   : 07/06/2020
'''

import tkinter as tk
from tkinter import W, N, E, S, ttk

class lcbci_lab(ttk.Frame):
    def __init__(self):
        self.initialize_root()
        self.configure_grid()
        self.create_title()
        self.create_main_frame()
        self.create_control_frame()
        self.create_sub_frame()

    def initialize_root(self):
        self.parent = tk.Tk()
        self.parent.geometry("800x600+300+300")
        self.parent.minsize(600, 450)
        super().__init__(self.parent)
        self.parent.title("lcbci_lab_v0.1")
        self.pack(fill=tk.BOTH, expand=True)

    def configure_grid(self):
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=5)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, pad=7)

    def create_title(self):
        label = ttk.Label(self, text="lcbci lab v0.1")
        label.grid(sticky=W, padx=5, pady=(5, 0))

    def create_main_frame(self):
        self.main_frame = tk.Frame(self, bg="#80c1ff")
        self.main_frame.grid(row=1, column=0, rowspan=4, columnspan=2, pady=5, padx=5, sticky=E+W+S+N)
        label = tk.Label(self.main_frame, text="Main Frame", bg="#80c1ff")
        label.pack()


    def create_control_frame(self):
        self.sub_frame = tk.Frame(self)
        self.sub_frame.grid(row=1, column=2, rowspan=4, padx=(0, 5), pady=5, sticky=N)

        open_bn = ttk.Button(self.sub_frame, text="Open")
        open_bn.pack()

        play = ttk.Button(self.sub_frame, text="Play")
        play.pack()

        start = ttk.Button(self.sub_frame, text="Start")
        start.pack()

        stop = ttk.Button(self.sub_frame, text="Stop")
        stop.pack()

        record = ttk.Button(self.sub_frame, text="Record")
        record.pack()

        save = ttk.Button(self.sub_frame, text="Save")
        save.pack()

    def create_sub_frame(self):
        self.sub_frame = tk.Frame(self, bg="red")
        self.sub_frame.grid(row=5, column=0, rowspan=1, columnspan=2, padx=5, pady=(0,5), sticky=N+S+E+W)
        label = tk.Label(self.sub_frame, text="Print Dialog", bg='red', fg='white')
        label.pack()

def main():
    app = lcbci_lab()
    app.mainloop()

if __name__ == '__main__':
    main()