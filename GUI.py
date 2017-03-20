# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
import re, string, sys
import colorama
import time as time1

# simport Login_Security
# import DashBoardPage
# import HiringStatusPage
import OrderNewReport
import Functions
import unittest, time, re
# import webbrowser

import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.simpledialog as dlg


# global toDisplayAssesseeFillInError

# global top, inputFrame
# global allFieldError 
# global text, whichInfo
# global enterButton

# toDisplayAssesseeFillInError = []
# result = {}


class GUIFunctions:
	def orderNewReportuserInputFieldCheck():
		if len([v for v in Functions.orderNewReportResult.values() if v == '']) > 0:
			print(Functions.orderNewReportResult)
			return False
		else:
			print(Functions.orderNewReportResult)
			return True
		
	def orderNewReportuserEntryNotValid():
		# unittest.TextTestRunner(verbosity=2).stop(suite)
		enterValidFormat = Label(Functions.GUIuserInputErrorRow_Frame, text="Please Enter inputs in valid format", fg='red', anchor='w')
		enterValidFormat.pack()


	def orderNewReportErrorMessageCheck(allFieldcheck, labelText):
		if allFieldcheck == False:
			if Functions.GUIallFieldError == None:
				Functions.GUIallFieldError = Label(Functions.GUIuserInputErrorRow_Frame, text=labelText, fg='red', anchor='nw')
				Functions.GUIallFieldError.pack(side=TOP)
			else:
				Functions.GUIallFieldError.pack_forget()
				Functions.GUIallFieldError.pack(side=TOP)
		else:
			suite = unittest.TestLoader().loadTestsFromTestCase(OrderNewReport.OrderNewReport)
			unittest.TextTestRunner(verbosity=2).run(suite) 

class GUItkinter:
	#global whichInfo
	def __init__(self, Parent):
		self.allFieldError = None
		self.myParent = Parent
		self.myParent.geometry('450x500')
		self.myParent.title('Automated QA Testing')

		self.chooseTest_Frame = Frame(Parent)
		self.chooseTest_Frame.pack(side=LEFT)

		self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text='Login_Security', command = self.loginSecurity).pack()
		self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text='Dashboard', command = self.dashBoard).pack()
		self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text='Hiring Status', command = self.hiringStatus).pack()
		self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text='Order New Report', command = self.ordernewReport).pack()

		self.userInput_Frame = tkinter.Frame(Parent)
		self.userInput_Frame.pack(side=LEFT, fill=X)
		self.userInput_Frame.existElement = False

	def loginSecurity(self):
		suite = unittest.TestLoader().loadTestsFromTestCase(Login_Security.Login_Security)
		unittest.TextTestRunner(verbosity=2).run(suite)
		
	def dashBoard(self):
		suite = unittest.TestLoader().loadTestsFromTestCase(DashBoardPage.DashBoardPage)
		unittest.TextTestRunner(verbosity=2).run(suite)

	def hiringStatus(self):
		suite = unittest.TestLoader().loadTestsFromTestCase(HiringStatusPage.HiringStatusPage)
		unittest.TextTestRunner(verbosity=2).run(suite)

	def makeForm(self):
		global fields
		fields = []

		for entry in whichInfo:	
			self.userInputRow_Frame = tkinter.Frame(self.userInput_Frame)
			self.userInputLabel_Label = tkinter.Label(self.userInputRow_Frame, width=20, text=entry, anchor='center')
			self.userInputEntry_Entry = tkinter.Entry(self.userInputRow_Frame)
			self.userInputRow_Frame.pack(side=TOP, fill=X)
			self.userInputLabel_Label.pack(side=LEFT)
			self.userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
			fields.append(self.userInputEntry_Entry)

	def getUserInputSendFunction(self):
		dictValue = []

		for f in fields:
			dictValue.append(f.get())

		Functions.orderNewReportResult = dict(zip(whichInfo, dictValue))
		Functions.orderNewReportResult['Also Notify'] = 'Young Kim'

		allFieldCheck = GUIFunctions.orderNewReportuserInputFieldCheck()
		GUIFunctions.orderNewReportErrorMessageCheck(allFieldCheck, "Please Enter all fields")

	def eachFrame(self):
		if (self.userInput_Frame.existElement == True):
			self.userInput_Frame.destroy()
			self.userInput_Frame = tkinter.Frame(self.Parent)
			self.userInput_Frame.pack(side=LEFT, fill=X)


		Functions.GUIuserInputErrorRow_Frame = tkinter.Frame(self.userInput_Frame)
		Functions.GUIuserInputErrorRow_Frame.pack(side=TOP, fil=X)
		self.makeForm()
		self.userInputEnterRow_Frame = tkinter.Frame(self.userInput_Frame)
		self.userInputEnterRow_Frame.pack(side=TOP, fill=X)
		self.userInputEnterButton_Button = tkinter.Button(self.userInputEnterRow_Frame, text="Enter", command =self.getUserInputSendFunction)
		self.userInputEnterButton_Button.pack(side=RIGHT)

	def ordernewReport(self):
		global whichInfo

		whichInfo = ['First Name','Last Name', 'Email Address', 'PO Box', 'Cost Center', 'Color', 'Position Number', 'Favorite Number', 'Message to Consultant', 'Message to Assessee']
		self.eachFrame()

