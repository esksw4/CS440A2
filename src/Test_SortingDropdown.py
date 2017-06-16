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

class Test_SortingDropdown(unittest.TestCase):
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

  def test_sortingDropdown(self):
    import Functions
    import automatedSmokeTest
    # checkNumError = 0
    Functions.GUIdisplay.testName = "Sorting Dropdown"
    driver = Functions.Functions.hiringOPL(self)

    whatToSort = 'Name'
    sortColumn = 2
    # print('1. Sort by', whatToSort)
    xpath = str("//table[@class='table cal-datagrid dataTable no-footer']/thead/tr/th[%d]" %sortColumn)

    automatedSmokeTest.GUIFunctions.outputDisplayConsole("1. Sort by %s" %whatToSort, Functions.GUIdisplay.testName,'display')

    driver.find_element_by_xpath(xpath).click()
    time1.sleep(2)
    tableText = driver.find_element_by_id("hiring-status-table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(2)
    sortingWorks = Functions.Functions.sortingCheck(driver, whatToSort, sortColumn, listAssessee)
    if sortingWorks == 0:
      automatedSmokeTest.GUIFunctions.outputDisplayConsole("The %s button does not sort the list by %s." %(whatToSort, whatToSort), Functions.GUIdisplay.testName,'se')
    else:
      automatedSmokeTest.GUIFunctions.outputDisplayConsole("The %s button correctly sorts the list by %s." %(whatToSort, whatToSort), Functions.GUIdisplay.testName,'display')
      whatToSort = 'Date'
      sortColumn = 4
      # print('2. Sort by', whatToSort)
      xpath = str("//table[@class='table cal-datagrid dataTable no-footer']/thead/tr/th[%d]" %sortColumn)

      automatedSmokeTest.GUIFunctions.outputDisplayConsole("2. Sort by %s" %whatToSort, Functions.GUIdisplay.testName,'display')

      driver.find_element_by_xpath(xpath).click()
      time1.sleep(2)
      tableText = driver.find_element_by_id("hiring-status-table_info").text
      systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
      time1.sleep(2)
      sortingWorks = Functions.Functions.sortingCheck(driver, whatToSort,  sortColumn, listAssessee)
      if sortingWorks == 0:
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("The %s button does not sort the list by %s." %(whatToSort, whatToSort), Functions.GUIdisplay.testName,'se')
      else:
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("The %s button correctly sorts the list by %s." %(whatToSort, whatToSort), Functions.GUIdisplay.testName,'display')
        whatToSort = 'Supervisor'
        sortColumn = 3
        xpath = str("//table[@class='table cal-datagrid dataTable no-footer']/thead/tr/th[%d]" %sortColumn)

        automatedSmokeTest.GUIFunctions.outputDisplayConsole("3. Sort by %s" %whatToSort, Functions.GUIdisplay.testName,'display')

        driver.find_element_by_xpath(xpath).click()
        time1.sleep(2)
        tableText = driver.find_element_by_id("hiring-status-table_info").text
        systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
        time1.sleep(5)
        sortingWorks = Functions.Functions.sortingCheck(driver, whatToSort,  sortColumn, listAssessee)
        if sortingWorks == 0:
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("The %s button does not sort the list by %s." %(whatToSort, whatToSort), Functions.GUIdisplay.testName,'se')
        else:
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("The list is correctly sorted by the each button.", Functions.GUIdisplay.testName,'s')
if __name__ == "__main__":
    unittest.main(warnings ='ignore')

    str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]" %(i,sortColumn))