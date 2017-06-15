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

class Test_HiringFunction(unittest.TestCase):
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

  def test_HiringSomeone(self):
    checkNumError = 0
    testName = "Hire"
    driver = Functions.Functions.hiringOPL(self, testName)

    # filter by pending to only view pending assesseess
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    time1.sleep(2)
    driver.find_element_by_xpath("//div[@class='btn-group']/a").click()
    driver.find_element_by_xpath("//ul[@class='dropdown-menu']//a").click()
    time1.sleep(1)
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='container-fluid']/div[2]/div[1]/div[2]/div[1]").click()
    time1.sleep(1)
    originalHiredAlert = "Once changed to Hired, Hiring Status cannot be reverted back to Not Hired. Proceed with this change?"
    checkHiredAlert = driver.find_element_by_xpath("//div[@class='bootbox modal fade in']//div[@class='bootbox-body']").text
    
    # check if hiredalert was given
    if checkHiredAlert != originalHiredAlert:
      checkNumError += 1
      errorMessage = str("'Hired Alert' is different")
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + errorMessage)

    driver.find_element_by_xpath("//div[@class='bootbox modal fade in']//div[@class='modal-footer']/button[1]").click()
    time1.sleep(2)
    # click the calendar to put hired date
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[3]/div[1]/div[1]/div[1]").click()
    # click the number on the first row
    driver.find_element_by_xpath("//body/div[6]//table[@class='table-condensed']/tbody/tr[2]/td[2]").click()
    # put the supervisor name
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//input[@id='supervising_contact_id-tokenfield']").send_keys("Young Kim")
    time1.sleep(1)
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//input[@id='supervising_contact_id-tokenfield']").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//input[@id='supervising_contact_id-tokenfield']").send_keys(Keys.ENTER)
    # may we contact the supervisor? -> Yes
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='container-fluid']/div[12]/div[1]/label[1]/div[1]").click()
    # Save it
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//div[@class='modal-footer']/button[1]").click()
    time1.sleep(2)
    checkStatus = driver.find_element_by_xpath("//tbody/tr[1]/td[4]").text
    assesseeName = driver.find_element_by_xpath("//tbody/tr[1]/td[2]/div/div").text
    # check if hired assesseename has been removed from the list (remember that I clicked the "Pending")
    # if the assesseename is still on the list, it is the error
    
    # if checkStatus != 'Hired':
    #   checkNumError += 1
    #   colorama.init(autoreset=True)
    #   print(colorama.Fore.RED + 'Hired button does not work')

    print("Check Hired data in Pivotal if " + assesseeName + " has been marked as 'Hired' or not.")
    Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')