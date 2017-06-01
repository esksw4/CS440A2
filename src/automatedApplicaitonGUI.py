import re, string, sys
import colorama
import collections
import time as time1

# import Login_Security
# import DashBoardPage
# import HiringStatusPage
# import OrderNewReport
# from Login_Security import Test_Login_Logout
# from Order_New_Report import Test_Order1

# from Login_Security import Test_PasswordRecovery
# from Login_Security import Test_PasswordUnlock
import Functions
import unittest, time, re
import Tab

import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.simpledialog as dlg
class GUIFunctions:
	def allFieldCheck(valueList, frame):
		if (len([v for v in valueList if v == '']) > 0): 
			return False
		else:
			# if OPL information is SAVED (user pressed save button) and all the information is all filled
			# and return true.
			frame.config(relief=RAISED)
			return True

	def errorMessageDisplay(allFieldCheckAnswer, errorLabel, LabelText):
		if allFieldCheckAnswer == False:
			errorLabel.config(text=LabelText, anchor=CENTER, bg=Functions.GUIdisplay.background_Color)
			errorLabel.pack()
		else:
			errorLabel.pack_forget()

	def outputDisplayConsole(text, displayType):
		if displayType == 'ie':
			Functions.GUIdisplay.textConsole_Text.insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.textConsole_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textConsole_Text.tag_config("insert", background="white", foreground ="red")
			Functions.GUIdisplay.bar_TabBar.switch_tab("Console")
		elif displayType == 'se':
			Functions.GUIdisplay.textConsole_Text.insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.textConsole_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textConsole_Text.tag_config("insert", background="white", foreground ="blue")
			Functions.GUIdisplay.bar_TabBar.switch_tab("Console")
		elif displayType == 'p':
			if Functions.GUIdisplay.textEvaluation_Text.get("0.0","100.0") is not '':
				Functions.GUIdisplay.textEvaluation_Text.delete("0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.textEvaluation_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="black")
		elif displayType == 's':
			Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.textEvaluation_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="green")
			GUIFunctions.orderNewReportCheckThis()
			Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	def orderNewReportCheckThis():
		Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, "Please Check these following information in the pivotal\n")
		temp = list(Functions.CustomInfo.keys())
		for i in temp:
			Functions.GUIdisplay.textEvaluation_Text.insert(INSERT, i + ": " +Functions.CustomInfo[i] + "\n")
			Functions.GUIdisplay.textEvaluation_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="green")

	def buttonPressCheck():
		if Functions.GUIdisplay.current_Button != None:
			# print(Functions.GUIdisplay.current_Button)
			if Functions.GUIdisplay.current_Button == "Order New Report":
				Functions.GUIdisplay.orderNewReport_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.OPL_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.Custom_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.ONR_GUIconsoleFrame.place_forget()
				Functions.GUIdisplay.userInputEnterRow_Frame.pack_forget()
				Functions.GUIdisplay.extraRow_Label.pack_forget()
				# Functions.GUIdisplay.ONR_GUIconsoleFrame.pack_forget()
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None

			elif Functions.GUIdisplay.current_Button == "Hiring Status":
				Functions.GUIdisplay.hiringStatusPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None

			elif Functions.GUIdisplay.current_Button == "Login_Security":
				Functions.GUIdisplay.loginSecurity_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.LS_LL_Frame.pack_forget()
				Functions.GUIdisplay.LS_PR_Frame.pack_forget()
				Functions.GUIdisplay.LS_PU_Frame.pack_forget()
				Functions.GUIdisplay.LS_LL_console_Frame.pack_forget()
				Functions.GUIdisplay.LS_PR_console_Frame.pack_forget()
				Functions.GUIdisplay.LS_PU_console_Frame.pack_forget()
				Functions.GUIdisplay.userInputEnterRow_Frame.pack_forget()
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None

			elif Functions.GUIdisplay.current_Button == "Dashboard":
				Functions.GUIdisplay.dashBoardPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None

