import re, string, sys
import colorama
import collections
import time as time1

# import Login_Security
# import DashBoardPage
# import HiringStatusPage
# import OrderNewReport
import Test_LoginLogout
# from Order_New_Report import Test_Order1

# from Login_Security import Test_PasswordRecovery
# from Login_Security import Test_PasswordUnlock
import Functions
import unittest, time, re
import Tab
# import Checkbar

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

	def outputDisplayConsole(text, testCaseName, displayType):
		# ie: Input Error
		# se: System Error
		# m: manually test this
		# s: Successfully tested
		Functions.GUIdisplay.testName = testCaseName
		if displayType == 'ie':
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][1].config(state=NORMAL)
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][1].insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][1].tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][1].tag_config("insert", background="white", foreground ="red")
			Functions.GUIdisplay.bar_TabBar.switch_tab("Console")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][1].config(state=DISABLED)
		elif displayType == 'se':
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].config(state=NORMAL)
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].tag_config("insert", background="white", foreground ="red")
			Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].config(state=DISABLED)
		elif displayType == 'm':
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].config(state=NORMAL)
			if Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].get("0.0","100.0") is not '':
				Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].delete("0.0", "100.0")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].tag_config("insert", background="white", foreground ="green")
			Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].config(state=DISABLED)
		elif displayType == 's':
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].config(state=NORMAL)
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "  " + text + "\n\n")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].tag_add("insert", "0.0", "100.0")
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].tag_config("insert", background="white", foreground ="green")
			if Functions.GUIdisplay.testName == "Order Existing Title with New Assessee":
				GUIFunctions.orderNewReportCheckThis()
			elif Functions.GUIdisplay.testName == "Login Logout":
				GUIFunctions.loginLogoutCheckThis()
			elif Functions.GUIdisplay.testName == "Password Recovery":
				GUIFunctions.passwordRecoveryCheckThis()
			elif Functions.GUIdisplay.testName == "Password Unlock":
				GUIFunctions.passwordUnlockCheckThis()
			Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].config(state=DISABLED)

			# Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	def orderNewReportCheckThis():
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "Following function(s) was(were) evaluated successfully: \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Checking 'Order a Report/Assessment' button \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Order with existing title \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Order with new assessee \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Create a new tag \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "\t * Please check '%s' tag in tag list \n" % Functions.CustomInfo['New Tag Name'])
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Search with assessee name \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Copy assessment URL \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Cancel Order \n")
		Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	def loginLogoutCheckThis():
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "Following function(s) was(were) evaluated successfully: \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Login/Logout \n")
		Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	def passwordRecoveryCheckThis():
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "Following function(s) was(were) evaluated successfully: \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Password Reset \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Password Recovery \n")
		Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	def passwordUnlockCheckThis():
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "Following function(s) was(were) evaluated successfully: \n")
		Functions.GUIdisplay.consoleTab[Functions.GUIdisplay.testName][0].insert(INSERT, "- Resend email for unlock instruction \n")
		Functions.GUIdisplay.bar_TabBar.switch_tab("Evaluation")

	def buttonPressCheck():
		if Functions.GUIdisplay.current_Button != None:
			# print(Functions.GUIdisplay.current_Button)
			if Functions.GUIdisplay.current_Button == "Login_Security":
				Functions.GUIdisplay.loginSecurity_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.testCases_Frame.pack_forget()
				Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.OPL_Input_Frame_Frame.pack_forget()
				for j in Functions.GUIdisplay.checkBoxInfo.keys():
					Functions.GUIdisplay.checkBoxInfo[j][2][0].pack_forget()
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None
				Functions.GUIdisplay.URL = StringVar(value="empty")

			elif Functions.GUIdisplay.current_Button == "Dashboard":
				Functions.GUIdisplay.dashBoardPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.testCases_Frame.pack_forget()
				Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.OPL_Input_Frame_Frame.pack_forget()
				for j in Functions.GUIdisplay.checkBoxInfo.keys():
					Functions.GUIdisplay.checkBoxInfo[j][2][0].pack_forget()
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None
				Functions.GUIdisplay.URL = StringVar(value="empty")

			elif Functions.GUIdisplay.current_Button == "Hiring Status":
				Functions.GUIdisplay.hiringStatusPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.testCases_Frame.pack_forget()
				Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.OPL_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.checkEnter.pack_forget()
				for j in Functions.GUIdisplay.checkBoxInfo.keys():
					Functions.GUIdisplay.checkBoxInfo[j][2][0].pack_forget()
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None
				Functions.GUIdisplay.URL = StringVar(value="empty")

			elif Functions.GUIdisplay.current_Button == "Order New Report":
				Functions.GUIdisplay.orderNewReport_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.testCases_Frame.pack_forget()
				Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.OPL_Input_Frame_Frame.pack_forget()
				Functions.GUIdisplay.Custom_Input_Frame_Frame.pack_forget()
				for j in Functions.GUIdisplay.checkBoxInfo.keys():
					Functions.GUIdisplay.checkBoxInfo[j][2][0].pack_forget()
				# Functions.GUIdisplay.userInputEnterRow_Frame.pack_forget()
				# Functions.GUIdisplay.extraRow_Label.pack_forget()
				# Functions.GUIdisplay.ONR_GUIconsoleFrame.pack_forget()
				Functions.GUIdisplay.current_Button = None
				Functions.GUIdisplay.current_Test = None
				Functions.GUIdisplay.URL = StringVar(value="empty")
			
