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

class Test_FilterbyDateRange(unittest.TestCase):
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

	def test_FilterbyDateRange(self):
	    checkNumError = 0
	    testName = "Filter by Date Range"
	    driver = Functions.Functions.hiringOPL(self, testName)

	    ############################################## testing 'Last 7 Days'
	    buttonStatus = 'Last 7 Days'
	    print('1. ' + buttonStatus)
	    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
	    # click "last 7 days"
	    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[1]").text
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[1]").click()

	    time1.sleep(7)
	    tableText = driver.find_element_by_id("table_info").text
	    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

	    # check if filter has the specific duration of the month
	    # click "select Date Range"
	    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
	    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates,checkNumError)

	    tothis = date.today()
	    # calculate what would be the beginning range to compare with
	    fromthis = tothis + timedelta(-6)
	    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
	    if checkEmpty == False:
	      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
	      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

	    #############################################testing 'Last 30 Days'
	    buttonStatus = 'Last 30 Days'
	    print('2. ' + buttonStatus)
	    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
	    # click "last 30 days"
	    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[2]").text
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[2]").click()

	    time1.sleep(7)
	    tableText = driver.find_element_by_id("table_info").text
	    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

	    # check if filter has the specific duration of the month
	    # click "select Date Range"
	    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
	    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates,checkNumError)

	    tothis = date.today()
	    # calculate what would be the beginning range to compare with
	    fromthis = tothis + timedelta(-29)
	    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
	    if checkEmpty == False:
	      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
	      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

	    ############################################## testing 'this Month'
	    buttonStatus = 'This Month'
	    print('3. ' + buttonStatus)
	    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
	    # click "Last 6 Months"
	    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[3]").text
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[3]").click()

	    time1.sleep(7)
	    tableText = driver.find_element_by_id("table_info").text
	    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

	    # check if filter has the specific duration of the month
	    # click "select Date Range"
	    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
	    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates, checkNumError)

	    # end date range to compare with
	    tothis = date.today()
	    # calculate what would be the beginning range to compare with
	    fromthis1 = str(tothis.month)
	    fromthis2 = str(1)
	    fromthis3 = str(tothis.year)
	    fromthis = fromthis1 + fromthis2 + fromthis3
	    # put it as date form
	    fromthis = datetime.strptime(fromthis, '%m%d%Y')
	    fromthis = fromthis.date()
	    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
	    if checkEmpty == False:
	      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
	      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

	    ############################################## testing 'last 6 months'
	    buttonStatus = 'Last 6 months'
	    print('4. ' + buttonStatus)

	    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
	    # click "Last 6 Months"
	    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[4]").text
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[4]").click()

	    time1.sleep(7)
	    tableText = driver.find_element_by_id("table_info").text
	    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

	    # check if filter has the specific duration of the month
	    # click "select Date Range"
	    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
	    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates, checkNumError)

	    # end date range to compare with
	    tothis = date.today()
	    # calculate what would be the beginning range to compare with
	    if tothis.month < 6:
	      fromthis1 = str(tothis.month + 12 - 5)
	      fromthis2 = str(1)
	      fromthis3 = str(tothis.year - 1)
	    else:
	      fromthis1 = str(tothis.month - 5)
	      fromthis2 = str(1)
	      fromthis3 = str(tothis.year)

	    fromthis = fromthis1 + fromthis2 + fromthis3
	    # put it as date form
	    fromthis = datetime.strptime(fromthis, '%m%d%Y')
	    fromthis = fromthis.date()
	    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
	    if checkEmpty == False:
	      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
	      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

	    ############################################# testing 'Custom Range'
	    buttonStatus = 'Custom Range'
	    print('5. ' + buttonStatus)
	    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
	    # click "Custom Range"
	    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[6]").text
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[6]").click()

	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_start_input']/input[@class='input-mini']").clear()
	    time1.sleep(2)
	    fromthis = "01/05/2016"
	    tothis = "08/05/2016"
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_start_input']/input[@class='input-mini']").send_keys(fromthis)
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_start_input']/input[@class='input-mini']").send_keys(Keys.TAB)
	    time1.sleep(2)

	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_end_input']/input[@class='input-mini']").clear()
	    time1.sleep(1)
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_end_input']/input[@class='input-mini']").send_keys(tothis)
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_end_input']/input[@class='input-mini']").send_keys(Keys.TAB)
	    time1.sleep(1)
	    # click apply
	    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/button[1]").click()
	    # check if filter has the specific duration of the month
	    # click "select Date Range"
	    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
	    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates, checkNumError)

	    # change RANGE DATES to date form
	    fromthis = datetime.strptime(fromthis, '%m/%d/%Y')
	    fromthis = fromthis.date()
	    tothis = datetime.strptime(tothis, '%m/%d/%Y')
	    tothis = tothis.date()
	    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')

	    if checkEmpty == False:
	      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
	      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

	    Functions.Functions.checkForError(checkNumError, testName)


if __name__ == "__main__":
    unittest.main(warnings ='ignore')