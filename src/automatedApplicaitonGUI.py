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
		if displayType == 'e':
			Functions.GUIdisplay.textConsole_Text.insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.textConsole_Text.tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.textConsole_Text.tag_config("insert", background="white", foreground ="red")
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
			Functions.GUIdisplay.textEvaluation_Text.tag_config("insert", background="white", foreground ="black")
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
		self.OPLInfoWidth_Width = 22
		self.betweeenFrame = 5

		self.OPLFrame_Dimension = '300x170'
		self.mainFrame_Dimension = '900x530'
		self.LS_Dimension = '875x525'

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

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		# self.User_Input_Frame_Frame.existElement = False
		# self.User_Input_Frame_Frame.fullElement = False

		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)
		# self.OPL_Input_Frame_Frame.existElement = False
		# self.OPL_Input_Frame_Frame.fullElement = False
		# self.OPL_Input_Frame_Frame.Error_Label = tkinter.Label()
		# self.OPL_Input_Frame_Frame.Error_Label.existElement = False

		self.Custom_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)
		# self.Custom_Input_Frame_Frame.existElement = False
		# self.Custom_Input_Frame_Frame.Error_Label = tkinter.Label()
		# self.Custom_Input_Frame_Frame.Error_Label.existElement = False

	def mainTestingFrame(self):
		# relief FLAT == if frame does not contain all the elements that needed to be placed
		# relief RAISED == if frame contain all the elements that needed to be placed
		self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width, height=self.chooseTestFrame_Height, bg=self.default_Color)
		self.chooseTest_Frame.pack(side=LEFT, fill=Y)

		# self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text="Login_Security", command=self.loginSecurity, bg=self.default_Color)
		# self.loginSecurity_Button.pack()
		# self.loginSecurity_Button.place(y=self.chooseTestPlace_Yaxis, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text="Dashboard", command =self.dashBoard, bg=self.default_Color)
		# self.dashBoardPage_Button.pack()
		# self.dashBoardPage_Button.place(y=self.chooseTestPlace_Yaxis+self.chooseTestButton_Height, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text="Hiring Status", command = self.hiringStatus, bg=self.default_Color)
		# self.hiringStatusPage_Button.pack()
		# self.hiringStatusPage_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*2), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text="Order New Report", relief=RAISED, command = self.ordernewReport, bg=self.default_Color)
		self.orderNewReport_Button.pack()
		self.orderNewReport_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*3), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

