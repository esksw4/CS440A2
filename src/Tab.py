###################################################
# Tabbed interface script
# www.sunjay-varma.com
###################################################

__doc__ = info = '''
# This script was written by Sunjay Varma - www.sunjay-varma.com

# This script has two main classes:
# Tab - Basic tab used by TabBar for main functionality
# TabBar - The tab bar that is placed above tab bodies (Tabs)

# It uses a pretty basic structure:
# root
# -->TabBar(root, init_name) (For switching tabs)
# -->Tab    (Place holder for content)
# 	\t-->content (content of the tab; parent=Tab)
# -->Tab    (Place holder for content)
# 	\t-->content (content of the tab; parent=Tab)
# -->Tab    (Place holder for content)
# 	\t-->content (content of the tab; parent=Tab)
# etc.
# '''

import tkinter
import Functions
from tkinter import *
import tkinter.scrolledtext as tkst
import collections

BASE = RAISED
SELECTED = SUNKEN

# a base tab class
class Tab(Frame):
	def __init__(self, master, name):
		Frame.__init__(self, master)
		self.tab_name = name

# the bulk of the logic is in the actual tab bar
class TabBar(Frame):
	def __init__(self, master=None, init_name=None, testName=None):
		Frame.__init__(self, master)
		# Functions.GUIdisplay.tabs = collections.OrderedDict()
		# self.buttons = {}
		self.current_tab = None
		self.init_name = init_name
		self.testName = testName
		
	
	def show(self):
		#self.pack(side=TOP, expand=YES, fill=X)
		self.grid(sticky='w')
		self.switch_tab(self.init_name or Functions.GUIdisplay.tabs[self.testName].keys()[-1], self.testName)# switch the tab to the first tab
	
	def add(self, tab):
		tab.grid_forget()									# hide the tab on init
		print("add, tab: ", tab)
		print("add, tab.tab_name: ", tab.tab_name)
		print("self.tabs: ", Functions.GUIdisplay.tabs)
		if len(Functions.GUIdisplay.tabs[self.testName]) == 0:
			Functions.GUIdisplay.tabs[self.testName][tab.tab_name] = tab
		else:
			Functions.GUIdisplay.tabs[self.testName].update({tab.tab_name: tab})						# add it to the list of tabs
		# print("tab.tab_name: ", tab.tab_name)
		b = Button(self, text=tab.tab_name, relief=BASE,	# basic button stuff
			command=(lambda name=tab.tab_name: self.switch_tab(name, self.testName)))	# set the command to switch tabs
		b.pack(side=LEFT)												# pack the buttont to the left mose of self

		if tab.tab_name == "Console":
			Functions.GUIdisplay.consoleTab[self.testName] = [Functions.GUIdisplay.consoleTab[self.testName], tkst.ScrolledText(master=Functions.GUIdisplay.tabs[self.testName][tab.tab_name], width=Functions.GUIdisplay.consoleTextWidth, height=Functions.GUIdisplay.consoleTextHeight, wrap=WORD, state=DISABLED)]   # pack the buttont to the left mose of self
			Functions.GUIdisplay.consoleTab[self.testName][1].focus()
			Functions.GUIdisplay.consoleTab[self.testName][1].grid(sticky='w')
			# Functions.GUIdisplay.textConsole_Text.place(x=3, y=1)
		elif tab.tab_name == "Evaluation":
			Functions.GUIdisplay.consoleTab[self.testName] = tkst.ScrolledText(master=Functions.GUIdisplay.tabs[self.testName][tab.tab_name], width=Functions.GUIdisplay.consoleTextWidth, height=Functions.GUIdisplay.consoleTextHeight ,wrap=WORD, state=DISABLED)   # pack the buttont to the left mose of self
			Functions.GUIdisplay.consoleTab[self.testName].focus()
			Functions.GUIdisplay.consoleTab[self.testName].grid(sticky='w')
			# Functions.GUIdisplay.textEvaluation_Text.place(x=3, y=1)

		Functions.GUIdisplay.tabsButtons[self.testName][tab.tab_name] = b									# add it to the list of buttons

	
	def delete(self, tabname):
		if tabname == self.current_tab:
			self.current_tab = None
			Functions.GUIdisplay.tabs[self.testName][tabname].pack_forget()
			del Functions.GUIdisplay.tabs[self.testName][tabname]

			if tabname == "Console":
				Functions.GUIdisplay.consoleTab[self.testName][1].grid_forget()
				del Functions.GUIdisplay.consoleTab[self.testName][1]
			elif tab_name == "Evaluation":
				Functions.GUIdisplay.consoleTab[self.testName][0].grid_forget()
				del Functions.GUIdisplay.consoleTab[self.testName][0]

			self.switch_tab(Functions.GUIdisplay.tabs.keys()[0], self.testName)
		
		else:
			del Functions.GUIdisplay.tabs[self.testName][tabname]
			if tabname == "Console":
				del Functions.GUIdisplay.consoleTab[self.testName][1]
			elif tab_name == "Evaluation":
				del Functions.GUIdisplay.consoleTab[self.testName][0]
		
		Functions.GUIdisplay.tabsButtons[self.testName][tabname].pack_forget()
		del Functions.GUIdisplay.tabsButtons[self.testName][tabname] 
		
	
	def switch_tab(self, name, testName):
		print("\n")
		print("switch_Tab TestName: ", testName)
		print("self.current_tab: ", self.current_tab)
		print("Functions.GUIdisplay.tabs: ", Functions.GUIdisplay.tabs)
		# print("Functions.GUIdisplay.consoleTab: \n", Functions.GUIdisplay.consoleTab)
		if self.current_tab:
			Functions.GUIdisplay.tabsButtons[testName][self.current_tab].config(relief=BASE)
			Functions.GUIdisplay.tabs[testName][self.current_tab].grid_forget()			# hide the current tab
			# self.tabs[self.current_tab].forget()
			if name == "Console":
				Functions.GUIdisplay.consoleTab[testName][1].grid_forget()
			elif name == "Evaluation":
				Functions.GUIdisplay.consoleTab[testName][0].grid_forget()

		# self.tabs[name].pack(side=BOTTOM)							# add the new tab to the display
		print("name: ", name)
		print("Functions.GUIdisplay.tabs[testName][name]: ", Functions.GUIdisplay.tabs[testName][name])
		Functions.GUIdisplay.tabs[testName][name].grid(sticky='w')

		if name == "Console":
			Functions.GUIdisplay.consoleTab[testName][1].grid(sticky='w')
		elif name == "Evaluation":
			Functions.GUIdisplay.consoleTab[testName][0].grid(sticky='w')

		self.current_tab = name									# set the current tab to itself
		
		Functions.GUIdisplay.tabsButtons[testName][name].config(relief=SELECTED)					# set it to the selected style
			
