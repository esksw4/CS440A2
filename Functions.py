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

class Functions():# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import Functions

class DashBoardPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://portal.qa.calipercorp.com/users/sign_in"
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

    def test_switch_different_language(self):
        checkNumError = 0
        testName = "'Switch Different language'"
        driver = Functions.Functions.OPL(self, testName)

        driver.find_element_by_id("localeSelector").click()
        driver.find_element_by_link_text("Deutsch - Deutschland").click()
        time.sleep(2)
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "Assessment einrichten/ Bericht anfordern":
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=English - UK |
        driver.find_element_by_link_text("English - UK").click()
        time.sleep(2)
        # assertText | css=#dashboard-graph > svg | exact:Created with Raphaël 2.1.216%Technician11%QA engineer10%Technician_SimpleChinese8%Customer Service Representative8%Management CPRJob Title Distribution (Top 5)*
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "Order a Report/Assessment":
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=日本語 - 日本 |
        driver.find_element_by_link_text(u"日本語 - 日本").click()
        time.sleep(2)
        # assertText | css=#dashboard-graph > svg | exact:Created with Raphaël 2.1.216%Technician11%QA engineer10%Technician_SimpleChinese8%Customer Service Representative8%Management CPR職種の分布（トップ5）*
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "受検登録とレポートオーダー":
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=한국어 - 한국 |
        driver.find_element_by_link_text(u"한국어 - 한국").click()
        time.sleep(2)
        # assertText | css=#dashboard-graph > svg | exact:Created with Raphaël 2.1.216%Technician11%QA engineer10%Technician_SimpleChinese8%Customer Service Representative8%Management CPR직위 분포(상위 5)*
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "보고서/평가 주문":
          print("Korean")
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=English - US |
        driver.find_element_by_link_text("English - US").click()
        time.sleep(2)
        # assertText | css=svg | Created with Raphaël 2.1.220Pending Assessments
        check = driver.find_element_by_id("localeSelector").text
        if check != "English - US":
          checkNumError += 1

        Functions.Functions.checkForError(checkNumError, testName)

    def test_does_ordera_report_work(self):
        checkNumError = 0
        testName = "'Order a Report'"
        driver = Functions.Functions.OPL(self, testName)
        # open | / |
        driver.get(self.base_url + "/")
        # click | id=dashboardOrderReport |
        driver.find_element_by_id("dashboardOrderReport").click()
        time.sleep(2)
        check = driver.title
        if check != "Caliper: Order Reports/Assessments":
          checkNumError += 1
        # click | link=Caliper |
        driver.find_element_by_link_text("Caliper").click()

        Functions.Functions.checkForError(checkNumError, testName)

    def test_view_a_report(self):
        checkNumError = 0
        testName = "'View a Report'"
        driver = Functions.Functions.OPL(self, testName)

        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        check = driver.title
        if check != "Caliper: Reports":
          checkNumError += 1

        driver.find_element_by_link_text("Caliper").click()
        time.sleep(2)
        # click 1st report to see
        assesseeName = driver.find_element_by_xpath("//div[@class='dashboard-orders']/div[1]/div[2]/a[1]").text
        assesseeName = assesseeName.split(" ")
        assesseeName = assesseeName[0] + "_" + assesseeName[1]
        driver.find_element_by_xpath("//div[@class='dashboard-orders']/div[1]/div[2]/a[1]").click()
        driver.switch_to.window(driver.window_handles[1])
        # FselectWindow | title=4207867 |
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | title=4207867 | ]]
        # assertTitle | 4207867 |
        time.sleep(2)
        #check = driver.current_url
        if assesseeName not in driver.current_url:
          checkNumError += 1

        driver.quit()
        Functions.Functions.checkForError(checkNumError, testName)

    def test_click_a_circle(self):
        checkNumError = 0
        testName = "'Click a circle'"
        driver = Functions.Functions.OPL(self, testName)
        #check = driver.title
        if "Dashboard" not in driver.title:
          checkNumError += 1

        # Click Pending Assessemtn circle
        driver.find_element_by_xpath("//div[@id='dashboard-chart1']").click()
        time.sleep(2)
        if "Caliper: Reports" not in driver.title:
          checkNumError += 1
        # Click Caliper logo
        driver.find_element_by_link_text("Caliper").click()
        time.sleep(2)

       
        # Click Pending Report circle
        driver.find_element_by_xpath("//div[@id='dashboard-chart2']").click()
        time.sleep(2)
        if "Caliper: Reports" not in driver.title:
          checkNumError += 1
        # Click Caliper logo
        driver.find_element_by_link_text("Caliper").click()
        time.sleep(2)
        
        # Click Completed Reports
        driver.find_element_by_xpath("//div[@id='dashboard-chart3']").click()
        time.sleep(2)
        if "Caliper: Reports" not in driver.title:
          checkNumError += 1
        # Click Caliper logo
        driver.find_element_by_link_text("Caliper").click()
        time.sleep(2)

        # Click Total Report
        driver.find_element_by_xpath("//div[@id='dashboard-chart4']").click()
        time.sleep(2)
        if "Caliper: Reports" not in driver.title:
          checkNumError += 1
        # Click Caliper logo
        driver.find_element_by_link_text("Caliper").click()
        time.sleep(2)
        if "Caliper: Dashboard" not in driver.title:
          checkNumError += 1

        Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')

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
		global lastName, emailAddress
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

		if firstname == "":
			return True
		return False





	#def orderReportUserheck(driver,):
