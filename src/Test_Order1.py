from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, string, sys
import time as time1

class Test_Order1(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e:
			return False
		return True

	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		except NoAlertPresentException as e:
			return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

	def test_order_Exist_Job_Title(self):
		# Existing Title
		# New Assessee
		# Added Also Notify Contact
		# New TAG
		# NO PROCTORED:: I THINK,.,.,    
		import Functions
		# import automatedApplicaitonGUI

		checkNumError = 0
		testName = "'Order for existing job title, new assessee, also notify with new tag.'"
		driver = Functions.Functions.OPL(self, testName)
		#driver.get(self.base_url + "/")

		# print("Print result with key called first Name: ". Functions.result.keys() == "firstName")

		# click | id=dashboardOrderReport |
		driver.find_element_by_id("dashboardOrderReport").click()
		time1.sleep(2)

		# Enter existing JobTitle
		driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys(Functions.CustomInfo['Job Title'])
		time1.sleep(1)
		driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys(Keys.ARROW_DOWN)
		driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys(Keys.ENTER)
		time1.sleep(1)

		# check if job title is inputted by checking visibility of alsoNotify field.
		alsoNotifyLocation = "//div[@id='deliverToRowDiv']"
		checkAlsoNotify = driver.find_element_by_xpath(alsoNotifyLocation).get_attribute("style")
		# print(checkAlsoNotify)
		if checkAlsoNotify == "display: block;":
			time1.sleep(2)
			alsoNotifyLocation = "//div[@id='deliverToDiv']/div[1]/span[1]/input[1]"
			driver.find_element_by_xpath(alsoNotifyLocation).send_keys(Functions.CustomInfo['Also Notify'])
			time1.sleep(2)
			driver.find_element_by_xpath(alsoNotifyLocation).send_keys(Keys.ARROW_DOWN)
			time1.sleep(2)
			driver.find_element_by_xpath(alsoNotifyLocation).send_keys(Keys.ENTER)
			time1.sleep(2)
			# print(Test_Order1.is_element_present(self, By.XPATH, "//div[@id='deliverToDiv']/div[1]/div[@class='token']"))
			if not Test_Order1.is_element_present(self, By.XPATH, "//div[@id='deliverToDiv']/div[1]/div[@class='token']"):
				driver.quit()
				automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Input Error: Please enter valid Name for 'Also Notify'.", 'ie')
			else:
				Functions.CustomInfo['Also Notify'] = driver.find_element_by_xpath("//div[@id='deliverToDiv']/div[1]/div[1]/span[1]").text
				# print("Functions.CustomInfo['Also Notify']: ", Functions.CustomInfo['Also Notify'])
		else:
			driver.quit()
			automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Input Error: The job title, you entered is not available; therefore, 'Also Notify' is not available. Please enter correct existing job title.", 'ie')

		# Enter new Assessee
		driver.find_element_by_id('assesseeBtn').click()
		time1.sleep(2)

		driver.find_element_by_id('assesseeFirstName').send_keys(Functions.CustomInfo['First Name'])
		driver.find_element_by_id('assesseeLastName').send_keys(Functions.CustomInfo['Last Name'])
		driver.find_element_by_id('assesseeEmail').send_keys(Functions.CustomInfo['Email Address'])
		driver.find_element_by_xpath("//div[@class='row assesseePoNumberRow']/div[2]/input[@id='assesseePoNumber']").send_keys(Functions.CustomInfo['PO Box'])
		driver.find_element_by_xpath("//div[@class='row assesseeCostCenterRow']/div[2]/input[@id='assesseeCostCenter']").send_keys(Functions.CustomInfo['Cost Center'])
		driver.find_element_by_xpath("//div[@class='row assesseeCustomFieldRow1']/div[2]/textarea[@id='assesseeCustomField1']").send_keys(Functions.CustomInfo['Color'])
		driver.find_element_by_xpath("//div[@class='row assesseeCustomFieldRow2']/div[2]/textarea[@id='assesseeCustomField2']").send_keys(Functions.CustomInfo['Position Number'])
		driver.find_element_by_xpath("//div[@class='row assesseeCustomFieldRow3']/div[2]/textarea[@id='assesseeCustomField3']").send_keys(Functions.CustomInfo['Favorite Number'])
		driver.find_element_by_xpath("//div[@class='row assesseeSpecialInstructionsRow']/div[2]/textarea[@id='assesseeSpecialInstructions']").send_keys(Functions.CustomInfo['Message to Consultant'])
		driver.find_element_by_xpath("//div[@class='row assesseeEmailMessageRow']/div[2]/textarea[@id='assesseeEmailMessage']").send_keys(Functions.CustomInfo['Message to Assessee'])
		# click save
		driver.find_element_by_id('assesseeSaveButton').click()
		time1.sleep(2)

		#check if Error occurs
		checkErrorMsg = Test_Order1.is_element_present(self, By.CLASS_NAME, "alert.alert-error.alert-dismissable")
		# print("ErrorMessage Exists? ", checkErrorMessage)
		# according to error occurs, display error message in the tkinter file.
		if (checkErrorMsg == True):
			driver.quit()
			# Functions.Functions.orderNewStopTest()
			automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Input Error: Please enter valid additional information. Cannot process with given input.", 'ie')
			# print(GUItkinter.py)
			# from GUItkinter import inputFrame
			# GUItkinter.getUserInputSendFunction

		# Click Prodctored Assessment
		try: 
			driver.find_element_by_xpath("//div[@id='newOrderForm']/div[6]/div[1]/div[1]/input[@id='proctored']").click()
			driver.find_element_by_xpath("//div[@id='sendToMeDiv']/input[@id='sendToMe']").click()
			#Click "Place Order"
		except:
			# if any of proctored checkbox is not working, then display the error message on the GUI
			automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Proctored checkbox cannot be pressed automatically. Please manually test the proctored checkbox", 'p')

		# Click Tags -> Edit
		time1.sleep(2)
		driver.find_element_by_id("allAssesseeGroupsBtn").click()
		time1.sleep(2)
		driver.find_element_by_id("aga_assesseeGroupName").send_keys(Functions.CustomInfo['New Tag Name'])
		time1.sleep(2)
		driver.find_element_by_id("aga_assesseeGroupDesc").send_keys('Smoke Test')
		time1.sleep(2)
		driver.find_element_by_id("assesseeGroupAssesseeSaveBtn").click()
		time1.sleep(2)

		try:
			# print(driver.find_element_by_class_name("alert.alert-error.alert-dismissable").text)
			if Test_Order1.is_element_present(self, By.CLASS_NAME, "alert.alert-error.alert-dismissable"):
				driver.quit()
				automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Input Error: Please choose different Tag Name. That Tag name exists in the system.", 'ie')
		except:
			try:
				time1.sleep(2)
				# print(driver.find_element_by_class_name("alert alert-info.alert-dismissable").text)
				if Test_Order1.is_element_present(self, By.CLASS_NAME, "alert.alert-info.alert-dismissable"):
					pass
			except:
				automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Tag is not created. Please check 'Creat New Tag' functionality.", 'se')

		# click "Place Order"
		time1.sleep(4)
		driver.find_element_by_id("newOrderBtn").click()
		time1.sleep(2)

		# if there is any error msg during creating order, quit the test and display error message to GUI
		# if not, click OK on order confirmation dlg box
		# then test the "Copy Assessment URL" -> by check the same email address and "register" page
		# if they are all same and good to go, cancel the order & check if its cancelled succesffully. 
		checkErrorMsg = Test_Order1.is_element_present(self, By.CLASS_NAME, "alert.alert-error.alert-dismissable")

		if checkErrorMsg == True:
			driver.quit()
			automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Input Error: Please choose different email for assessee. That email address already exists in the system.", 'ie')

		else:
		  	#click OK on order confirmation dlg box
			driver.find_element_by_id("okButton").click()
			time1.sleep(5)

			if 'reports' in driver.current_url:
				# print("1")
				fullName = Functions.CustomInfo['First Name'] + " " + Functions.CustomInfo['Last Name']
				tableText = driver.find_element_by_id("table_info").text
				systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
				whichRow = Functions.Functions.findWhichRow(driver,"Name", fullName, listAssessee)

				if whichRow != 9999:
					# print("3")
					# click the dropdown
					driver.find_element_by_xpath("//tbody/tr[%d]/td[1]/div[1]/a[1]" % whichRow).click()
					time1.sleep(1)
					# test "Copy assessment URL"
					assessmentURL =  driver.find_element_by_xpath("//tbody/tr[%d]/td[1]/div[1]/ul[1]/li[5]" % whichRow).get_attribute('data-clipboard-text')
					# click "Copy assessment URL"
					driver.find_element_by_xpath("//tbody/tr[%d]/td[1]/div[1]/ul[1]/li[5]" % whichRow).click()
					tab0 = driver.window_handles[0]
					driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'T')
					tab1 = driver.window_handles[1]
					driver.switch_to.window(tab1)
					driver.get(assessmentURL)
					time1.sleep(2)
					registerCheck = driver.find_element_by_xpath("//div[@class='container container-min-height']/div[2]/legend[1]/h4[1]").text
					emailCheck =  driver.find_element_by_xpath("//input[@id='assessee_email']").get_attribute('value')

					if len(emailCheck) != len(Functions.CustomInfo['Email Address']):
						Functions.CustomInfo['Email Address'] = Functions.CustomInfo['Email Address'][:len(emailCheck)]
					# print(Functions.CustomInfo['Email Address'])

					if "Register" == registerCheck and Functions.CustomInfo['Email Address'] == emailCheck:
						# print("4")
						# print(registerCheck + ", " + emailCheck)

						driver.switch_to.window(tab0)
						driver.find_element_by_tag_name('body').click()
						# Cancel It
						driver.find_element_by_xpath("//tbody/tr[%d]/td[1]/div[1]/a[1]" % whichRow).click()
						time1.sleep(1)
						driver.find_element_by_xpath("//tbody/tr[%d]/td[1]/div[1]/ul[1]/li[3]" % whichRow).click()
						time1.sleep(1)
						driver.find_element_by_xpath("//div[@class='modal-dialog']/div[1]/div[3]/button[@id='cancelOrderBtn']").click()

						# print("5")
						checkConfirmationMessage = Test_Order1.is_element_present(self, By.CLASS_NAME, "alert.alert-success.alert-dismissable")
						# print(checkConfirmationMessage)

						if checkConfirmationMessage == True:
							# print("6")
							# print("Cancelled Succesfully")
							driver.close()
							automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("%s tested succesfully" %testName , 's')

						else:
							# print("7")
							# print("Cancellation Failed")
							automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Cancellation Failed" , 'se')
					else:
						# print("8")
						# print(len(Functions.CustomInfo['Email Address']))
						# print(Functions.CustomInfo['Email Address'])
						# print(len(emailCheck))
						# print(emailCheck + " 123124123")
						automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Register page email address is not same as user input email address", 'se')
						# print("Email address is not same as user input email address")
				else:
					# print("9")
					automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("The name is not found from the report list", 'se')
					# print("Name does not match")

			else:
				# print("10")
				# print("The page is not directed to 'View Reports' page")
				automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("The page is not directed to 'View Reports' page" , 'se')

if __name__ == "__main__":
  unittest.main(warnings='ignore')