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
        self.create_widgets()

    def initialize_root(self):
        self.parent = tk.Tk()
        self.parent.geometry("800x600+300+300")
        super().__init__(self.parent)
        self.parent.title("lcbci_lab_v0.1")
        self.pack(fill=tk.BOTH, expand=True)

    def configure_grid(self):
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

    def create_widgets(self):
        lbl = ttk.Label(self, text="lcbci lab v0.1")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = tk.Text(self, bg="white", font=("sans", 12))
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

        start = ttk.Button(self, text="Start")
        start.grid(row=1, column=3, padx=5)

        stop = ttk.Button(self, text="Stop")
        stop.grid(row=2, column=3, pady=4, padx=5)

        hbtn = ttk.Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = ttk.Button(self, text="Export")
        obtn.grid(row=5, column=3, padx=5)

def main():
    app = lcbci_lab()
    app.mainloop()

if __name__ == '__main__':
    main()