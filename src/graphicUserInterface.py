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
	def buttonPressCheck():
		if Functions.GUIdisplay.current_Button != None:
			print(Functions.GUIdisplay.current_Button)
			if Functions.GUIdisplay.current_Button == "Order New Report":
				Functions.GUIdisplay.orderNewReport_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.ONR_GUIconsoleFrame.pack_forget()
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == "Hiring Status":
				Functions.GUIdisplay.hiringStatusPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == "Login_Security":
				Functions.GUIdisplay.loginSecurity_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.LS_LL_Frame.pack_forget()
				Functions.GUIdisplay.LS_PR_Frame.pack_forget()
				Functions.GUIdisplay.LS_PU_Frame.pack_forget()
				Functions.GUIdisplay.LS_LL_console_Frame.pack_forget()
				Functions.GUIdisplay.LS_PR_console_Frame.pack_forget()
				Functions.GUIdisplay.LS_PU_console_Frame.pack_forget()
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == "Dashboard":
				Functions.GUIdisplay.dashBoardPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None

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

		self.allFieldError = None
		self.current_Button = None

		self.GUIuserInputErrorRow_Frame = Frame()

		self.myParent = Parent
		self.myParent.geometry(self.mainFrame_Dimension)
		self.myParent.title("Automated Smoke Test")

		self.mainTestingFrame()

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent)
		self.User_Input_Frame_Frame.existElement = False
		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame)
		self.OPL_Input_Frame_Frame.existElement = False
		self.Custom_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame)
		self.Custom_Input_Frame_Frame.existElement = False

	def mainTestingFrame(self):
		self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width, height=self.chooseTestFrame_Height, bg=self.default_Color)
		self.chooseTest_Frame.pack(side=LEFT, fill=Y)
		self.chooseTest_Frame.existElement = True

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

	def ordernewReport(self):
		self.background_Color = "lavender"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Order New Report"
		self.myParent.config(bg=self.background_Color)
		self.orderNewReport_Button.config(bg=self.background_Color, relief=FLAT)

		self.User_Input_Frame_Frame.config(bg=self.background_Color)
		self.User_Input_Frame_Frame.pack(side=LEFT)

		self.includeTitle_Frame(self.OPL_Input_Frame_Frame, "Login Information:", 16)
		self.createErrorLabel(self.OPL_Input_Frame_Frame)
		self.creatingRadioButton(self.OPL_Input_Frame_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"], "ONR")
		self.whichInfo = ["Email Address", "Email Password", "Portal Username", "Portal Password"]
		self.userInputFrame(self.OPL_Input_Frame_Frame, "ONR1")

		self.includeExtraBlankRow_Frame(self.User_Input_Frame_Frame, 1)
		self.includeTitle_Frame(self.Custom_Input_Frame_Frame, "Additional Information:", 16)
		self.createErrorLabel(self.Custom_Input_Frame_Frame)
		self.whichInfo = ["First Name","Last Name", "Email Address", "Job Title", "PO Box", "Cost Center", "Color", "Position Number", "Favorite Number", "Message to Consultant", "Message to Assessee", "Also Notify", "New Tag Name"]
		self.userInputFrame(self.Custom_Input_Frame_Frame, "ONR2")

		self.ONR_GUIconsoleFrame = tkinter.Frame(self.myParent)
		self.ONR_GUIconsoleFrame.existElement = False
		# self.conSoleFrame(self.ONR_GUIconsoleFrame, "ONR")
		
		self.whichInfo = []

	def getUserInputSendFunction(self):
		if Functions.GUIallFieldError != None:
			Functions.GUIallFieldError.pack_forget()

		dictValue = []

		if self.OPL_Input_Frame_Frame.existElement:
			for f in self.OPLINfoEntry:
				dictValue.append(f.get())

			Functions.OPLINfo = collections.OrderedDict(zip(self.OPLInfoLabelName, dictValue))
			# print(Functions.OPLINfo['URL to test'])
			# allFieldCheck = GUIFunctions.userInputFieldCheck("OPL")
			# GUIFunctions.orderNewReportErrorMessageCheck(allFieldCheck,"OPL", "Please Enter all fields")

		# elif self.chooseTest_Frame.existElement:
		# 	for f in self.fields:
		# 		dictValue.append(f.get())

		# 	Functions.orderNewReportResult = collections.OrderedDict(zip(self.whichInfo, dictValue))
		# 	allFieldCheck = GUIFunctions.userInputFieldCheck("orderNewReport")
		# 	GUIFunctions.orderNewReportErrorMessageCheck(allFieldCheck,"orderNewReport", "Please Enter all fields")

	# used in "userInputFrame"
	def makeUserInputForm(self, arg, testType):
		if testType == "LS":
			labelanchorAs = W
			self.userInputWidth_Width = 16
			frameSideAs = LEFT

		elif testType == "ONR1" or testType == "ONR2":
			labelanchorAs = 'center'
			self.userInputWidth_Width = 23
			frameSideAs = TOP

		self.fields = []
		for entry in self.whichInfo:	
			userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
			userInputLabel_Label = tkinter.Label(userInputRow_Frame, width=self.userInputWidth_Width, text=entry, anchor=labelanchorAs, bg=self.background_Color)
			userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
			userInputRow_Frame.pack(side=frameSideAs, fill=X)
			userInputLabel_Label.pack(side=LEFT)
			userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
			self.fields.append(userInputEntry_Entry)

		userInputEnterRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
		userInputEnterRow_Frame.pack(side=TOP, fill=X)
		userInputEnterButton_Button = tkinter.Button(userInputEnterRow_Frame, text="Enter", command =self.getUserInputSendFunction)
		userInputEnterButton_Button.pack(side=RIGHT)

	def createErrorLabel(self,arg):
		arg.Error_Label = tkinter.Label(arg, text=" ", bg=self.background_Color, anchor = 'w', height=0)
		arg.Error_Label.pack(side=TOP, fill=X)

	def userInputFrame(self, arg, testType):
		arg.config(bg=self.background_Color)

		if self.background_Color == "light goldenrod yellow": 
			arg.pack(side=LEFT, fill=Y, padx=self.betweeenFrame, expand=0)
		else:
			arg.pack(side=TOP, fill=X, padx=self.betweeenFrame)

		if (arg.existElement == False):
			arg.existElement = True
			self.makeUserInputForm(arg, testType)

	def creatingRadioButton(self, arg, labelText, radioList, valueList, testType):
		if testType == "ONR":
			labelanchorAs = 'center'
			self.userInputWidth_Width = 23
			frameSideAs = TOP
			self.URL = StringVar(value="empty")
			radioRow_Frame = Frame(arg, width=self.OPLInfoWidth_Width, bg=self.background_Color)
			radioRow_Frame.pack(side=frameSideAs, fill=X)
			radioLabel_Label = Label(radioRow_Frame, width=self.OPLInfoWidth_Width, text=labelText, anchor=labelanchorAs, bg=self.background_Color)
			radioLabel_Label.pack(side=LEFT)

			for radioText,valueText in zip(radioList, valueList):
				radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.URL, value=valueText, bg=self.background_Color)
				radioButton_Button.pack(side=LEFT)

	def includeExtraBlankRow_Frame(self, arg, howMany):
		if (arg.existElement == False):
	 		for i in range(howMany):
	 			# extraRow_Frame= Frame(arg, bg=self.background_Color)
	 			# extraRow_Frame.pack(side=TOP, fill=X)
	 			extraRow_Label = Label(arg, bg=self.background_Color, text=" ")
	 			extraRow_Label.pack(side=LEFT, fill=X)

	def includeTitle_Frame(self, arg, txt, fontSize):
		if (arg.existElement == False):
			title_Label = tkinter.Label(arg, bg=self.background_Color, text=txt, font=(fontSize), anchor='w')
			title_Label.pack(side=TOP, fill=X)

if Functions.GUImainFrame == None:
	Functions.GUImainFrame = Tk()
	Functions.GUIdisplay = GUItkinter(Functions.GUImainFrame)
	Functions.GUImainFrame.mainloop()