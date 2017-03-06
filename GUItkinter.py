import Login_Security
import DashBoardPage
import HiringStatusPage
import OrderNewReport
import Functions
import unittest, time, re
import webbrowser

from tkinter import *
import tkinter
import tkinter.messagebox as msg
import tkinter.simpledialog as dlg

global top

def mainTab():
	main = Frame()
	main.pack(side = LEFT)
	login_Security = tkinter.Button(main, text='Login_Security', command = loginSecurity).pack()
	# db = OnButtonClick()
	dashBoard_Page = tkinter.Button(main, text='Dashboard', command = dashBoard).pack()
	hiringStatus_Page = tkinter.Button(main, text='Hiring Status', command = hiringStatus).pack()
	order_newReport = tkinter.Button(main, text='Order New Report', command = ordernewReport).pack()

def eachFrame():
	txtConsole = Text(master=top, height=10, width=40, background ='black', fg='white')
	#txtConsole.pack(side=LEFT)

	txtConsoleScrollBar = Scrollbar(top, command=txtConsole.xview)
	txtConsole.config(yscrollcommand=txtConsoleScrollBar.set)


	txtConsole.pack(side=LEFT)
	txtConsoleScrollBar.pack(side=RIGHT)
	

	#txtConsoleScrollBar.config(command=txtConsole.yview)

def makeForm(root, entries):
	fields = []
	for entry in entries:
		row = Frame(root)
		lab = Label(row, width=20, text=entry, anchor='center')
		ent = Entry(row)
		row.pack(side=TOP, fill=X)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		fields.append(ent)
	return fields

def getUserInputSendFunction(asdf):
	text = []
	for i in asdf:
		text.append(i.get())
	checkEmpty = Functions.Functions.userInputAssign(text)
	while checkEmpty == True:
		inputs = makeForm(inputFrame, whichInfo)
		top.bind('<Return>', (lambda event, e=inputs: getUserInputSendFunction(e)))


def loginSecurity():
	suite = unittest.TestLoader().loadTestsFromTestCase(Login_Security.Login_Security)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
def dashBoard():
	# if button_id == 2:
	suite = unittest.TestLoader().loadTestsFromTestCase(DashBoardPage.DashBoardPage)
	unittest.TextTestRunner(verbosity=2).run(suite)

def hiringStatus():
	suite = unittest.TestLoader().loadTestsFromTestCase(HiringStatusPage.HiringStatusPage)
	unittest.TextTestRunner(verbosity=2).run(suite)
	# else:
	# 	pass

def ordernewReport():
	inputFrame = Frame()
	inputFrame.pack(side=LEFT)

	global whichInfo
	whichInfo = ['First Name','Last Name', 'Email Address', 'PO Box', 'Cost Center', 'Color', 'Position Number', 'Favorite Number', 'Mewwage to Consultant', 'Message to Assessee', ]

	inputs = makeForm(inputFrame, whichInfo)
	top.bind('<Return>', (lambda event, e=inputs: getUserInputSendFunction(e)))

	suite = unittest.TestLoader().loadTestsFromTestCase(OrderNewReport.OrderNewReport)
	unittest.TextTestRunner(verbosity=2).run(suite)




top = Tk()

# ls = OnButtonClick(1)
top.geometry('450x500')
top.title('Automated QA Testing')

mainTab()


top.mainloop()