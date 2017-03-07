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
global allFieldError, inputFrame 
global text, whichInfo

def mainTab():
	main = Frame(top)
	main.pack(side = LEFT)
	login_Security = tkinter.Button(main, text='Login_Security', command = loginSecurity).pack()
	# db = OnButtonClick()
	dashBoard_Page = tkinter.Button(main, text='Dashboard', command = dashBoard).pack()
	hiringStatus_Page = tkinter.Button(main, text='Hiring Status', command = hiringStatus).pack()
	order_newReport = tkinter.Button(main, text='Order New Report', command = ordernewReport).pack()

def eachFrame():
	if inputFrame == None: # if there is no initial inputFrame, initializer the frame
		global inputFrame
		inputFrame = Frame(top)
	else:  # if there IS inital inputFrame, then remove previous one and create new one
		inputFrame.destroy()
		inputFrame = Frame(top)

	global allFieldError # To check If Error Message is existing: Label that shows Error message everytime "ENter" is pressed and there are fields that are blank
	allFieldError = None

	inputFrame.pack(side=LEFT)

	global inputs
	inputs = makeForm(inputFrame)

	global text
	text = []

	global b
	b = Button(inputFrame, text="Enter", command=getUserInputSendFunction)
	b.pack(side=RIGHT)

def makeForm(root):
	fields = []
	for entry in whichInfo:
		row = Frame(root)
		lab = Label(row, width=20, text=entry, anchor='center')
		ent = Entry(row)
		row.pack(side=TOP, fill=X)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		fields.append(ent)
	return fields

def getUserInputSendFunction(*args):
	text = []
	for i in inputs:
		text.append(i.get())
	print("getUserInputSendFUnction", text)
	if (Functions.Functions.userInputAssign(whichInfo, text) == False): # and (allFieldError.winfo_exists() == 0): # if input is not empty
		print(allFieldError)
		if allFieldError == None:
			global allFieldError
			allFieldError = Label(inputFrame, text="Please Enter all fields", fg='red', anchor='nw')
			allFieldError.pack(side=TOP)
		else:
			allFieldError.pack_forget()
			allFieldError.pack(side=TOP)
	else:
		suite = unittest.TestLoader().loadTestsFromTestCase(OrderNewReport.OrderNewReport)
		unittest.TextTestRunner(verbosity=2).run(suite)


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
	global whichInfo
	whichInfo = ['First Name','Last Name', 'Email Address', 'PO Box', 'Cost Center', 'Color', 'Position Number', 'Favorite Number', 'Message to Consultant', 'Message to Assessee']



	eachFrame()
	if Functions.Functions.userInputAssign(whichInfo, text) == True:
		print("whatever")
		print(text)





top = Tk()

# ls = OnButtonClick(1)
top.geometry('450x500')
top.title('Automated QA Testing')

global inputFrame
inputFrame = None

mainTab()


top.mainloop()



########################SCROLL BAR
# txtConsole = Text(master=top, height=10, width=40, background ='black', fg='white')
# #txtConsole.pack(side=LEFT)

# txtConsoleScrollBar = Scrollbar(top, command=txtConsole.xview)
# txtConsole.config(yscrollcommand=txtConsoleScrollBar.set)


# txtConsole.pack(side=LEFT)
# txtConsoleScrollBar.pack(side=RIGHT)

#txtConsoleScrollBar.config(command=txtConsole.yview)

########################def userInfo(inputFrame, whichInfo):
# 	checkEmpty = True
# 	print(checkEmpty)
# 	checkEmpty = Functions.Functions.userInputAssign(text)
# 	# while checkEmpty == True:
# 	# 	inputs = makeForm(inputFrame, whichInfo)
# 	# 	top.bind('<Return>', getUserInputSendFunction(inputs))
# 	# 	print(text)
# 	# 	checkEmpty = Functions.Functions.userInputAssign(text)
		