# ["Email Address", "Email Password", "Portal Username", "Portal Password"]
	def ordernewReport(self):
		self.background_Color = "lavender"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Order New Report"
		self.current_Test = Test_Order1.Test_Order1
		self.myParent.config(bg=self.background_Color)
		self.orderNewReport_Button.config(bg=self.background_Color, relief=FLAT)

		self.User_Input_Frame_Frame.config(bg=self.background_Color)
		self.User_Input_Frame_Frame.pack(side=LEFT)

		self.frameType = "ONR1"
		self.createTitle_Frame(self.OPL_Input_Frame_Frame, "Login Information:", 16)
		self.createErrorLabel(self.OPL_Input_Frame_Frame) 
		self.createRadioButton(self.OPL_Input_Frame_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		self.whichInfoOPL = ["Portal Username", "Portal Password"]
		self.userInputFrame(self.OPL_Input_Frame_Frame)

		self.createExtraBlankRow_Frame(self.User_Input_Frame_Frame, 1)

		self.frameType = "ONR2"
		self.createTitle_Frame(self.Custom_Input_Frame_Frame, "Additional Information:", 16)
		self.createErrorLabel(self.Custom_Input_Frame_Frame)
		self.whichInfoCustom = ["First Name","Last Name", "Email Address", "Job Title", "PO Box", "Cost Center", "Color", "Position Number", "Favorite Number", "Message to Consultant", "Message to Assessee", "Also Notify", "New Tag Name"]
		self.userInputFrame(self.Custom_Input_Frame_Frame)
		self.createSaveButton(self.Custom_Input_Frame_Frame, "Save & Continue", self.GetUserInputSendFunction)

		self.ONR_GUIconsoleFrame = tkinter.Frame(self.myParent, relief=FLAT)
		self.conSoleFrame(self.ONR_GUIconsoleFrame)

	def createTitle_Frame(self, arg, txt, fontSize):
		if (arg.cget("relief") == FLAT):
			title_Label = tkinter.Label(arg, bg=self.background_Color, text=txt, font=(fontSize), anchor='w')
			title_Label.pack(side=TOP, fill=X)

	def createErrorLabel(self,arg):
		if (arg.cget("relief") == FLAT):
			arg.Error_Frame = tkinter.Frame(arg, bg=self.background_Color)
			arg.Error_Frame.pack(side=TOP, fill=X)
			arg.Error_Label = tkinter.Label(arg.Error_Frame, text=" ", fg='red', bg=self.background_Color, anchor = 'w')
			arg.Error_Label.pack(side=TOP, fill=X)

	def createRadioButton(self, arg, labelText, radioList, valueList):
		if (arg.cget("relief") == FLAT):
			if self.frameType == "ONR1":
				labelanchorAs = 'center'
				self.userInputWidth_Width = 23
				frameSideAs = TOP
				
				radioRow_Frame = Frame(arg, width=self.OPLInfoWidth_Width, bg=self.background_Color)
				radioRow_Frame.pack(side=frameSideAs, fill=X)
				radioLabel_Label = Label(radioRow_Frame, width=self.OPLInfoWidth_Width, text=labelText, anchor=labelanchorAs, bg=self.background_Color)
				radioLabel_Label.pack(side=LEFT)

				for radioText,valueText in zip(radioList, valueList):
					radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.URL, value=valueText, bg=self.background_Color)
					radioButton_Button.pack(side=LEFT)

	def GetUserInputSendFunction(self):
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

		if self.background_Color == "light goldenrod yellow": 
			arg.pack(side=LEFT, fill=Y, padx=self.betweeenFrame, expand=0)
		else:
			arg.pack(side=TOP, fill=X, padx=self.betweeenFrame)

		if (arg.cget("relief") == FLAT):
			self.makeUserInputForm(arg)

	# used in "userInputFrame"
	def makeUserInputForm(self, arg):
		if self.frameType == "LS":
			labelanchorAs = W
			self.userInputWidth_Width = 16
			frameSideAs = LEFT

		elif self.frameType == "ONR1":
			labelanchorAs = 'center'
			self.userInputWidth_Width = 23
			frameSideAs = TOP

			self.OPLINfoEntry = []
			for entry in self.whichInfoOPL:	
				userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
				userInputLabel_Label = tkinter.Label(userInputRow_Frame, width=self.userInputWidth_Width, text=entry, anchor=labelanchorAs, bg=self.background_Color)
				userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
				userInputRow_Frame.pack(side=frameSideAs, fill=X)
				userInputLabel_Label.pack(side=LEFT)
				userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
				self.OPLINfoEntry.append(userInputEntry_Entry)
			arg.config(relief=GROOVE)

		elif self.frameType == "ONR2":
			labelanchorAs = 'center'
			enterButtonContinue = "Save & Continue"
			self.userInputWidth_Width = 23
			frameSideAs = TOP

			self.CustomInfo = []
			for entry in self.whichInfoCustom:	
				userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
				userInputLabel_Label = tkinter.Label(userInputRow_Frame, width=self.userInputWidth_Width, text=entry, anchor=labelanchorAs, bg=self.background_Color)
				userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
				userInputRow_Frame.pack(side=frameSideAs, fill=X)
				userInputLabel_Label.pack(side=LEFT)
				userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
				self.CustomInfo.append(userInputEntry_Entry)
			arg.config(relief=GROOVE)

	def createExtraBlankRow_Frame(self, arg, howMany):
		if (arg.cget("relief") == FLAT):
			for i in range(howMany):
				extraRow_Label = Label(arg, bg=self.background_Color, text=" ")
				extraRow_Label.pack(side=TOP, fill=X)

	def createSaveButton(self, arg, buttonText, commandMethod):
		userInputEnterRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
		userInputEnterRow_Frame.pack(side=TOP, fill=X)
		UserInputEnterButton = tkinter.Button(userInputEnterRow_Frame, text=buttonText, command=commandMethod, relief=RAISED)
		UserInputEnterButton.pack(side=RIGHT)

	def conSoleFrame(self, arg):
		# print("arg: ", arg)
		if self.frameType == "LS":
			self.consoleTextWidth = 28
			self.consoleTextHeight = 32
			whichSide = RIGHT
		else: 
			self.consoleTextWidth = 62
			self.consoleTextHeight = 31
			whichSide = LEFT
		
		arg.config(bg=self.background_Color)
		arg.pack(side=whichSide, fill=BOTH, padx=self.betweeenFrame, pady=5)

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