# relief FLAT == if frame does not contain no fields // does not contain the console
# relief GROOVE == if frame CONTAINS all fields BUT NOT full entries // CONTAINS console but does not contain entries
# relief RAISED == if frame CONTAINS all fields & full entries // CONTAINS console & CONTAINS entries
class GUItkinter:
	def __init__(self, Parent):
		self.chooseTestFrame_Width = 100
		self.chooseTestFrame_Height = 450
		self.chooseTestButton_Height = 26
		self.chooseTestPlace_Yaxis = 173
		self.OPLInfoWidth_Width = 70
		self.betweeenFrame = 5

		self.OPLFrame_Dimension = '300x170'
		self.mainFrame_Dimension = '900x530'
		self.LS_Dimension = '1010x630'

		self.default_Color = Parent.cget("bg")
		self.background_Color = "White"

		self.URL = StringVar(value="empty")

		self.allFieldError = None
		self.current_Button = None

		self.GUIuserInputErrorRow_Frame = Frame()

		self.myParent = Parent
		self.myParent.geometry(self.mainFrame_Dimension)
		self.myParent.title("Automated Smoke Test")

		self.mainTestingFrame()

		# self.User_Input_Frame_Frame.existElement = False
		# self.User_Input_Frame_Frame.fullElement = False

		# self.OPL_Input_Frame_Frame.existElement = False
		# self.OPL_Input_Frame_Frame.fullElement = False
		# self.OPL_Input_Frame_Frame.Error_Label = tkinter.Label()
		# self.OPL_Input_Frame_Frame.Error_Label.existElement = False
		
		# self.Custom_Input_Frame_Frame.existElement = False
		# self.Custom_Input_Frame_Frame.Error_Label = tkinter.Label()
		# self.Custom_Input_Frame_Frame.Error_Label.existElement = False

	def mainTestingFrame(self):
		# relief FLAT == if frame does not contain all the elements that needed to be placed
		# relief RAISED == if frame contain all the elements that needed to be placed
		self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width)#, height=self.chooseTestFrame_Height, bg=self.default_Color)
		self.chooseTest_Frame.pack(side=LEFT, fill=Y)

		self.LS_LL_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.LS_LL_Info_Frame=tkinter.Frame(self.LS_LL_Frame, relief=FLAT)
		self.LS_LL_console_Frame = tkinter.Frame(self.LS_LL_Frame, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)

		self.LS_PR_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.LS_PR_console_Frame = tkinter.Frame(self.LS_PR_Frame, relief=FLAT)

		self.LS_PU_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.LS_PU_console_Frame = tkinter.Frame(self.LS_PU_Frame, relief=FLAT)

		self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text="Login_Security", command=self.loginSecurity, bg=self.default_Color)
		self.loginSecurity_Button.pack()
		self.loginSecurity_Button.place(y=self.chooseTestPlace_Yaxis, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text="Dashboard", command =self.dashBoard, bg=self.default_Color)
		# self.dashBoardPage_Button.pack()
		# self.dashBoardPage_Button.place(y=self.chooseTestPlace_Yaxis+self.chooseTestButton_Height, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text="Hiring Status", command = self.hiringStatus, bg=self.default_Color)
		# self.hiringStatusPage_Button.pack()
		# self.hiringStatusPage_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*2), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)
		self.Custom_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)

		self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text="Order New Report", relief=RAISED, command = self.ordernewReport, bg=self.default_Color)
		self.orderNewReport_Button.pack()
		self.orderNewReport_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*3), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

