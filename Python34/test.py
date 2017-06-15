import tkinter
import tkinter.messagebox as msg
import tkinter.simpledialog as dlg
import Login_Security
import DashBoardPage
import HiringStatusPage
import OrderNewReport
import Functions
import unittest, time, re
import webbrowser


from tkinter import *

# def cbc(id, tex):
#     return lambda : callback(id, tex)

# def callback(id, tex):
#     s = 'At {} f is {}\n'.format(id, id**id/0.987)
#     tex.insert(END, s)
#     tex.see(END)             # Scroll if necessary

# top = Tk()
# tex = Text(master=top)
# tex.pack(side=LEFT)
# bop = Frame()
# bop.pack(side=RIGHT)
# for k in range(1,10):
#     tv = 'Say {}'.format(k)
#     b = Button(bop, text=tv, command=cbc(k, tex))
#     b.pack()

# Button(bop, text='Exit', command=top.destroy).pack()
# top.mainloop()


import tkinter as tk
import time
import sys

class Display(tk.Frame):
    def __init__(self):
       tk.Frame.__init__(self)
       self.doIt = tk.Button(self,text="Start", command=self.start, background = 'black', fg='white')
       self.doIt.pack()

       self.output = tk.Text(self, width=100, height=15, background = 'black', fg='white')
       self.output.pack(side=tk.LEFT)

       self.scrollbar = tk.Scrollbar(self, orient="vertical", command = self.output.yview)
       self.scrollbar.pack(side=tk.RIGHT, fill="y")

       self.output['yscrollcommand'] = self.scrollbar.set

       self.count = 1
       self.configure(background='black')
       self.pack()


    def start(self):
        if self.count < 1000:
            self.write(str(self.count) + '\n')
            print (self.count)
            self.count += 1
            self.after(2000, self.start)


    def write(self, txt):
        self.output.insert(tk.END,str(txt))
        self.update_idletasks()


if __name__ == '__main__':
    Display().mainloop()