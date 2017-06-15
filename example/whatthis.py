


import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tkst
# class Example(tk.Frame):
#     def __init__(self, root):

#         tk.Frame.__init__(self, root)
#         self.canvas = tk.Canvas(root, borderwidth=0, background="#d3d3d3")
#         self.frame = tk.Frame(self.canvas, background="#ffffff")
#         self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
#         self.canvas.configure(yscrollcommand=self.vsb.set)

#         self.vsb.pack(side="right", fill="y")
#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
#                                   tags="self.frame")
#         self.frame.bind("<Configure>", self.onFrameConfigure)
#         self.pop()

#     def pop(self):
#         for i in range(100):
#             self.f = Label(self.frame, text=i,background="#ffffff", anchor="center")
#             self.f.pack(side="top", fill="both")

#     def onFrameConfigure(self, event):
#         '''Reset the scroll region to encompass the inner frame'''
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))


# if __name__ == "__main__":
#     root=tk.Tk()
#     root.geometry("800x500")
#     Example(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()



class App(object):

    def __init__(self):
        self.root = tk.Tk()

    # create a Text widget with a Scrollbar attached
        self.txt = tkst.ScrolledText(self.root, undo=True, state=DISABLED)
        self.txt['font'] = ('consolas', '12')
        self.txt.pack(expand=True, fill='both')
        self.txt.config(state=NORMAL)
        self.txt.insert(INSERT, "Is This Working")
        self.txt.config(state=DISABLED)

app = App()
app.root.mainloop()