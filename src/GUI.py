
import re, string, sys
import colorama
import collections
import time as time1

# simport Login_Security
# import DashBoardPage
# import HiringStatusPage
import OrderNewReport
import Functions
import unittest, time, re
import Tab


import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.simpledialog as dlg

class GUIFunctions:
	# def askUserOPLInfo():

	def orderNewReportuserInputFieldCheck():
		if len([v for v in Functions.orderNewReportResult.values() if v == '']) > 0:
			print(Functions.orderNewReportResult)
			return False
		else:
			print(Functions.orderNewReportResult)
			return True
		
	def orderNewReportuserEntryNotValid():
		# unittest.TextTestRunner(verbosity=2).stop(suite)
		enterValidFormat = Label(Functions.GUIdisplay.GUIuserInputErrorRow_Frame, text="Please Enter inputs in valid format", fg='red', anchor='w')
		enterValidFormat.pack()

	def orderNewReportErrorMessageCheck(allFieldcheck, labelText):
		if allFieldcheck == False:
			if Functions.GUIallFieldError == None:
				Functions.GUIallFieldError = Label(Functions.GUIdisplay.GUIuserInputErrorRow_Frame, text=labelText, fg='red', bg=Functions.GUIdisplay.background_Color, anchor='nw')
				Functions.GUIallFieldError.pack(side=TOP)
			else:
				Functions.GUIallFieldError.pack_forget()
				Functions.GUIallFieldError.config(text=labelText, bg=Functions.GUIdisplay.background_Color)
				Functions.GUIallFieldError.pack(side=TOP)
		else:
			suite = unittest.TestLoader().loadTestsFromTestCase(OrderNewReport.OrderNewReport)
			unittest.TextTestRunner(verbosity=2).run(suite)

	def orderNewReportCheckThis():
		Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, "\n Please Check these following information in the pivotal")
		temp = list(Functions.orderNewReportResult.keys())
		for i in temp:
			Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, i + ": " +Functions.orderNewReportResult[i] + "\n")
			Functions.GUIdisplay.textEvaluation_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="black")

	def outputDisplayConsole(text, displayType):
		if displayType == 'e': # 'e' == console
			print(Functions.GUIdisplay.textConsole_Text.get("0.0","100.0"))
			# if Tab.TabBar.txtBox[Console].get("0.0","2.0") is not '':
			# 	Functions.GUIdisplay.tex.delete("0.0", "2.0")
			Functions.GUIdisplay.textConsole_Text.insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.textConsole_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textConsole_Text.tag_config("insert", background="white", foreground ="red")
			Functions.GUIdisplay.bar_TabBar.switch_tab("Console")
		else:
			print(Functions.GUIdisplay.textEvaluation_Text.get("0.0","100.0"))
			if Functions.GUIdisplay.textEvaluation_Text.get("0.0","100.0") is not '':
				Functions.GUIdisplay.textEvaluation_Text.delete("0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, "  " + text + "\n")
			Functions.GUIdisplay.textEvaluation_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="black")
			GUIFunctions.orderNewReportCheckThis()
			Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	def buttonPressCheck():
		print(Functions.GUIdisplay.current_Button)
		print(Functions.GUIdisplay.background_Color)
		if Functions.GUIdisplay.current_Button != None:
			if Functions.GUIdisplay.current_Button == 'Order New Report':
				Functions.GUIdisplay.orderNewReport_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				# Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.GUIuserInput_Frame.pack_forget()
				Functions.GUIdisplay.GUIconsoleFrame.pack_forget()
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == 'Hiring Status':
				Functions.GUIdisplay.hiringStatusPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				# Functions.GUIdisplay.GUIuserInput_Frame.pack_forget()#config(bg=Functions.GUIdisplay.default_Color)
				# # Functions.GUIdisplay.userInputLabel_Label.config(bg=Functions.GUIdisplay.default_Color)
				# # Functions.GUIdisplay.userInputEnterRow_Frame.config(bg=Functions.GUIdisplay.default_Color)
				# Functions.GUIdisplay.GUIconsoleFrame.pack_forget()#config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == 'Login_Security':
				Functions.GUIdisplay.loginSecurity_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				# Functions.GUIdisplay.GUIuserInput_Frame.pack_forget()#config(bg=Functions.GUIdisplay.default_Color)
				# # Functions.GUIdisplay.userInputLabel_Label.config(bg=Functions.GUIdisplay.default_Color)
				# # Functions.GUIdisplay.userInputEnterRow_Frame.config(bg=Functions.GUIdisplay.default_Color)
				# Functions.GUIdisplay.GUIconsoleFrame.pack_forget()#config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == 'Dashboard':
				Functions.GUIdisplay.dashBoardPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				# Functions.GUIdisplay.GUIuserInput_Frame.pack_forget()#config(bg=Functions.GUIdisplay.default_Color)
				# # Functions.GUIdisplay.userInputLabel_Label.config(bg=Functions.GUIdisplay.default_Color)
				# # Functions.GUIdisplay.userInputEnterRow_Frame.config(bg=Functions.GUIdisplay.default_Color)
				# Functions.GUIdisplay.GUIconsoleFrame.pack_forget()#config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None

