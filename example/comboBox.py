from tkinter import *
from tkinter import ttk
 
from demopanels import MsgPanel, SeeDismissPanel
 
class ComboBoxDemo(ttk.Frame):
     
    def __init__(self, isapp=True, name='comboboxdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Combobox Demo')
        self.isapp = isapp
        self._create_widgets()
         
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self,
                     ["Three different spin-boxes are displayed below. ",
                      "The first is fully editable, pressing 'Return' adds ",
                      "the entered text to the list. The second is disabled. ",
                      "The third is a pre-defined, non-editable list.\n",
                      "Select a value using the up/down arrowhead keys or ",
                      "keyboard up/down arrow keys."])
             
            SeeDismissPanel(self)
         
        self._create_demo_panel()
         
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
             
        # create comboboxes
        cbp1 = ttk.Labelframe(demoPanel, text='Fully Editable')
        cb1 = ttk.Combobox(cbp1)
        cb1.bind('<Return>', self._update_values)
        cb1.pack(pady=5, padx=10)
 
        cbp2 = ttk.Labelframe(demoPanel, text='Disabled')
        ttk.Combobox(cbp2, state='disabled').pack(pady=5, padx=10)
         
        cities = ('Toronto', 'Ottawa', 'Montreal', 'Vancouver', 'St. John')
        cbp3 = ttk.Labelframe(demoPanel, text='Pre-defined List')
        cb3 = ttk.Combobox(cbp3, values=cities, state='readonly')
        cb3.current(1)  # set selection
        cb3.pack(pady=5, padx=10)
 
        # position and display
        cbp1.pack(in_=demoPanel, side=TOP, pady=5, padx=10)
        cbp2.pack(in_=demoPanel, side=TOP, pady=5, padx=10)
        cbp3.pack(in_=demoPanel, side=TOP, pady=5, padx=10)
 
    def _update_values(self, evt):
        # add entered text to combobox list of values
        widget = evt.widget           # get widget
        txt = widget.get()            # get current text
        vals = widget.cget('values')  # get values
         
        if not vals:
            widget.configure(values = (txt, ))
        elif txt not in vals:
            widget.configure(values = vals + (txt, ))
             
        return 'break'  # don't propagate event
 
if __name__ == '__main__':
    ComboBoxDemo().mainloop()