# relief FLAT == if frame does not contain no fields // does not contain the console
# relief GROOVE == if frame CONTAINS all fields BUT NOT full entries and SAVE BUTTON// CONTAINS console but does not contain entries
# relief GROOVE == if frame CONTAINS all fields AND SAVE BUTTON BUT NOT full entries
# relief RAISED == if frame CONTAINS all fields & full entries // CONTAINS console & CONTAINS entries
class GUItkinter:
	def __init__(self, Parent):
		self.chooseTestFrame_Width = 140
		self.chooseTestFrame_Height = 450
		self.chooseTestButton_Width = 130
		self.chooseTestButton_Height = 26
		self.chooseTestPlace_Yaxis = 173
		self.OPLInfoWidth_Width = 75
		self.betweeenFrame = 5

		self.OPLFrame_Dimension = '300x170'
		self.mainFrame_Dimension = '980x530'
		self.max1_Dimension = '900x450'
		self.max2_Dimension = '900x600'
		self.max3_Dimension = '900x750'
		self.max4_Dimension = '900x850'
		self.max5_Dimension = '900x950' 

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

	def mainTestingFrame(self):
		# relief FLAT == if frame does not contain all the elements that needed to be placed
		# relief RAISED == if frame contain all the elements that needed to be placed

		self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width, highlightcolor="blue", highlightthickness=7)#, height=self.chooseTestFrame_Height, bg=self.default_Color)
		self.chooseTest_Frame.pack(side=LEFT, anchor=W, fill=Y)

		self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text="Login_Security", command=self.loginSecurity, bg=self.default_Color)
		self.loginSecurity_Button.pack(side=LEFT)
		self.loginSecurity_Button.place(y=self.chooseTestPlace_Yaxis, height=self.chooseTestButton_Height, width=self.chooseTestButton_Width)

		self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text="Dashboard", command =self.dashBoard, bg=self.default_Color)
		self.dashBoardPage_Button.pack()
		self.dashBoardPage_Button.place(y=self.chooseTestPlace_Yaxis+self.chooseTestButton_Height, height=self.chooseTestButton_Height, width=self.chooseTestButton_Width)

		self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text="Hiring Status", command = self.hiringStatus, bg=self.default_Color)
		self.hiringStatusPage_Button.pack()
		self.hiringStatusPage_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*2), height=self.chooseTestButton_Height, width=self.chooseTestButton_Width)

		self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text="Order New Report", relief=RAISED, command = self.ordernewReport, bg=self.default_Color)
		self.orderNewReport_Button.pack(side=LEFT)
		self.orderNewReport_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*3), height=self.chooseTestButton_Height, width=self.chooseTestButton_Width)