# if __name__ == '__main__':
# 	def write(x):
# 		print(x)
		
# 	root = Tk()
# 	root.title("Tabs")
	
# 	bar = TabBar(root, "Info")
	
# 	tab1 = Tab(root, "Wow...")				# notice how this one's master is the root instead of the bar
# 	Label(tab1, text="Sunjay Varma is an extra ordinary little boy.\n\n\n\n\nCheck out his website:\nwww.sunjay-varma.com", bg="white", fg="red").pack(side=TOP, expand=YES, fill=BOTH)
# 	Button(tab1, text="PRESS ME!", command=(lambda: write("YOU PRESSED ME!"))).pack(side=BOTTOM, fill=BOTH, expand=YES)
# 	Button(tab1, text="KILL THIS TAB", command=(lambda: bar.delete("Wow..."))).pack(side=BOTTOM, fill=BOTH, expand=YES)
	
# 	tab2 = Tab(root, "Hi there!")
# 	Label(tab2, text="How are you??", bg='black', fg='#3366ff').pack(side=TOP, ifll=BOTH, expand=YES)
# 	txt = Text(tab2, width=50, height=20)
# 	txt.focus()
# 	txt.pack(side=LEFT, fill=X, expand=YES)
# 	Button(tab2, text="Get", command=(lambda: write(txt.get('1.0', END).strip()))).pack(side=BOTTOM, expand=YES, fill=BOTH)

# 	tab3 = Tab(root, "Info")
# 	Label(tab3, bg='white', text="This tab was given as an argument to the TabBar constructor.\n\nINFO:\n"+info).pack(side=LEFT, expand=YES, fill=BOTH)
	
# 	bar.add(tab1)                   # add the tabs to the tab bar
# 	bar.add(tab2)
# 	bar.add(tab3)

# 	#bar.config(bd=2, relief=RIDGE)			# add some border
	
# 	bar.show()
	
# 	root.mainloop()
