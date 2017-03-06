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

def eachFrame(whichInfo):
	# txtConsole = Text(master=top, height=10, width=40, background ='black', fg='white')
	# #txtConsole.pack(side=LEFT)

	# txtConsoleScrollBar = Scrollbar(top, command=txtConsole.xview)
	# txtConsole.config(yscrollcommand=txtConsoleScrollBar.set)


	# txtConsole.pack(side=LEFT)
	# txtConsoleScrollBar.pack(side=RIGHT)
	
	#txtConsoleScrollBar.config(command=txtConsole.yview)
	global inputFrame
	inputFrame = Frame()
	inputFrame.pack(side=LEFT)

	global inputs
	inputs = makeForm(inputFrame, whichInfo)
	# inputFrame.bind('<Return>', getUserInputSendFunction)
	b = Button (inputFrame, text="Enter", command=getUserInputSendFunction)
	b.pack(side=RIGHT)

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

# def userInfo(inputFrame, whichInfo):
# 	checkEmpty = True
# 	print(checkEmpty)
# 	checkEmpty = Functions.Functions.userInputAssign(text)
# 	# while checkEmpty == True:
# 	# 	inputs = makeForm(inputFrame, whichInfo)
# 	# 	top.bind('<Return>', getUserInputSendFunction(inputs))
# 	# 	print(text)
# 	# 	checkEmpty = Functions.Functions.userInputAssign(text)
		
#################################################FIX HERE
def getUserInputSendFunction(*args):
	text = []
	for i in inputs:
		text.append(i.get())
	if (Functions.Functions.userInputAssign(text) == False): # and (allFieldError.winfo_exists() == 0): # if input is not empty
			allFieldError = Label(inputFrame, text="Please Enter all fields", fg='red', anchor='nw').pack(side=TOP)
			allFieldError.destroy()
	else:
		print("idk")



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

def ordernewReport():
	whichInfo = ['First Name','Last Name', 'Email Address', 'PO Box', 'Cost Center', 'Color', 'Position Number', 'Favorite Number', 'Mewwage to Consultant', 'Message to Assessee', ]

	eachFrame(whichInfo)

	print("whatever")
	# suite = unittest.TestLoader().loadTestsFromTestCase(OrderNewReport)
	# unittest.TextTestRunner(verbosity=2).run(suite)




top = Tk()

# ls = OnButtonClick(1)
top.geometry('450x500')
top.title('Automated QA Testing')

mainTab()


top.mainloop()