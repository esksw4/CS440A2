# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
import re, string, sys
import colorama
import time as time1

# from tkinter import *
# import tkinter
# import tkinter.messagebox as msg
# import tkinter.simpledialog as dlg

class Functions():
	global timeAfterLogin
	timeAfterLogin = 7

	def checkForError(checkNumError, testName):
		colorama.init(autoreset=True)
		print(colorama.Fore.BLACK + colorama.Back.YELLOW + str(testName) + " with " + str(checkNumError) + " error(s).")

	def hiringOPL(self, testName):
		print('Testing ', testName)
		driver = self.driver
		driver.get(self.base_url)
		# type | id=user_password | 1234567899s
		driver.find_element_by_id("user_password").clear()
		driver.find_element_by_id("user_password").send_keys("123456789")
		# type | id=user_email | ekim+abc1@calipercorp.com
		driver.find_element_by_id("user_email").clear()
		driver.find_element_by_id("user_email").send_keys("ekim+abc1@calipercorp.com")
		# click | name=commit |
		driver.find_element_by_id("login-btn").click()
		time1.sleep(timeAfterLogin)

		driver.find_element_by_link_text("Hiring Status").click()
		time1.sleep(2)

		return driver

	def hiringButtonCheck(checkNumError, filterStatus):
		#print("checkNumError: " + str(checkNumError) + ",  FilterStatsu: " + filterStatus)
		if checkNumError > 0:
			colorama.init(autoreset=True)
			print(colorama.Fore.RED + filterStatus + str(" button doesn't work"))

	def hiringEmptyCheck(varToCheckIfEmpty,checkNumError):
		if varToCheckIfEmpty == []:
			checkNumError += 1
		
		return checkNumError

	def OPL(self, testName):
		print('Testing ', testName)
		driver = self.driver
		
		driver.get("http://portal.qa.calipercorp.com/users/sign_in")
		driver.find_element_by_id("user_email").clear()
		driver.find_element_by_id("user_email").send_keys("ekim+ABC1@calipercorp.com")
		# type User Password
		driver.find_element_by_id("user_password").clear()
		driver.find_element_by_id("user_password").send_keys("123456789")
		# click Ente
		driver.find_element_by_id("login-btn").click()
		time1.sleep(timeAfterLogin)

		return driver

	def userInputAssign(userInfo):
		global firstName, lastName, emailAddress
		global poBox, costCenter, coLor, positionNum, favNum, msgConsultant, msgPersonalized
		global alsoNotify

		firstName = userInfo[0]
		lastName = userInfo[1]
		emailAddress = userInfo[2]
		poBox = userInfo[3]
		costCenter = userInfo[4]
		coLor = userInfo[5]
		positionNum = userInfo[6]
		favNum = userInfo[7]
		msgConsultant = userInfo[8]
		msgPersonalized = userInfo[9]

		alsoNotify = "Young Kim"

		if firstName == "" or lastName == "" or emailAddress == "" or poBox == "" or costCenter == "" or coLor == "" or positionNum == "" or favNum == "" or msgConsultant == "" or msgPersonalized == "":
			return False
		return True





	#def orderReportUserheck(driver,):