class GUItkinter:
	#global whichInfo
	def __init__(self, Parent):
		self.chooseTestFrame_Width = 100
		self.chooseTestFrame_Height = 450
		self.chooseTestButton_Height = 26
		self.chooseTestPlace_Yaxis = 173
		self.userInputWidth = 23
		self.consoleWidth = 60
		self.consoleTextWidth = 55
		self.betweeenFrame = 5

		Functions.GUIOPLFrame = Tk

		self.default_Color = Parent.cget('bg')
		self.background_Color = 'White'

		self.allFieldError = None
		self.current_Button = None

		self.myParent = Parent
		self.myParent.geometry('200x125')
		self.myParent.title('Automated QA Testing')

		self.OPLInfoLabelName = ['Url to test', 'Portal Username', 'Portal Password']
		self.OPLINfoEntry = []
		self.askUserOPLInfo_Frame = Frame(self.myParent)
		self.askUserOPLInfo_Frame.pack()
		self.TestInfo_Label = Label(self.askUserOPLInfo_Frame, text="Test Information: ")
		self.TestInfo_Label.pack()


		for info in self.OPLInfoLabelName:
			self.Row_Frame = tkinter.Frame(self.askUserOPLInfo_Frame)
			self.Label_Label = tkinter.Label(self.Row_Frame, text=info, anchor='w')#, bg=self.background_Color)
			self.Entry_Entry = tkinter.Entry(self.Row_Frame)
			self.Row_Frame.pack(side=TOP, fill=X)
			self.Label_Label.pack(side=LEFT)
			self.Entry_Entry.pack(side=RIGHT, expand=YES, fill=X)
			self.OPLINfoEntry.append(self.Entry_Entry)


		self.continueToNextFrame = tkinter.Button(self.askUserOPLInfo_Frame, text='Continue', command=self.mainTestingFrame)#, bg=self.default_Color)
		self.continueToNextFrame.pack()


		# self.URLEntry = Entry(askUserOPLInfo_Frame)
		# self.example1 = tkinter.Button(self.askUserOPLInfo_Frame, text='Continue', command=self.mainTestingFrame, bg=self.default_Color)
		# self.askUserOPLInfo_Frame.pack()
		# self.example.pack()
		# self.example1.pack()

		# self.myParent.geometry('850x450')

		# self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width, height=self.chooseTestFrame_Height, bg=self.default_Color)
		# self.chooseTest_Frame.pack(side=LEFT, fill=Y)

		# self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text='Login_Security', command=self.loginSecurity, bg=self.default_Color)
		# self.loginSecurity_Button.pack()
		# self.loginSecurity_Button.place(y=self.chooseTestPlace_Yaxis, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text='Dashboard', command =self.dashBoard, bg=self.default_Color)
		# self.dashBoardPage_Button.pack()
		# self.dashBoardPage_Button.place(y=self.chooseTestPlace_Yaxis+self.chooseTestButton_Height, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text='Hiring Status', command = self.hiringStatus, bg=self.default_Color)
		# self.hiringStatusPage_Button.pack()
		# self.hiringStatusPage_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*2), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text='Order New Report', relief=RAISED, command = self.ordernewReport, bg=self.default_Color)
		# self.orderNewReport_Button.pack()
		# self.orderNewReport_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*3), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)


		# self.GUIuserInput_Frame = tkinter.Frame(self.myParent)
		# self.GUIuserInput_Frame.existElement = False

		# self.GUIconsoleFrame = tkinter.Frame(self.myParent)
		# self.GUIconsoleFrame.existElement = False

	def mainTestingFrame(self):
		dictValue = []

		for f in self.OPLINfoEntry:
			dictValue.append(f.get())

		Functions.OPLINfo = collections.OrderedDict(zip(self.OPLInfoLabelName, dictValue))

		self.askUserOPLInfo_Frame.destroy()

		self.myParent.geometry('850x450')

		self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width, height=self.chooseTestFrame_Height, bg=self.default_Color)
		self.chooseTest_Frame.pack(side=LEFT, fill=Y)

		self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text='Login_Security', command=self.loginSecurity, bg=self.default_Color)
		self.loginSecurity_Button.pack()
		self.loginSecurity_Button.place(y=self.chooseTestPlace_Yaxis, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text='Dashboard', command =self.dashBoard, bg=self.default_Color)
		self.dashBoardPage_Button.pack()
		self.dashBoardPage_Button.place(y=self.chooseTestPlace_Yaxis+self.chooseTestButton_Height, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text='Hiring Status', command = self.hiringStatus, bg=self.default_Color)
		self.hiringStatusPage_Button.pack()
		self.hiringStatusPage_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*2), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text='Order New Report', relief=RAISED, command = self.ordernewReport, bg=self.default_Color)
		self.orderNewReport_Button.pack()
		self.orderNewReport_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*3), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)


		self.GUIuserInput_Frame = tkinter.Frame(self.myParent)
		self.GUIuserInput_Frame.existElement = False

		self.GUIconsoleFrame = tkinter.Frame(self.myParent)
		self.GUIconsoleFrame.existElement = False


	def getUserInputSendFunction(self):
		if Functions.GUIallFieldError != None:
			Functions.GUIallFieldError.pack_forget()

		dictValue = []

		for f in fields:
			dictValue.append(f.get())

		Functions.orderNewReportResult = collections.OrderedDict(zip(whichInfo, dictValue))
		Functions.orderNewReportResult['Also Notify'] = 'Young Kim'

		allFieldCheck = GUIFunctions.orderNewReportuserInputFieldCheck()
		GUIFunctions.orderNewReportErrorMessageCheck(allFieldCheck, "Please Enter all fields")

	def makeUserInputForm(self):
		global fields
		fields = []

		for entry in whichInfo:	
			self.userInputRow_Frame = tkinter.Frame(self.GUIuserInput_Frame)
			self.userInputLabel_Label = tkinter.Label(self.userInputRow_Frame, width=self.userInputWidth, text=entry, anchor='center', bg=self.background_Color)
			self.userInputEntry_Entry = tkinter.Entry(self.userInputRow_Frame)
			self.userInputRow_Frame.pack(side=TOP, fill=X)
			self.userInputLabel_Label.pack(side=LEFT)
			self.userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
			fields.append(self.userInputEntry_Entry)

	def userInputFrame(self):
		if (self.GUIuserInput_Frame.existElement == True):
			self.GUIuserInput_Frame.destroy()
			self.GUIuserInput_Frame = tkinter.Frame(self.myParent)
		
		self.GUIuserInput_Frame.config(bg=self.background_Color)
		self.GUIuserInput_Frame.pack(side=LEFT, fill=X, padx=self.betweeenFrame)
		self.GUIuserInput_Frame.existElement = True

		Functions.GUIdisplay.GUIuserInputErrorRow_Frame = tkinter.Frame(self.GUIuserInput_Frame, bg=self.background_Color)
		Functions.GUIdisplay.GUIuserInputErrorRow_Frame.pack(side=TOP, fill=X)

		self.makeUserInputForm()
		self.userInputEnterRow_Frame = tkinter.Frame(self.GUIuserInput_Frame, bg=self.background_Color)
		self.userInputEnterRow_Frame.pack(side=TOP, fill=X)
		self.userInputEnterButton_Button = tkinter.Button(self.userInputEnterRow_Frame, text="Enter", command =self.getUserInputSendFunction)
		self.userInputEnterButton_Button.pack(side=RIGHT)

	def conSoleFrame(self):
		if (self.GUIconsoleFrame.existElement == True):
			self.GUIconsoleFrame.forget()
			self.GUIconsoleFrame = tkinter.Frame(self.myParent)

		self.GUIconsoleFrame.config(bg=self.background_Color)
		self.GUIconsoleFrame.pack(side=LEFT, fill=BOTH, padx=self.betweeenFrame, pady=5)
		self.GUIconsoleFrame.existElement = True

		self.bar_TabBar = Tab.TabBar(self.GUIconsoleFrame, "Evaluation")

		self.tab1_Tab = Tab.Tab(self.GUIconsoleFrame, "Evaluation")
		self.tab2_Tab = Tab.Tab(self.GUIconsoleFrame, "Console")

		self.bar_TabBar.add(self.tab1_Tab)
		self.bar_TabBar.add(self.tab2_Tab)
		self.bar_TabBar.show()

	def loginSecurity(self):
		Functions.GUIOPLFrame()
		GUIFunctions.buttonPressCheck()
		self.background_Color = 'light goldenrod yellow'
		self.current_Button = 'Login_Security'
		self.myParent.config(bg=self.background_Color)
		self.loginSecurity_Button.config(bg=self.background_Color, relief=FLAT)

		suite = unittest.TestLoader().loadTestsFromTestCase(Login_Security.Login_Security)
		unittest.TextTestRunner(verbosity=2).run(suite)
		
	def dashBoard(self):
		GUIFunctions.buttonPressCheck()
		self.background_Color = 'peach puff'
		self.current_Button = 'Dashboard'
		self.myParent.config(bg=self.background_Color)
		self.dashBoardPage_Button.config(bg=self.background_Color, relief=FLAT)

		suite = unittest.TestLoader().loadTestsFromTestCase(DashBoardPage.DashBoardPage)
		unittest.TextTestRunner(verbosity=2).run(suite)

	def hiringStatus(self):
		GUIFunctions.buttonPressCheck()
		self.background_Color = 'misty rose'
		self.current_Button = 'Hiring Status'
		self.myParent.config(bg=self.background_Color)
		self.hiringStatusPage_Button.config(bg=self.background_Color, relief=FLAT)

		suite = unittest.TestLoader().loadTestsFromTestCase(HiringStatusPage.HiringStatusPage)
		unittest.TextTestRunner(verbosity=2).run(suite)

	def ordernewReport(self):
		
		self.background_Color = 'lavender'
		GUIFunctions.buttonPressCheck()
		self.current_Button = 'Order New Report'
		self.myParent.config(bg=self.background_Color)
		self.orderNewReport_Button.config(bg=self.background_Color, relief=FLAT)
		

		global whichInfo
		whichInfo = ['First Name','Last Name', 'Email Address', 'PO Box', 'Cost Center', 'Color', 'Position Number', 'Favorite Number', 'Message to Consultant', 'Message to Assessee']
		self.userInputFrame()
		self.conSoleFrame()


if Functions.GUImainFrame == None:
	Functions.GUImainFrame = Tk()
	Functions.GUIdisplay = GUItkinter(Functions.GUImainFrame)
	Functions.GUImainFrame.mainloop()


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


################ How to embed a terminal in a Tkinter application?
# http://stackoverflow.com/questions/7253448/how-to-embed-a-terminal-in-a-tkinter-application


################ Console in the TkinterFrame
# http://tkinter.unpythonic.net/wiki/CmdTk

################ combination of Grid and Pack
# http://stackoverflow.com/questions/11257771/combining-grid-pack-tkinter
