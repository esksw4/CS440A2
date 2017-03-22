
import tkinter
from tkinter import *

def cbc(id, tex):
    return lambda : callback(id, tex)

def callback(id, tex):
    s = 'At {} f is {}\n'.format(id, id**id/0.987)
    tex.insert(END, s)
    tex.see(END)             # Scroll if necessary

top = Tk()
tex = Text(master=top)
tex.pack(side=RIGHT)
bop = Frame()
bop.pack(side=LEFT)
for k in range(1,10):
    tv = 'Say {}'.format(k)
    b = Button(bop, text=tv, command=cbc(k, tex))
    b.pack()

Button(bop, text='Exit', command=top.destroy).pack()
top.mainloop()