if Functions.GUImainFrame == None:
	Functions.GUImainFrame = Tk()
	gui = GUItkinter(Functions.GUImainFrame)
	Functions.GUImainFrame.mainloop()





# def eachFrame():
# 	if inputFrame == None: # if there is no initial inputFrame, initializer the frame
# 		global inputFrame
# 		inputFrame = Frame(top)
# 	else:  # if there IS inital inputFrame, then remove previous one and create new one
# 		inputFrame.destroy()
# 		inputFrame = Frame(top)

# 	global allFieldError # To check If Error Message is existing: Label that shows Error message everytime "ENter" is pressed and there are fields that are blank
# 	allFieldError = None

# 	inputFrame.pack(side=LEFT, fill='x')

# 	global inputs
# 	inputs = makeForm(inputFrame)

# 	global text
# 	text = []

# 	global enterButton, enterRow
# 	enterRow = Frame(inputFrame)
# 	enterRow.pack(side=TOP, fill=X)
# 	Functions.toDisplayAssesseeFillInError = enterRow
# 	enterButton = Button(enterRow, text="Enter", command=getUserInputSendFunction)
# 	enterButton.pack(side=RIGHT)

# def makeForm(root):
# 	fields = []
# 	for entry in whichInfo:
# 		row = Frame(root)
# 		lab = Label(row, width=20, text=entry, anchor='center')
# 		ent = Entry(row)
# 		row.pack(side=TOP, fill=X)
# 		lab.pack(side=LEFT)
# 		ent.pack(side=RIGHT, expand=YES, fill=X)
# 		fields.append(ent)
# 	return fields

# def getUserInputSendFunction(*args):
# 	text = []
# 	for i in inputs:
# 		text.append(i.get())

# 	result = dict(zip(whichInfo, text))
# 	result['Also Notify'] = 'Young Kim'
# 	# print("inGUItkinter: ", enterRow)
	
# 	allFieldCheck = Functions.orderNewReportuserInputAssign()
# 	# print("allFieldCheck: " , allFieldCheck)
# 	if  allFieldCheck == False:
# 		#print("AllFieldError: " ,allFieldError)
# 		if allFieldError == None:
# 			allFieldError = Label(enterRow, text="Please Enter all fields", fg='red', anchor='nw')
# 			allFieldError.pack(side=TOP)
# 		else:
# 			allFieldError.pack_forget()
# 			allFieldError.pack(side=TOP)
# 	else:
# 		suite = unittest.TestLoader().loadTestsFromTestCase(OrderNewReport.OrderNewReport)
# 		unittest.TextTestRunner(verbosity=2).run(suite)

# def loginSecurity():
# 	suite = unittest.TestLoader().loadTestsFromTestCase(Login_Security.Login_Security)
# 	unittest.TextTestRunner(verbosity=2).run(suite)
	
# def dashBoard():
# 	suite = unittest.TestLoader().loadTestsFromTestCase(DashBoardPage.DashBoardPage)
# 	unittest.TextTestRunner(verbosity=2).run(suite)

# def hiringStatus():
# 	suite = unittest.TestLoader().loadTestsFromTestCase(HiringStatusPage.HiringStatusPage)
# 	unittest.TextTestRunner(verbosity=2).run(suite)

# def ordernewReport():
# 	global whichInfo
# 	whichInfo = ['First Name','Last Name', 'Email Address', 'PO Box', 'Cost Center', 'Color', 'Position Number', 'Favorite Number', 'Message to Consultant', 'Message to Assessee']

# 	eachFrame()



