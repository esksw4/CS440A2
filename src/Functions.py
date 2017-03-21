import re, string, sys
import colorama
import time as time1

class Functions:
	global timeAfterLogin
	timeAfterLogin = 7

	global orderNewReportResult
	orderNewReportResult = {}

	global orderNewReportCheckErrorMsg
	orderNewReportCheckErrorMsg = None

	global GUIuserInputErrorRow_Frame
	GUIuserInputErrorRow_Frame = None

	global GUImainFrame
	GUImainFrame = None

	global GUIallFieldError
	GUIallFieldError = None


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
		driver.find_element_by_id("user_password").send_keys("12345678")
		# click Ente
		driver.find_element_by_id("login-btn").click()
		time1.sleep(timeAfterLogin)

		return driver
