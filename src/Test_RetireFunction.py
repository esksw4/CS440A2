from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import Functions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, string, sys
import time as time1
from datetime import date
from datetime import time 
from datetime import datetime
from datetime import timedelta

class Test_RetireFunction(unittest.TestCase):
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
	# def test_RetireSomeone(self):
	#     checkNumError = 0
	#     testName = "Retire"
	#     driver = Functions.Functions.hiringOPL(self, testName)
	#     # filter by Hired to only view Hired assesseess
	#     driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[2]/label[1]").click()
	#     time1.sleep(2)
	#     # how many assessees are in list?
	#     tableText = driver.find_element_by_id("table_info").text
	#     systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
	#     i = 1

	#     # open 1st assessee  frame
	#     assesseeName = driver.find_element_by_xpath("//tbody/tr[%d]/td[2]/div/div" % (i)).text
	#     driver.find_element_by_xpath("//tbody/tr[%d]//div[@class='btn-group']/a" % (i)).click()
	#     time1.sleep(1)
	#     driver.find_element_by_xpath("//ul[@class='dropdown-menu']//a").click()
	#     time1.sleep(1)

	#     leavingDate = driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[4]/div[1]/div[1]").text

	#     # while the leaving date is Not empty, go to next assessee and do it.
	#     while leavingDate != "":
	# 		# click cancel
	# 		driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//div[@class='modal-footer']/button[@id='hiringStatusCancelButton']").click()
	# 		time1.sleep(2)
	# 		# proceed to next assessee
	# 		i += 1
	# 		# save next assesseeName
	# 		assesseeName = driver.find_element_by_xpath("//tbody/tr[%d]/td[2]/div/div" % (i)).text
	# 		# open assessee's frame
	# 		driver.find_element_by_xpath("//tbody/tr[%d]//div[@class='btn-group']/a" % (i)).click()
	# 		driver.find_element_by_xpath("//tbody/tr[%d]//ul[@class='dropdown-menu']//a" % (i)).click()
	# 		time1.sleep(1)
	# 		leavingDate = driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[4]/div[1]/div[1]").text
	# 		# if i is out of range in list, then click next list and reset i as 1.
	# 		if i == listAssessee:
	# 			driver.find_element_by_xpath("//div[@id='table_paginate']//li[@class='next']/a[1]").click()
	# 		i = 1
	    
	#     time1.sleep(1)  
	#     # if assesse is NOT retired,click Leaving Date Calendar
	#     driver.find_element_by_xpath("//div[@id='separation_date_row']//div[@id='separation_date']").click()
	#     time1.sleep(2)
	#     # click 2nd Wednesday of the month
	#     driver.find_element_by_xpath("//body/div[5]//table[@class='table-condensed']/tbody/tr[2]/td[4]").click()
	#     time1.sleep(2)
	#     # click voluntary
	#     driver.find_element_by_xpath("//div[@id='leaving_reason_row']/div[1]/div[2]/div[1]").click()
	#     # click save
	#     driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//div[@class='modal-footer']/button[1]").click()
	#     time1.sleep(1)

	#     # # check if the date is there.
	#     # checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[4]/div[1]/div[1]/div[1]").text
	#     # if checkDates == []:
	#     #    checkNumError += 1
	#     # time1.sleep(1)

	#     print("Check Hired data in Pivotal if " + assesseeName + " is retired or not.")
	#     Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')