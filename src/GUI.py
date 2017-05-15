
import re, string, sys
import colorama
import collections
import time as time1

# import Login_Security
# import DashBoardPage
# import HiringStatusPage
# import OrderNewReport
from Order_New_Report import Test_Order1
import Functions
import unittest, time, re
import Tab

import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.simpledialog as dlg

class GUIFunctions:
	# def userInputFieldCheck(typeName):
	# 	if typeName == "OPL":
	# 		if len([v for v in Functions.OPLINfo.values() if v == '']) > 0 or (Functions.GUIdisplay.URL.get() == "empty"):
	# 			# print(Functions.OPLINfo)
	# 			return False
	# 		else:
	# 			# print(Functions.OPLINfo)
	# 			return True

	# 	elif typeName == "orderNewReport":
	# 		if (len([v for v in Functions.orderNewReportResult.values() if v == '']) > 0):
	# 			# print(Functions.orderNewReportResult)
	# 			return False
	# 		else:
	# 			# print(Functions.orderNewReportResult)
	# 			return True
		
	def orderNewReportuserEntryNotValid():
		enterValidFormat = Label(Functions.GUIdisplay.GUIuserInputErrorRow_Frame, text="Please Enter inputs in valid format", fg='red', anchor='w')
		enterValidFormat.pack()

	def orderNewReportErrorMessageCheck(allFieldcheck, typeName, labelText):
		if allFieldcheck == False:
			if typeName == "OPL":
				if Functions.GUIallFieldError == None:
					Functions.GUIallFieldError = Label(Functions.GUIdisplay.GUIOPLErrorRow_Frame, text=labelText, fg='red', anchor='nw')
					Functions.GUIallFieldError.pack(side=TOP)
				else:
					Functions.GUIallFieldError.pack_forget()
					Functions.GUIallFieldError.config(text=labelText)
					Functions.GUIallFieldError.pack(side=TOP)
			elif typeName == "orderNewReport":
				if Functions.GUIallFieldError == None:
					Functions.GUIallFieldError = Label(Functions.GUIdisplay.GUIuserInputErrorRow_Frame, text=labelText, fg='red', bg=Functions.GUIdisplay.background_Color, anchor='nw')
					Functions.GUIallFieldError.pack(side=TOP)
				else:
					Functions.GUIallFieldError.pack_forget()
					Functions.GUIallFieldError.config(text=labelText, bg=Functions.GUIdisplay.background_Color)
					Functions.GUIallFieldError.pack(side=TOP)
		else:
			if typeName == "OPL":
				Functions.GUIdisplay.OPLInfo_Frame.destroy()
				Functions.GUIallFieldError = None
				Functions.GUIdisplay.OPLInfo_Frame.existElement = False
				Functions.GUIdisplay.mainTestingFrame()

			elif typeName == "orderNewReport":
				suite = unittest.TestLoader().loadTestsFromTestCase(Test_Order1.Test_Order1)
				unittest.TextTestRunner(verbosity=2).run(suite)

	def orderNewReportCheckThis():
		Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, "\nPlease Check these following information in the pivotal\n")
		temp = list(Functions.orderNewReportResult.keys())
		for i in temp:
			Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, i + ": " +Functions.orderNewReportResult[i] + "\n")
			Functions.GUIdisplay.textEvaluation_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="green")

	def outputDisplayConsole(text, displayType):
		if displayType == 'e':
			Functions.GUIdisplay.textConsole_Text.insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.textConsole_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textConsole_Text.tag_config("insert", background="white", foreground ="red")
			Functions.GUIdisplay.bar_TabBar.switch_tab("Console")
		else:
			if Functions.GUIdisplay.textEvaluation_Text.get("0.0","100.0") is not '':
				Functions.GUIdisplay.textEvaluation_Text.delete("0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, "  " + text + "\n")
			Functions.GUIdisplay.textEvaluation_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="black")
			GUIFunctions.orderNewReportCheckThis()
			Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	# def buttonPressCheck():
	# 	if Functions.GUIdisplay.current_Button != None:
	# 		print(Functions.GUIdisplay.current_Button)
	# 		if Functions.GUIdisplay.current_Button == "Order New Report":
	# 			Functions.GUIdisplay.orderNewReport_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
	# 			Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
	# 			Functions.GUIdisplay.ONR_GUIconsoleFrame.pack_forget()
	# 			Functions.GUIdisplay.current_Button = None

	# 		elif Functions.GUIdisplay.current_Button == "Hiring Status":
	# 			Functions.GUIdisplay.hiringStatusPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
	# 			Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
	# 			Functions.GUIdisplay.current_Button = None

	# 		elif Functions.GUIdisplay.current_Button == "Login_Security":
	# 			Functions.GUIdisplay.loginSecurity_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
	# 			Functions.GUIdisplay.LS_LL_Frame.pack_forget()
	# 			Functions.GUIdisplay.LS_PR_Frame.pack_forget()
	# 			Functions.GUIdisplay.LS_PU_Frame.pack_forget()
	# 			Functions.GUIdisplay.LS_LL_console_Frame.pack_forget()
	# 			Functions.GUIdisplay.LS_PR_console_Frame.pack_forget()
	# 			Functions.GUIdisplay.LS_PU_console_Frame.pack_forget()
	# 			Functions.GUIdisplay.current_Button = None

	# 		elif Functions.GUIdisplay.current_Button == "Dashboard":
	# 			Functions.GUIdisplay.dashBoardPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
	# 			Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
	# 			Functions.GUIdisplay.current_Button = None