# ["Email Address", "Email Password", "Portal Username", "Portal Password"]

	def loginSecurity(self):
		import Test_LoginLogout
		import Test_PasswordRecovery
		import Test_PasswordUnlock

		self.myParent.geometry(self.max2_Dimension)

		self.background_Color = "light goldenrod yellow"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Login_Security"
		# self.current_Test = Test_LoginLogout.Test_Login_Logout
		self.myParent.config(bg=self.background_Color)
		self.loginSecurity_Button.config(bg=self.background_Color, relief=FLAT)
		self.OPLInfoWidth_Width = 15

		self.frameType = "LSOPL"

		self.testCases_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.rootOfEnterButton = self.testCases_Frame
		self.EnterButton_width = 7
		self.EnterButton_Height = 1

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)

		self.LS_LL_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		self.LS_PR_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.LS_PU_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)

		self.UserInputFrame_Anchor = NW
		self.UserInputFrame_PackSide = TOP
		self.UserInputFrame_PackFill = X
		self.userInputFrame_PackExpand = YES		

		self.OPLInputFrame_PackSide = LEFT
		self.OPLInputFrame_PackFill = X
		self.OPLInputFrame_PackExpand = YES

		self.titleFrame_Anchor = NW
		self.titleLabel_PackSide = TOP
		# self.titleLabel_PackFill = NONE

		self.errorFrame_Anchor = CENTER
		self.errorFrame_PackSide = TOP
		self.errorLabel_PackFill = X

		self.radioButtonFrame_Anchor = W
		self.radioButtonFrame_PackSide = TOP
		self.radioButtonFrame_Width = 33
		self.radioButtonLabel_Width = 17
		self.radioButton_Width = 7

		self.userInputFormFrame_Anchor = NW
		self.userInputFormFrame_PackSide = TOP
		# self.userInputFormFrame_PackFill = NONE

		self.extraLabel_PackSide = TOP
		self.extraLabel_PackFill = X

		self.saveButton_Anchor = E
		self.saveButton_PackSide = TOP
		self.saveButton_ipadx = 88

		self.consoleTextWidth = 90
		self.consoleTextHeight = 7
		self.consolePack_padx = 10
		self.consoleFrame_Anchor = NW
		self.consoleFrame_PackSide = TOP
		self.consoleFrame_PackFill = X
		self.consoleFrame_PackExpand = YES
		# self.console_PlaceY = 0
		# self.console_PlaceX = 10

		self.testInfoFrames = [self.OPL_Input_Frame_Frame]

		self.checkBoxInfo =collections.OrderedDict({"Login Logout": [["Portal Username", "Portal Password"],[Test_LoginLogout.Test_LoginLogout], [self.LS_LL_console_Frame]], \
							"Password Recovery": [["Portal Username", "Portal Password to change", "Email Address", "Email Password"],[Test_PasswordRecovery.Test_PasswordRecovery], [self.LS_PR_console_Frame]], \
							"Password Unlock": [["Portal Username", "Portal Password", "Email Address", "Email Password"],[Test_PasswordUnlock.Test_PasswordUnlock],[self.LS_PU_console_Frame]]})

		self.createCheckButton([self.testCases_Frame], 20)

	def dashBoard(self):
		import Test_Circles
		import Test_OrderReportButton
		import Test_SwitchDifferentLanguage
		import Test_ViewReport

		self.myParent.geometry(self.max2_Dimension)

		self.background_Color = "peach puff"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Dashboard"
		self.myParent.config(bg=self.background_Color)
		self.dashBoardPage_Button.config(bg=self.background_Color, relief=FLAT)
		self.OPLInfoWidth_Width = 15

		self.frameType = "OPL"

		self.testCases_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.rootOfEnterButton = self.testCases_Frame
		self.EnterButton_width = 7
		self.EnterButton_Height = 1

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)

		self.DB_CC_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		self.DB_ORB_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.DB_SDL_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.DB_VRT_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)

		self.UserInputFrame_Anchor = NW
		self.UserInputFrame_PackSide = TOP
		self.UserInputFrame_PackFill = X
		self.userInputFrame_PackExpand = YES		

		self.OPLInputFrame_PackSide = LEFT
		self.OPLInputFrame_PackFill = X
		self.OPLInputFrame_PackExpand = YES

		self.titleFrame_Anchor = NW
		self.titleLabel_PackSide = TOP
		# self.titleLabel_PackFill = NONE

		self.errorFrame_Anchor = CENTER
		self.errorFrame_PackSide = TOP
		self.errorLabel_PackFill = X

		self.radioButtonFrame_Anchor = W
		self.radioButtonFrame_PackSide = TOP
		self.radioButtonFrame_Width = 33
		self.radioButtonLabel_Width = 17
		self.radioButton_Width = 7

		self.userInputFormFrame_Anchor = NW
		self.userInputFormFrame_PackSide = TOP
		# self.userInputFormFrame_PackFill = NONE

		self.extraLabel_PackSide = TOP
		self.extraLabel_PackFill = X

		self.saveButton_Anchor = E
		self.saveButton_PackSide = TOP
		self.saveButton_ipadx = 88

		self.consoleTextWidth = 90
		self.consoleTextHeight = 7
		self.consolePack_padx = 10
		self.consoleFrame_Anchor = NW
		self.consoleFrame_PackSide = TOP
		self.consoleFrame_PackFill = X
		self.consoleFrame_PackExpand = YES

		self.testInfoFrames = [self.OPL_Input_Frame_Frame]

		self.checkBoxInfo =collections.OrderedDict({"Click Circles": [["Portal Username", "Portal Password"],[Test_Circles.Test_Circles], [self.DB_CC_console_Frame]], \
							"Order Report Button": [["Portal Username", "Portal Password"],[Test_OrderReportButton.Test_OrderReportButton], [self.DB_ORB_console_Frame]], \
							"Switch Different language": [["Portal Username", "Portal Password"],[Test_SwitchDifferentLanguage.Test_SwitchDifferentLanguage],[self.DB_SDL_console_Frame]], \
							"View Report Tab": [["Portal Username", "Portal Password"], [Test_ViewReport.Test_ViewReport],[self.DB_VRT_console_Frame]]})

		self.createCheckButton([self.testCases_Frame], 20)

	def hiringStatus(self):
		import Test_FilterByStatus
		import Test_FilterbyDateRange
		import Test_FilterBySupervisor
		import Test_HiringFunction
		import Test_DontHireFunction
		import Test_RetireFunction
		import Test_SearchForAssessee
		import Test_SortingDropdown

		self.myParent.geometry(self.mainFrame_Dimension)

		self.background_Color = "misty rose"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Hiring Status"
		self.myParent.config(bg=self.background_Color)
		self.hiringStatusPage_Button.config(bg=self.background_Color, relief=FLAT)
		self.OPLInfoWidth_Width = 15

		self.frameType = "OPL"

		self.testCases_Frame = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		self.testCases_Frame.pack(side=TOP, anchor=NW, fill=X)
		self.testCases_Frame1 = tkinter.Frame(self.testCases_Frame, relief=FLAT)#, highlightcolor="red", highlightthickness=7)
		self.testCases_Frame2 = tkinter.Frame(self.testCases_Frame, relief=FLAT)# highlightcolor="black", highlightthickness=7)
		self.rootOfEnterButton = self.testCases_Frame1
		self.EnterButton_width = 10
		self.EnterButton_Height = 1

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)

		self.HS_FBStatus_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		self.HS_FBSupervisor_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.HS_FBDate_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.HS_Hire_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.HS_DHire_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		self.HS_Retire_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.HS_SFA_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.HS_SD_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)

		self.UserInputFrame_Anchor = NW
		self.UserInputFrame_PackSide = TOP
		self.UserInputFrame_PackFill = X
		self.userInputFrame_PackExpand = YES		

		self.OPLInputFrame_PackSide = LEFT
		self.OPLInputFrame_PackFill = X
		self.OPLInputFrame_PackExpand = YES

		self.titleFrame_Anchor = NW
		self.titleLabel_PackSide = TOP
		# self.titleLabel_PackFill = NONE

		self.errorFrame_Anchor = CENTER
		self.errorFrame_PackSide = TOP
		self.errorLabel_PackFill = X

		self.radioButtonFrame_Anchor = W
		self.radioButtonFrame_PackSide = TOP
		self.radioButtonFrame_Width = 33
		self.radioButtonLabel_Width = 17
		self.radioButton_Width = 7

		self.userInputFormFrame_Anchor = NW
		self.userInputFormFrame_PackSide = TOP
		# self.userInputFormFrame_PackFill = NONE


		self.extraLabel_PackSide = TOP
		self.extraLabel_PackFill = X

		self.saveButton_Anchor = E
		self.saveButton_PackSide = TOP
		self.saveButton_ipadx = 88

		self.consoleTextWidth = 90
		self.consoleTextHeight = 7
		self.consolePack_padx = 10
		self.consoleFrame_Anchor = NW
		self.consoleFrame_PackSide = TOP
		self.consoleFrame_PackFill = X
		self.consoleFrame_PackExpand = YES

		self.testInfoFrames = [self.OPL_Input_Frame_Frame]

		# self.HS_FBStatus_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		# self.HS_FBDate_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		# self.HS_FBSupervisor_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		# self.HS_Hire_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		# self.HS_DHire_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		# self.HS_Retire_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		# self.HS_SFA_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		# self.HS_SD_console_Frame = tkinter.Frame(self.myParent, relief=FLAT)

		self.checkBoxInfo =collections.OrderedDict({"Filter by Status": [["Portal Username", "Portal Password"],[Test_FilterByStatus.Test_FilterByStatus], [self.HS_FBStatus_console_Frame]], \
							"Filter by Date Range": [["Portal Username", "Portal Password"],[Test_FilterbyDateRange.Test_FilterbyDateRange], [self.HS_FBDate_console_Frame]], \
							"Filter By Supervisor": [["Portal Username", "Portal Password"],[Test_FilterBySupervisor.Test_FilterBySupervisor],[self.HS_FBSupervisor_console_Frame]], \
							"Hire": [["Portal Username", "Portal Password"], [Test_HiringFunction.Test_HiringFunction],[self.HS_Hire_console_Frame]], \
							"Don't Hire": [["Portal Username", "Portal Password"], [Test_DontHireFunction.Test_DontHireFunction],[self.HS_DHire_console_Frame]], \
							"Retire": [["Portal Username", "Portal Password"], [Test_RetireFunction.Test_RetireFunction],[self.HS_Retire_console_Frame]], \
							"Search For Assessee": [["Portal Username", "Portal Password"], [Test_SearchForAssessee.Test_SearchForAssessee],[self.HS_SFA_console_Frame]], \
							"Sorting Dropdown": [["Portal Username", "Portal Password"], [Test_SortingDropdown.Test_SortingDropdown],[self.HS_SD_console_Frame]]})

		self.createCheckButton([self.testCases_Frame1,self.testCases_Frame2], 20)
		
	def ordernewReport(self):
		import Test_Order1

		self.myParent.geometry(self.mainFrame_Dimension)

		self.background_Color = "lavender"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Order New Report"
		self.myParent.config(bg=self.background_Color)
		self.orderNewReport_Button.config(bg=self.background_Color, relief=FLAT)

		self.testCases_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.rootOfEnterButton = self.testCases_Frame
		self.EnterButton_width = 7
		self.EnterButton_Height = 1

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent, relief=FLAT)
		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)
		self.Custom_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)

		self.ONR_GUIconsoleFrame = tkinter.Frame(self.myParent, relief=FLAT)

		self.UserInputFrame_Anchor = NW
		self.UserInputFrame_PackSide = LEFT
		self.UserInputFrame_PackFill = NONE
		self.userInputFrame_PackExpand = FALSE

		self.OPLInputFrame_PackSide = TOP
		self.OPLInputFrame_PackFill = NONE
		self.OPLInputFrame_PackExpand = YES

		# self.titleLabel_Anchor = W
		# self.titleLabel_PackSide = TOP
		# self.titleLabel_PackFill = X

		self.errorFrame_Anchor = CENTER
		self.errorFrame_PackSide = TOP
		self.errorLabel_PackFill = NONE

		self.radioButtonFrame_Anchor = W
		self.radioButtonFrame_PackSide = TOP
		self.radioButtonFrame_Width = 30
		self.radioButtonLabel_Width = 15
		self.radioButton_Width = 7


		self.frameType = "OPL"
		self.userInputFormFrame_Anchor = NW
		self.userInputFormFrame_PackSide = TOP
		self.userInputFormFrame_PackFill = X

		self.extraLabel_PackSide = TOP
		self.extraLabel_PackFill = X

		self.saveButton_Anchor = 'e'
		self.saveButton_PackSide = TOP
		self.saveButton_ipadx = 83

		self.consoleTextWidth = 66
		self.consoleTextHeight = 28
		self.consolePack_padx = 0
		self.consoleFrame_PackSide = RIGHT
		self.consoleFrame_PackFill = NONE
		self.consoleFrame_Anchor = NE
		self.consoleFrame_PackExpand = FALSE
		# self.console_PlaceY = 0
		# self.console_PlaceX = 390

		self.testInfoFrames = [self.OPL_Input_Frame_Frame, self.Custom_Input_Frame_Frame]

		self.checkBoxInfo = collections.OrderedDict({"Order Existing Title with New Assessee":[["Portal Username", "Portal Password"],[Test_Order1.Test_Order1],[self.ONR_GUIconsoleFrame]]})
		self.createCheckButton([self.testCases_Frame], 20)

	def onPress(self,this):
		if self.testUserTestCases[this] == 0:
			self.testUserTestCases[this] = 1
		elif self.testUserTestCases[this] == 1:
			self.testUserTestCases[this] = 0


		# if self.testCases[this] == 0:
		# 	self.testCases[this] = 1
		# 	self.frame.config(bg=self.background_Color)#, highlightcolor="green", highlightthickness=1)
		# 	self.frame.pack(side=TOP, anchor='w', expand=YES, fill=X)
		# 	self.infoFrame.config(bg=self.background_Color)#, highlightcolor="red", highlightthickness=10)
		# 	self.infoFrame.pack(side=LEFT, fill=Y, anchor='w')

		# 	self.createTitle_Frame(self.infoFrame, this, 20)
		# 	self.createErrorLabel(self.infoFrame)
		# 	self.whichInfoOPL = ["Email Address", "Email Password", "Portal Username", "Portal Password"]
		# 	self.createRadioButton(self.infoFrame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		# 	self.userInputFrame(self.infoFrame)
		# 	self.createSaveButton(self.infoFrame, "Save & Continue", self.GetUserInputSendFunction(this, self.infoFrame))
		# 	self.conSoleFrame(self.consoleFrame)

		# else: 
		# 	self.testCases[this] = 0
		# 	self.frame.pack_forget()
		# 	self.consoleFrame.pack_forget()
		# 	Functions.GUIdisplay.userInputEnterRow_Frame.pack_forget()
		# 	Functions.GUIdisplay.current_Button = None
		# 	Functions.GUIdisplay.current_Test = None

	def onOKPress(self):
		for i in self.checkButtonsEntered:
			i.config(state=DISABLED)
		self.checkEnter.config(state=DISABLED)

		self.testToRun = []
		self.whichInfoOPL= collections.OrderedDict()
		self.consoleToDisplay = []
		for k in self.testInfoFrames:
			if k.cget("relief") is not FLAT:
				k.pack_forget()
				k = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)#, highlightcolor="blue", highlightthickness=7)#, highlightcolor="blue", highlightthickness=7)
		# remove console frame and re open it
		for j in self.checkBoxInfo.keys():
			self.checkBoxInfo[j][2][0].pack_forget()
			self.checkBoxInfo[j][2][0] = tkinter.Frame(self.myParent, relief=FLAT)#, highlightcolor="black", highlightthickness=7)

		# decide which cases are taken considred 
		for i in list(self.testUserTestCases.keys()):
			if self.testUserTestCases[i] == 1:
				self.whichInfoOPL.update(zip(self.checkBoxInfo[i][0], [0]*len(self.checkBoxInfo[i][0])))
				self.testToRun.append(self.checkBoxInfo[i][1][0])
				self.consoleToDisplay.append(self.checkBoxInfo[i][2][0])
			else:
				del self.testUserTestCases[i]
		# print(self.whichInfoOPL)

		# self.whichInfoOPL = list(self.whichInfoOPL.keys())
		self.User_Input_Frame_Frame.config(bg=self.background_Color)#, highlightcolor="red", highlightthickness=7)
		self.User_Input_Frame_Frame.pack(side=self.UserInputFrame_PackSide, anchor=self.UserInputFrame_Anchor, fill=self.UserInputFrame_PackFill, expand=self.userInputFrame_PackExpand)

		for k in self.testInfoFrames:
			k.config(bg=self.background_Color)#, highlightcolor="blue", highlightthickness=7)
			k.pack(side=self.OPLInputFrame_PackSide, fill=self.OPLInputFrame_PackFill, expand=self.OPLInputFrame_PackExpand)
		self.createErrorLabel()
		self.createRadioButton(self.testInfoFrames[0], "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		self.userInputFrame()
		# self.testInfoFrames[len(self.testInfoFrames)-1].config(relief=FLAT)
		self.createSaveButton(self.testInfoFrames[len(self.testInfoFrames)-1], "Save & Continue", self.GetUserInputSendFunction)
		self.conSoleFrame(self.consoleToDisplay)

	def createCheckButton(self, parent, fontsize):
		# to disable choosing user test cases when click "OK" button
		self.checkButtonsEntered = []
		self.testUserTestCases = collections.OrderedDict(zip(list(self.checkBoxInfo.keys()), [0]*len(self.checkBoxInfo)))
		for i in range(len(parent)):
			if (parent[i].cget("relief") == FLAT):
				parent[i].config(bg=self.background_Color, relief=GROOVE)#, highlightcolor="blue", highlightthickness=5)
				parent[i].pack(side=TOP, fill=X, anchor=NW)
				if i < 1:
					for j in list(self.checkBoxInfo.keys())[:4]:
						check = Checkbutton(parent[i], text=j, command=(lambda j=j: self.onPress(j)), font=(fontsize), bg=self.background_Color)
						check.pack(side=LEFT)
						check.deselect()
						self.checkButtonsEntered.append(check)
				else:
					for j in list(self.checkBoxInfo.keys())[4:]:
						check = Checkbutton(parent[i], text=j, command=(lambda j=j: self.onPress(j)), font=(fontsize), bg=self.background_Color)
						check.pack(side=LEFT)
						check.deselect()
						self.checkButtonsEntered.append(check)

		self.checkEnter = tkinter.Button(self.rootOfEnterButton, text="OK", font=('','10','bold'), command=self.onOKPress, width=self.EnterButton_width, height=self.EnterButton_Height, relief=RAISED)
		self.checkEnter.pack(side=TOP, anchor=NE)

	def createTitle_Frame(self, arg, txt, fontSize):
		# print(arg.cget("relief"))
		if (arg.cget("relief") == FLAT):
			# print(1)
			title_Frame = tkinter.Frame(arg,bg=self.background_Color)#, highlightcolor="blue", highlightthickness=7)
			title_Frame.grid(sticky=W)
			title_Label = tkinter.Label(title_Frame, bg=self.background_Color, text=txt, font=(fontSize), anchor='w')
			title_Label.grid(sticky=W)

	def createErrorLabel(self):
		for arg in self.testInfoFrames:
			if (arg.cget("relief") == FLAT):
				self.createExtraBlankRow_Frame(arg, 1)
				arg.Error_Frame = tkinter.Frame(arg, bg=self.background_Color)#, highlightcolor="blue", highlightthickness=7)
				arg.Error_Frame.pack(side=self.errorFrame_PackSide, anchor= self.errorFrame_Anchor)
				arg.Error_Label = tkinter.Label(arg.Error_Frame, text=" ", fg='red', bg=self.background_Color)
				arg.Error_Label.pack(side=TOP, anchor=NW, fill=self.errorLabel_PackFill)

	def createRadioButton(self, arg, labelText, radioList, valueList):
		if (arg.cget("relief") == FLAT):				
			radioRow_Frame = Frame(arg, bg=self.background_Color, width=self.radioButtonFrame_Width)#, highlightcolor="blue", highlightthickness=7)#, width=self.OPLInfoWidth_Width)
			radioRow_Frame.pack(side=self.radioButtonFrame_PackSide, anchor = self.radioButtonFrame_Anchor)#side=self.radioButton_FrameSide)#, fill=X)
			radioLabel_Label = Label(radioRow_Frame, text=labelText, bg=self.background_Color, width=self.radioButtonLabel_Width)#, width=int(self.OPLInfoWidth_Width*0.4))
			radioLabel_Label.pack(side=LEFT, anchor='center')

			for radioText,valueText in zip(radioList, valueList):
				self.radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.URL, value=valueText, bg=self.background_Color, width=self.radioButton_Width)
				self.radioButton_Button.pack(side=LEFT, anchor=NW)
				self.radioButton_Button.deselect()

	def GetUserInputSendFunction(self):
		suite = unittest.TestSuite()
		if self.current_Button == "Login_Security":
			self.OPL_Input_Frame_Frame.config(relief=GROOVE)
			self.OPLGetUserInputSendFunction()
			if (self.OPL_Input_Frame_Frame.cget("relief") == RAISED and self.radioButtonCheck == True):
				self.OPL_Input_Frame_Frame.Error_Label.pack_forget()
				print("self.testToRun: ", self.testToRun)
				for i in self.testToRun:
					print("i: ", i)
					suite.addTests(unittest.makeSuite(i))
				self.runTest(suite)
		elif self.current_Button == "Order New Report":
			self.OPL_Input_Frame_Frame.config(relief=GROOVE)
			self.Custom_Input_Frame_Frame.config(relief=GROOVE)
			self.OPLGetUserInputSendFunction()
			self.CustomGetUserInputSendFunction()
			if (self.OPL_Input_Frame_Frame.cget("relief") == RAISED and self.Custom_Input_Frame_Frame.cget("relief") == RAISED and self.radioButtonCheck == True):
				self.OPL_Input_Frame_Frame.Error_Label.pack_forget()
				self.Custom_Input_Frame_Frame.Error_Label.pack_forget()
				# print("self.testToRun: ", self.testToRun)
				for i in self.testToRun:
					# print("i: ", i)
					suite.addTests(unittest.makeSuite(i))
				self.runTest(suite)

		# if whichTestToRun is "OPL" or whichTestToRun is "ONR":
		# 	whichFrame.config(relief=GROOVE)
		# 	self.OPLGetUserInputSendFunction()
		# 	# self.CustomGetUserInputSendFunction()

		# 	if (whichFrame.cget("relief") == RAISED and self.radioButtonCheck == True):
		# 		# get rid of error. This means everything is fine.
		# 		for i in whichFrame:
		# 			i.pack_forget()
		# 		self.current_Test = Test_Order1.Test_Order1
		# 		# IF EVERYTHING IS FINE THEN RUN THE TEST!!!
		# 		self.runTest()

		# elif (whichTestToRun in self.testCases.keys()):
		# 	for i in self.testCases:
		# 		if self.testCases[i] == 1:
		# 			self.frame.config(relief=GROOVE)
			# self.OPLGetUserInputSendFunction()

	def OPLGetUserInputSendFunction(self):
		dictValue = []
		# First, check if self.URL gets either QA or Production. If it did not get anything, self.radioButtonCheck is False
		print("Which URL:", self.URL.get())
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
		Functions.OPLInfo = collections.OrderedDict(zip(list(self.whichInfoOPL.keys()), dictValue))
		print(Functions.OPLInfo)
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
			
	def userInputFrame(self):
		# arg.config(bg=self.background_Color)
		# arg.pack(side=self.OPLInputFrame_PackSide)#, fill=self.userInputFrame_PackFill)#, padx=self.betweeenFrame)
		for k in self.testInfoFrames:
			if (k.cget("relief") == FLAT):
				self.makeUserInputForm(k)
				if self.frameType is not "ONR":
					self.frameType = "ONR"
					self.whichInfoCustom = ["First Name","Last Name", "Email Address", "Job Title", "PO Box", "Cost Center", "Message to Consultant", "Message to Assessee", "Also Notify", "New Tag Name"]

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
				userInputEntry_Entry.pack(side=RIGHT)#, fill=X)#expand=self.OPLInputFrameEntry_Expand)#
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
				userInputEntry_Entry.pack(side=RIGHT)#, expand=self.OPLInputFrameEntry_Expand)#, fill=X)
				self.CustomInfo.append(userInputEntry_Entry)
			arg.config(relief=GROOVE)

	def createExtraBlankRow_Frame(self, arg, howMany):
		if (arg.cget("relief") == FLAT):
			for i in range(howMany):
				self.extraRow_Label = Label(arg, bg=self.background_Color, text=" ")
				self.extraRow_Label.pack(side=self.extraLabel_PackSide, fill=self.extraLabel_PackFill)

	def createSaveButton(self, arg, buttonText, commandMethod):
		if (arg.cget("relief") == GROOVE): 
			self.userInputEnterRow_Frame = tkinter.Frame(arg, bg=self.background_Color)#, highlightcolor="blue", highlightthickness=7)
			self.userInputEnterRow_Frame.pack(side=TOP, anchor='w', ipadx=self.saveButton_ipadx)
			UserInputEnterButton = tkinter.Button(self.userInputEnterRow_Frame, text=buttonText, command=commandMethod, relief=RAISED)
			UserInputEnterButton.pack(side=self.saveButton_PackSide, anchor=self.saveButton_Anchor)
			arg.config(relief=RIDGE)

	def conSoleFrame(self, frames):
		self.consoleTab = {}
		for arg, i in zip(frames, self.testUserTestCases.keys()):
			arg.config(bg=self.background_Color)#, highlightcolor="blue", highlightthickness=1)
			arg.pack(padx=self.consolePack_padx, side=self.consoleFrame_PackSide, anchor=self.consoleFrame_Anchor, fill=self.consoleFrame_PackFill, expand=self.consoleFrame_PackExpand)
			# if there are more than two buttons selected == need to display more than two consoles, then enlarge the frame
			if self.current_Button == "Order New Report":
				self.myParent.geometry(self.mainFrame_Dimension)
			# elif self.current_Button == "Hiring Status":
			# 	self.myParent.geometry(self.HiringStatus_Dimension)
				
			else:
				if len(frames) == 1:
					self.myParent.geometry(self.max1_Dimension)
				# if there are more than one buttons selected == need to display more than one console, then give title to each of console frame
				elif len(frames) == 2:
					self.myParent.geometry(self.max2_Dimension)
				elif len(frames) == 3:
					self.myParent.geometry(self.max3_Dimension)
				elif len(frames) == 4:
					self.myParent.geometry(self.max4_Dimension)
				elif len(frames) == 5:
					self.myParent.geometry(self.max2_Dimension)

			if len(frames) > 1:
				self.createTitle_Frame(arg, i, 20)
			if (arg.cget("relief") == FLAT):
				# self.consoleTab[i]
				self.bar_TabBar = Tab.TabBar(arg, "Evaluation", i)
				tab1_Tab = Tab.Tab(arg, "Evaluation")
				tab2_Tab = Tab.Tab(arg, "Console")
				# self.consoleTab[i] = [tab1_Tab, tab2_Tab]
				self.bar_TabBar.add(tab1_Tab)
				self.bar_TabBar.add(tab2_Tab)
				self.bar_TabBar.show()

				arg.config(relief=GROOVE)
		# print(self.consoleTab)
		# self.consoleTab["Password Recovery"][0].insert(INSERT, "  " + "This is stupid" + "\n\n")
		# print("First One: ", self.consoleTab["Password Recovery"][0])
		# print("Second One: ", self.consoleTab["Password Recovery"][1])
		# self.consoleTab["Password Recovery"][0].insert(INSERT, "  " + "This is stupid" + "\n\n")

	def runTest(self, suite):
		result = unittest.TextTestRunner(verbosity=2).run(suite)

if Functions.GUImainFrame == None:
	Functions.GUImainFrame = Tk()
	Functions.GUIdisplay = GUItkinter(Functions.GUImainFrame)
	Functions.GUImainFrame.mainloop()