# ["Email Address", "Email Password", "Portal Username", "Portal Password"]

	def loginSecurity(self):
		import Test_LoginLogout

		self.myParent.geometry(self.LS_Dimension)

		self.background_Color = "light goldenrod yellow"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Login_Security"
		self.current_Test = Test_LoginLogout.Test_Login_Logout
		self.myParent.config(bg=self.background_Color)
		self.loginSecurity_Button.config(bg=self.background_Color, relief=FLAT)
		self.OPLInfoWidth_Width = 15

		self.frameType = "LSOPL"

		self.titleFrame_Anchor = 'w'
		self.titleLabel_PackSide = TOP
		# self.titleLabel_PackFill = NONE

		self.errorFrame_Anchor = 'w'
		self.errorFrame_PackSide = TOP
		# self.error_PackFill = NONE

		self.radioButtonFrame_Anchor = 'w'
		self.radioButtonFrame_PackSide = TOP
		self.radioButtonFrame_Width = 30
		self.radioButtonLabel_Width = 15
		self.radioButton_Width = 7

		self.userInputFrame_PackSide = TOP
		self.userInputFrame_PackFill = NONE
		self.userInputEntry_Expand = YES

		self.userInputFormFrame_Anchor = 'w'
		self.userInputFormFrame_PackSide = TOP
		# self.userInputFormFrame_PackFill = NONE

		self.extraLabel_PackSide = TOP
		self.extraLabel_PackFill = X

		self.saveButton_Anchor = 'e'
		self.saveButton_PackSide = TOP
		self.saveButton_ipadx = 82

		self.consoleTextWidth = 75
		self.consoleTextHeight = 6
		self.console_PackSide = RIGHT
		self.console_PackFill = NONE
		self.console_PlaceY = 0
		self.console_PlaceX = 300

		self.LS_LL_Frame.config(bg=self.background_Color)#, highlightcolor="green", highlightthickness=1)
		self.LS_LL_Frame.pack(side=LEFT, anchor='w', expand=YES, fill=X)

		self.LS_LL_Info_Frame.config(bg=self.background_Color)#, highlightcolor="red", highlightthickness=10)
		self.LS_LL_Info_Frame.pack(side=LEFT, fill=Y, anchor='w')
		#, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)
		# self.LS_PR_Frame.config(bg=self.background_Color, highlightcolor="blue", highlightthickness=1)
		# self.LS_PR_Frame.pack(fill=X)
		# self.LS_PU_Frame.config(bg=self.background_Color, highlightcolor="blue", highlightthickness=1)
		# self.LS_PU_Frame.pack(fill=X)

		self.createTitle_Frame(self.LS_LL_Info_Frame, "Login and Logout", 20)
		self.createErrorLabel(self.LS_LL_Info_Frame)
		self.whichInfoOPL = ["Portal Username", "Portal Password"]
		self.createRadioButton(self.LS_LL_Info_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		self.userInputFrame(self.LS_LL_Info_Frame)
		self.createSaveButton(self.LS_LL_Info_Frame, "Save & Continue", self.GetUserInputSendFunction)
		self.conSoleFrame(self.LS_LL_console_Frame)

		# self.createTitle_Frame(self.LS_PR_Frame, "Password Recovery", 20)
		# self.createErrorLabel(self.LS_PR_Frame)
		# self.createRadioButton(self.LS_PR_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		# self.whichInfoOPL = ["Email Address", "Email Password", "Portal Username", "Portal Password"]
		# self.userInputFrame(self.LS_PR_Frame)
		# self.createSaveButton(self.LS_PR_Frame, "Save & Continue", self.GetUserInputSendFunction)
		# self.conSoleFrame(self.LS_PR_console_Frame)

		# self.createTitle_Frame(self.LS_PU_Frame, "Password Unlock", 20)
		# self.createErrorLabel(self.LS_PU_Frame)
		# self.createRadioButton(self.LS_PU_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		# self.whichInfoOPL = ["Email Address", "Email Password", "Portal Username", "Portal Password"]
		# self.userInputFrame(self.LS_PU_Frame)
		# self.createSaveButton(self.LS_PU_Frame, "Save & Continue", self.GetUserInputSendFunction)
		# self.conSoleFrame(self.LS_PU_console_Frame)

	def ordernewReport(self):
		import Test_Order1

		self.myParent.geometry(self.mainFrame_Dimension)

		self.background_Color = "lavender"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Order New Report"
		self.current_Test = Test_Order1.Test_Order1
		self.myParent.config(bg=self.background_Color)
		self.orderNewReport_Button.config(bg=self.background_Color, relief=FLAT)

		self.titleLabel_Anchor = 'w'
		self.titleLabel_PackSide = TOP
		self.titleLabel_PackFill = X

		self.errorFrame_Anchor = 'w'
		self.errorFrame_PackSide = TOP

		self.radioButtonFrame_Anchor = 'w'
		self.radioButtonFrame_PackSide = TOP
		self.radioButtonFrame_Width = 30
		self.radioButtonLabel_Width = 15
		self.radioButton_Width = 7

		self.userInputFrame_PackSide = TOP
		self.userInputFrame_PackFill = X
		self.userInputEntry_Expand = NO

		self.User_Input_Frame_Frame.config(bg=self.background_Color)
		self.User_Input_Frame_Frame.pack(side=LEFT)

		self.frameType = "OPL"
		self.userInputFormFrame_Anchor = 'center'
		self.userInputFormFrame_PackSide = TOP
		self.userInputFormFrame_PackFill = X

		self.extraLabel_PackSide = TOP
		self.extraLabel_PackFill = X

		self.saveButton_Anchor = 'e'
		self.saveButton_PackSide = TOP
		self.saveButton_ipadx = 83

		self.consoleTextWidth = 62
		self.consoleTextHeight = 31
		self.console_PackSide = LEFT
		self.console_PackFill = X
		self.console_PlaceY = 0
		self.console_PlaceX = 390

		self.createTitle_Frame(self.OPL_Input_Frame_Frame, "Login Information:", 16)
		self.createErrorLabel(self.OPL_Input_Frame_Frame) 
		self.createRadioButton(self.OPL_Input_Frame_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		self.whichInfoOPL = ["Portal Username", "Portal Password"]
		self.userInputFrame(self.OPL_Input_Frame_Frame)
		self.createExtraBlankRow_Frame(self.User_Input_Frame_Frame, 1)

		self.frameType = "ONR"
		self.userInputFormLabel_Anchor = 'center'
		self.userInputFormFrame_PackSide = TOP
		self.userInputFormFrame_PackFill = X
		self.createTitle_Frame(self.Custom_Input_Frame_Frame, "Additional Information:", 16)
		self.createErrorLabel(self.Custom_Input_Frame_Frame)
		self.whichInfoCustom = ["First Name","Last Name", "Email Address", "Job Title", "PO Box", "Cost Center", "Color", "Position Number", "Favorite Number", "Message to Consultant", "Message to Assessee", "Also Notify", "New Tag Name"]
		self.userInputFrame(self.Custom_Input_Frame_Frame)
		self.createSaveButton(self.Custom_Input_Frame_Frame, "Save & Continue", self.GetUserInputSendFunction)

		self.ONR_GUIconsoleFrame = tkinter.Frame(self.myParent, relief=FLAT)
		self.conSoleFrame(self.ONR_GUIconsoleFrame)

	def createTitle_Frame(self, arg, txt, fontSize):
		# print(arg.cget("relief"))
		if (arg.cget("relief") == FLAT):
			title_Frame = tkinter.Frame(arg,bg=self.background_Color)#, highlightcolor="blue", highlightthickness=7)
			title_Frame.pack(side=TOP, anchor='w')
			title_Label = tkinter.Label(title_Frame, bg=self.background_Color, text=txt, font=(fontSize), anchor='w')
			title_Label.pack()

	def createErrorLabel(self,arg):
		if (arg.cget("relief") == FLAT):
			arg.Error_Frame = tkinter.Frame(arg, bg=self.background_Color)#, highlightcolor="blue", highlightthickness=7)
			arg.Error_Frame.pack(side=self.errorFrame_PackSide, anchor= self.errorFrame_Anchor)#fill=self.error_PackFill)
			arg.Error_Label = tkinter.Label(arg.Error_Frame, text=" ", fg='red', bg=self.background_Color)
			arg.Error_Label.pack(anchor='w')

	def createRadioButton(self, arg, labelText, radioList, valueList):
		if (arg.cget("relief") == FLAT):				
			radioRow_Frame = Frame(arg, bg=self.background_Color, width=self.radioButtonFrame_Width)#, highlightcolor="blue", highlightthickness=7)#, width=self.OPLInfoWidth_Width)
			radioRow_Frame.pack(side=self.radioButtonFrame_PackSide, anchor = self.radioButtonFrame_Anchor)#side=self.radioButton_FrameSide)#, fill=X)
			radioLabel_Label = Label(radioRow_Frame, text=labelText, bg=self.background_Color, width=self.radioButtonLabel_Width)#, width=int(self.OPLInfoWidth_Width*0.4))
			radioLabel_Label.pack(side=LEFT, anchor='center')

			for radioText,valueText in zip(radioList, valueList):
				radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.URL, value=valueText, bg=self.background_Color, width=self.radioButton_Width)
				radioButton_Button.pack(side=LEFT, anchor='w')

	def GetUserInputSendFunction(self):
		if self.frameType is not "LSOPL":
			self.OPL_Input_Frame_Frame.config(relief=GROOVE)
			self.Custom_Input_Frame_Frame.config(relief=GROOVE)

			self.OPLGetUserInputSendFunction()
			self.CustomGetUserInputSendFunction()

			if (self.OPL_Input_Frame_Frame.cget("relief") == RAISED and self.radioButtonCheck == True and self.Custom_Input_Frame_Frame.cget("relief") == RAISED):
				# get rid of error. This means everything is fine.
				self.OPL_Input_Frame_Frame.Error_Label.pack_forget()
				self.Custom_Input_Frame_Frame.Error_Label.pack_forget()
				# IF EVERYTHING IS FINE THEN RUN THE TEST!!!
				self.runTest()
		else:
			self.LS_LL_Frame.config(relief=GROOVE)
			self.LS_PR_Frame.config(relief=GROOVE)

	def OPLGetUserInputSendFunction(self):
		dictValue = []
		# First, check if self.URL gets either QA or Production. If it did not get anything, self.radioButtonCheck is False
		if self.URL.get() == "empty":
			self.radioButtonCheck = False
		# If it got something, self.radioButtonCheck is True
		else: 
			self.radioButtonCheck = True

		# If the OPL_Input_Frame_Frame contains full input fields but not all the entries' input are collected,

			# this checks if the all inputs are filled by the user, DEFAULTLY = NONE
		self.allFieldCheckAnswer = None
		# collects the data from the entries
		for f in self.OPLINfoEntry:
			dictValue.append(f.get())

		# Functions.OPLInfo collects the information and put it as ordred Dictionary
		Functions.OPLInfo = collections.OrderedDict(zip(self.whichInfoOPL, dictValue))
		# Check if all fields are filled. If not, it returns FALSE
		self.allFieldCheckAnswer = GUIFunctions.allFieldCheck(Functions.OPLInfo.values(), self.OPL_Input_Frame_Frame)
		# Display the erorr message if OPL_Input_Frame_Frame did not collect all the inputs.
		GUIFunctions.errorMessageDisplay(self.allFieldCheckAnswer, self.OPL_Input_Frame_Frame.Error_Label, "Please enter all fields.")
		
		# if OPL_Input_Frame_Frame collected all the information and radioButtonCheck is not collected, display the error message, instead of waiting for user to click "Save & Continue" button again
		if self.radioButtonCheck == False and self.allFieldCheckAnswer is True:
			GUIFunctions.errorMessageDisplay(self.radioButtonCheck, self.OPL_Input_Frame_Frame.Error_Label, "Please Select the server to test.")

	def CustomGetUserInputSendFunction(self):
		# when "Save & Continue" button is clicked, operate this. 
		dictValue = []
		# this checks if the all inputs are filled by the user, DEFAULTLY = NONE
		self.allFieldCheckAnswer = None
		# collects the data from the entries
		for f in self.CustomInfo:
			dictValue.append(f.get())

		# Functions.CustomInfo collects the information and put it as ordred Dictionary
		Functions.CustomInfo = collections.OrderedDict(zip(self.whichInfoCustom, dictValue))
		# Check if all fields are filled. If not it returns FALSE
		self.allFieldCheckAnswer = GUIFunctions.allFieldCheck(Functions.CustomInfo.values(), self.Custom_Input_Frame_Frame)
		# Display the erorr message if CUstom_Input_Frame_Frame did not collect all the inputs.
		GUIFunctions.errorMessageDisplay(self.allFieldCheckAnswer, self.Custom_Input_Frame_Frame.Error_Label, "Please enter all fields.")

		# # Regardless Custom_Input_Frame_Frame collected all the information, get information from OPL frame.
		# self.OPLGetUserInputSendFunction()
			
	def userInputFrame(self, arg):
		arg.config(bg=self.background_Color)
		arg.pack(side=self.userInputFrame_PackSide)#, fill=self.userInputFrame_PackFill)#, padx=self.betweeenFrame)

		if (arg.cget("relief") == FLAT):
			self.makeUserInputForm(arg)

	# used in "userInputFrame"
	def makeUserInputForm(self, arg):
		if self.frameType == "OPL" or self.frameType == "LSOPL":
			self.OPLINfoEntry = []
			for entry in self.whichInfoOPL:	
				userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color, width=self.radioButtonFrame_Width)#highlightcolor="blue", highlightthickness=7#, width=self.OPLInfoWidth_Width)
				userInputLabel_Label = tkinter.Label(userInputRow_Frame, text=entry, bg=self.background_Color, width=self.radioButtonLabel_Width+4)#,width=int(self.OPLInfoWidth_Width*0.4))
				userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
				userInputRow_Frame.pack(side=self.userInputFormFrame_PackSide, anchor=self.userInputFormFrame_Anchor)#fill=self.userInputFormFrame_PackFill)
				userInputLabel_Label.pack(side=LEFT, anchor='center')
				userInputEntry_Entry.pack(side=RIGHT)#, fill=X)#expand=self.userInputEntry_Expand)#
				self.OPLINfoEntry.append(userInputEntry_Entry)
			arg.config(relief=GROOVE)

		elif self.frameType == "ONR":
			self.CustomInfo = []
			for entry in self.whichInfoCustom:	
				userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color, width=self.radioButtonFrame_Width)#highlightcolor="blue", highlightthickness=7)#, width=self.OPLInfoWidth_Width)
				userInputLabel_Label = tkinter.Label(userInputRow_Frame, text=entry, bg=self.background_Color, width=self.radioButtonLabel_Width+5)
				userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
				userInputRow_Frame.pack(side=self.userInputFormFrame_PackSide, anchor=self.userInputFormFrame_Anchor)
				userInputLabel_Label.pack(side=LEFT, anchor='center')
				userInputEntry_Entry.pack(side=RIGHT)#, expand=self.userInputEntry_Expand)#, fill=X)
				self.CustomInfo.append(userInputEntry_Entry)
			arg.config(relief=GROOVE)

	def createExtraBlankRow_Frame(self, arg, howMany):
		if (arg.cget("relief") == FLAT):
			for i in range(howMany):
				self.extraRow_Label = Label(arg, bg=self.background_Color, text=" ")
				self.extraRow_Label.pack(side=self.extraLabel_PackSide, fill=self.extraLabel_PackFill)

	def createSaveButton(self, arg, buttonText, commandMethod):
		self.userInputEnterRow_Frame = tkinter.Frame(arg, bg=self.background_Color)#, highlightcolor="blue", highlightthickness=7)
		self.userInputEnterRow_Frame.pack(side=TOP, anchor='w', ipadx=self.saveButton_ipadx)
		UserInputEnterButton = tkinter.Button(self.userInputEnterRow_Frame, text=buttonText, command=commandMethod, relief=RAISED)
		UserInputEnterButton.pack(side=self.saveButton_PackSide, anchor=self.saveButton_Anchor)

	def conSoleFrame(self, arg):
		# print("arg: ", arg)

		arg.config(bg=self.background_Color)#, highlightcolor="blue", highlightthickness=1)
		arg.pack(side=self.console_PackSide)#, anchor='e')
		arg.place(y=self.console_PlaceY, x=self.console_PlaceX)
		# arg.pack(side=self.console_PackSide, anchor='e')#, fill=self.console_PackFill)#, padx=self.betweeenFrame, pady=5)

		if (arg.cget("relief") == FLAT):
			self.bar_TabBar = Tab.TabBar(arg, "Evaluation")
			tab1_Tab = Tab.Tab(arg, "Evaluation")
			tab2_Tab = Tab.Tab(arg, "Console")
			self.bar_TabBar.add(tab1_Tab)
			self.bar_TabBar.add(tab2_Tab)
			self.bar_TabBar.show()
			# arg.existElement = True
			arg.config(relief=GROOVE)

	def runTest(self):
		suite = unittest.TestLoader().loadTestsFromTestCase(self.current_Test)
		unittest.TextTestRunner(verbosity=2).run(suite)

if Functions.GUImainFrame == None:
	Functions.GUImainFrame = Tk()
	Functions.GUIdisplay = GUItkinter(Functions.GUImainFrame)
	Functions.GUImainFrame.mainloop()