class GUItkinter:
	def __init__(self, Parent):
		self.chooseTestFrame_Width = 100
		self.chooseTestFrame_Height = 450
		self.chooseTestButton_Height = 26
		self.chooseTestPlace_Yaxis = 173
		self.OPLInfoWidth_Width = 22
		self.betweeenFrame = 5

		self.OPLFrame_Dimension = '300x170'
		self.mainFrame_Dimension = '900x425'
		self.LS_Dimension = '875x525'

		self.default_Color = Parent.cget("bg")
		self.background_Color = "White"

		self.URL = StringVar(value="empty")

		self.allFieldError = None
		self.current_Button = None

		self.GUIuserInputErrorRow_Frame = Frame()

		self.bar_TabBar = Tab.TabBar() # For console Tab. -> in conSoleFrame

		self.myParent = Parent
		self.myParent.geometry(self.OPLFrame_Dimension)
		self.myParent.title("Automated Smoke Test")

	# def creatingRadioButton(self, arg, labelText, radioList, valueList, testType):
	# 	if testType == "OPL":
	# 		radioRow_Frame = Frame(arg, width=self.OPLInfoWidth_Width)
	# 		radioRow_Frame.pack(side=TOP, fill=X)
	# 		radioLabel_Label = Label(radioRow_Frame, width=self.OPLInfoWidth_Width -6, text=labelText, anchor='w')
	# 		radioLabel_Label.pack(side=LEFT)

	# 		for radioText,valueText in zip(radioList, valueList):
	# 			radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.URL, value=valueText)
	# 			radioButton_Button.pack(side=LEFT)

	# def includeExtraBlankRow_Frame(self, arg, howMany):
	# 	if (arg.existElement == False):
	#  		for i in range(howMany):
	#  			extraRow_Frame= Frame(arg, bg=self.background_Color)
	#  			extraRow_Frame.pack(side=TOP, fill=X)
	#  			extraRow_Label = Label(extraRow_Frame, bg=self.background_Color, text=" ")
	#  			extraRow_Label.pack(side=LEFT, fill=X)

	# def includeTitle_Frame(self, arg, txt, fontSize):
	# 	if (arg.existElement == False):
	# 		title_Frame = tkinter.Frame(arg, bg=self.background_Color)
	# 		title_Frame.pack(side=TOP, fill=X)
	# 		title_Label = tkinter.Label(title_Frame, bg=self.background_Color, text=txt, font=(fontSize))
	# 		title_Label.pack(side=LEFT, fill=X)

	def OPLInfoFrame(self):
		## Displaying OPL information.

		self.OPLInfoLabelName = ["Email Address", "Email Password", "Portal Username", "Portal Password"]
		self.OPLINfoEntry = []
		self.OPLInfo_Frame = Frame(self.myParent)
		self.OPLInfo_Frame.pack()
		self.OPLInfo_Frame.existElement = True

		self.TestInfo_Label = Label(self.OPLInfo_Frame, text="Test Information: ")
		self.TestInfo_Label.pack()

		self.GUIOPLErrorRow_Frame = tkinter.Frame(self.OPLInfo_Frame)#, bg=self.background_Color)
		self.GUIOPLErrorRow_Frame.pack(side=TOP, fill=X)

		self.creatingRadioButton(self.OPLInfo_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"], "OPL")

		for info in self.OPLInfoLabelName:
			self.Row_Frame = tkinter.Frame(self.OPLInfo_Frame, width=self.OPLInfoWidth_Width)
			self.Label_Label = tkinter.Label(self.Row_Frame, width=self.OPLInfoWidth_Width - 7, text=info, anchor='w')#, bg=self.background_Color)
			self.Entry_Entry = tkinter.Entry(self.Row_Frame, width=self.OPLInfoWidth_Width + 7)
			self.Row_Frame.pack(side=TOP, fill=X)
			self.Label_Label.pack(side=LEFT)
			self.Entry_Entry.pack(side=RIGHT, expand=YES, fill=X)
			self.OPLINfoEntry.append(self.Entry_Entry)

		self.OPLINfoLabelSave_Button = tkinter.Button(self.OPLInfo_Frame, text="Continue", command=self.getUserInputSendFunction)#, bg=self.default_Color)
		self.OPLINfoLabelSave_Button.pack(side=RIGHT)

	def mainTestingFrame(self):
		# self.myParent.geometry(self.mainFrame_Dimension)

		# self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width, height=self.chooseTestFrame_Height, bg=self.default_Color)
		# self.chooseTest_Frame.pack(side=LEFT, fill=Y)
		# self.chooseTest_Frame.existElement = True

		# self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text="Login_Security", command=self.loginSecurity, bg=self.default_Color)
		# self.loginSecurity_Button.pack()
		# self.loginSecurity_Button.place(y=self.chooseTestPlace_Yaxis, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		self.LS_LL_Frame = tkinter.Frame(self.myParent)
		self.LS_LL_Frame.existElement = False
		self.LS_LL_console_Frame = tkinter.Frame(self.LS_LL_Frame)
		self.LS_LL_console_Frame.existElement = False

		self.LS_PR_Frame = tkinter.Frame(self.myParent)
		self.LS_PR_Frame.existElement = False
		self.LS_PR_console_Frame = tkinter.Frame(self.LS_PR_Frame)
		self.LS_PR_console_Frame.existElement = False

		self.LS_PU_Frame = tkinter.Frame(self.myParent)
		self.LS_PU_Frame.existElement = False
		self.LS_PU_console_Frame = tkinter.Frame(self.LS_PU_Frame)
		self.LS_PU_console_Frame.existElement = False

		# self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text="Dashboard", command =self.dashBoard, bg=self.default_Color)
		# self.dashBoardPage_Button.pack()
		# self.dashBoardPage_Button.place(y=self.chooseTestPlace_Yaxis+self.chooseTestButton_Height, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text="Hiring Status", command = self.hiringStatus, bg=self.default_Color)
		# self.hiringStatusPage_Button.pack()
		# self.hiringStatusPage_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*2), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text="Order New Report", relief=RAISED, command = self.ordernewReport, bg=self.default_Color)
		# self.orderNewReport_Button.pack()
		# self.orderNewReport_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*3), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.User_Input_Frame_Frame = tkinter.Frame(self.myParent)
		# self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame)
		# self.OPL_Input_Frame_Frame.existElement = False

		# self.ONR_GUIconsoleFrame = tkinter.Frame(self.myParent)
		# self.ONR_GUIconsoleFrame.existElement = False

	# def getUserInputSendFunction(self):
	# 	if Functions.GUIallFieldError != None:
	# 		Functions.GUIallFieldError.pack_forget()

	# 	dictValue = []

	# 	if self.OPLInfo_Frame.existElement:
	# 		for f in self.OPLINfoEntry:
	# 			dictValue.append(f.get())

	# 		Functions.OPLINfo = collections.OrderedDict(zip(self.OPLInfoLabelName, dictValue))
	# 		# print(Functions.OPLINfo['URL to test'])
	# 		allFieldCheck = GUIFunctions.userInputFieldCheck("OPL")
	# 		GUIFunctions.orderNewReportErrorMessageCheck(allFieldCheck,"OPL", "Please Enter all fields")

	# 	elif self.chooseTest_Frame.existElement:
	# 		for f in self.fields:
	# 			dictValue.append(f.get())

	# 		Functions.orderNewReportResult = collections.OrderedDict(zip(self.whichInfo, dictValue))
	# 		allFieldCheck = GUIFunctions.userInputFieldCheck("orderNewReport")
	# 		GUIFunctions.orderNewReportErrorMessageCheck(allFieldCheck,"orderNewReport", "Please Enter all fields")

	# used in "userInputFrame"
	# def makeUserInputForm(self, arg, testType):
		# if testType == "LS":
		# 	anchorAs = SW
		# 	self.userInputWidth_Width = 16

		# elif testType == "ONR":
		# 	self.userInputWidth_Width = 23
		# 	anchorAs = 'center'

		# self.fields = []
		# for entry in self.whichInfo:	
		# 	userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
		# 	userInputLabel_Label = tkinter.Label(userInputRow_Frame, width=self.userInputWidth_Width, text=entry, anchor=anchorAs, bg=self.background_Color)
		# 	userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
		# 	userInputRow_Frame.pack(side=TOP, fill=X)
		# 	userInputLabel_Label.pack(side=LEFT)
		# 	userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
		# 	self.fields.append(userInputEntry_Entry)

	# def userInputFrame(self, arg, testType):
	# 	print("arg: ", arg)
	# 	print("arg.existElement: ",arg.existElement)

	# 	arg.config(bg=self.background_Color)

	# 	if self.background_Color == "light goldenrod yellow": 
	# 		arg.pack(side=LEFT, fill=Y, padx=self.betweeenFrame, expand=0)
	# 	else:
	# 		arg.pack(side=LEFT, fill=X, padx=self.betweeenFrame)

	# 	if (arg.existElement == False):
	# 		self.GUIuserInputErrorRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
	# 		self.GUIuserInputErrorRow_Frame.pack(side=TOP, fill=X)

	# 		self.makeUserInputForm(arg, testType)

	# 		arg.existElement = True

	# 		if len(self.whichInfo):
	# 			userInputEnterRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
	# 			userInputEnterRow_Frame.pack(side=TOP, fill=X)
	# 			userInputEnterButton_Button = tkinter.Button(userInputEnterRow_Frame, text="Enter", command =self.getUserInputSendFunction)
	# 			userInputEnterButton_Button.pack(side=RIGHT)

	# def conSoleFrame(self, arg, testType):
	# 	print("arg: ", arg)
	# 	print("arg.existElement: ",arg.existElement)

	# 	if testType == "LS":
	# 		self.consoleTextWidth = 28
	# 		whichSide = RIGHT
	# 	else: 
	# 		self.consoleTextWidth = 90
	# 		whichSide = LEFT
		
	# 	arg.config(bg=self.background_Color)
	# 	arg.pack(side=whichSide, fill=BOTH, padx=self.betweeenFrame, pady=5)

	# 	if (arg.existElement == False):
	# 		self.bar_TabBar = Tab.TabBar(arg, "Evaluation")
	# 		tab1_Tab = Tab.Tab(arg, "Evaluation")
	# 		tab2_Tab = Tab.Tab(arg, "Console")
	# 		self.bar_TabBar.add(tab1_Tab)
	# 		self.bar_TabBar.add(tab2_Tab)
	# 		self.bar_TabBar.show()
	# 		arg.existElement = True

	def loginSecurity(self):
		self.myParent.geometry(self.LS_Dimension)
		self.background_Color = "light goldenrod yellow"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Login_Security"
		self.myParent.config(bg=self.background_Color)

		self.loginSecurity_Button.config(bg=self.background_Color, relief=FLAT)

		self.includeTitle_Frame(self.LS_LL_Frame, "Login and Logout", 20)
		self.includeExtraBlankRow_Frame(self.LS_LL_Frame, 3)
		
		self.whichInfo = []
		self.userInputFrame(self.LS_LL_Frame, "LS")
		self.conSoleFrame(self.LS_LL_console_Frame, "LS")

		self.includeTitle_Frame(self.LS_PR_Frame, "Password Recovery", 20)
		
		self.whichInfo = ["Email Address:\n password recovery"]
		self.userInputFrame(self.LS_PR_Frame, "LS")
		self.conSoleFrame(self.LS_PR_console_Frame, "LS")

		self.includeTitle_Frame(self.LS_PU_Frame, "Password Unlock", 20)
		
		self.whichInfo = ["Email address:\n password unlock"]
		self.userInputFrame(self.LS_PU_Frame, "LS")
		self.conSoleFrame(self.LS_PU_console_Frame, "LS")

		suite = unittest.TestLoader().loadTestsFromTestCase(Login_Security.Login_Security)
		unittest.TextTestRunner(verbosity=2).run(suite)
		
	def dashBoard(self):
		GUIFunctions.buttonPressCheck()
		self.background_Color = "peach puff"
		self.current_Button = "Dashboard"
		self.myParent.config(bg=self.background_Color)
		self.dashBoardPage_Button.config(bg=self.background_Color, relief=FLAT)

		suite = unittest.TestLoader().loadTestsFromTestCase(DashBoardPage.DashBoardPage)
		unittest.TextTestRunner(verbosity=2).run(suite)

	def hiringStatus(self):
		GUIFunctions.buttonPressCheck()
		self.background_Color = "misty rose"
		self.current_Button = "Hiring Status"
		self.myParent.config(bg=self.background_Color)
		self.hiringStatusPage_Button.config(bg=self.background_Color, relief=FLAT)

		suite = unittest.TestLoader().loadTestsFromTestCase(HiringStatusPage.HiringStatusPage)
		unittest.TextTestRunner(verbosity=2).run(suite)

	def ordernewReport(self):
		self.myParent.geometry(self.mainFrame_Dimension)
		self.background_Color = "lavender"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Order New Report"
		self.myParent.config(bg=self.background_Color)
		self.orderNewReport_Button.config(bg=self.background_Color, relief=FLAT)
		
		
		self.whichInfo = ["First Name","Last Name", "Email Address", "Job Title", "PO Box", "Cost Center", "Color", "Position Number", "Favorite Number", "Message to Consultant", "Message to Assessee", "Also Notify", "New Tag Name"]
		self.userInputFrame(self.User_Input_Frame_Frame, "ONR")
		self.conSoleFrame(self.ONR_GUIconsoleFrame, "ONR")
		self.whichInfo = []

if Functions.GUImainFrame == None:
	Functions.GUImainFrame = Tk()
	Functions.GUIdisplay = GUItkinter(Functions.GUImainFrame)
	Functions.GUImainFrame.mainloop()

	# def messageBox(self):
	# 	msgBox = Tk()
	# 	msgBox.geometry('150x150')
	# 	label = Label(msgBox, text="Please enter valid email/password:")
	# 	label.pack()
	# 	msgBox.mainloop()
######################################tkinter background color chart
# http://cs.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

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
# 	inputs = makeUserInputForm(inputFrame)

# 	global text
# 	text = []

# 	global enterButton, enterRow
# 	enterRow = Frame(inputFrame)
# 	enterRow.pack(side=TOP, fill=X)
# 	Functions.toDisplayAssesseeFillInError = enterRow
# 	enterButton = Button(enterRow, text="Enter", command=getUserInputSendFunction)
# 	enterButton.pack(side=RIGHT)

# def makeUserInputForm(root):
# 	fields = []
# 	for entry in self.whichInfo:
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

# 	result = dict(zip(self.whichInfo, text))
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
# 	
# 	self.whichInfo = ['First Name','Last Name', 'Email Address', 'PO Box', 'Cost Center', 'Color', 'Position Number', 'Favorite Number', 'Message to Consultant', 'Message to Assessee']

# 	eachFrame()


################ How to embed a terminal in a Tkinter application?
# http://stackoverflow.com/questions/7253448/how-to-embed-a-terminal-in-a-tkinter-application


################ Console in the TkinterFrame
# http://tkinter.unpythonic.net/wiki/CmdTk

################ combination of Grid and Pack
# http://stackoverflow.com/questions/11257771/combining-grid-pack-tkinter
