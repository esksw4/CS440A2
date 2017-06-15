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

class Test_FilterBySupervisor(unittest.TestCase):
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

  # def test_FilterBySupervisor(self):
  #   ##PUT THE code to verify total number of entries with summation of each status entries
  #   checkNumError = 0
  #   testName = "Filter By Supervisor"
  #   driver = Functions.Functions.hiringOPL(self, testName)

  #   supervisorname = ["Young Kim", "Kendra Barnett", "Marley Bee"]

  #   for i in range(0,3):
  #     driver.find_element_by_id("supervisorSearch-tokenfield").send_keys(supervisorname[i])
  #     time1.sleep(1)
  #     driver.find_element_by_id("supervisorSearch-tokenfield").send_keys(Keys.ARROW_DOWN)
  #     driver.find_element_by_id("supervisorSearch-tokenfield").send_keys(Keys.ENTER)
  #     time1.sleep(2)

  #     tableText = driver.find_element_by_id("table_info").text
  #     systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

  #     str1 = str("//tbody/tr[")
  #     str3 = str("]/td[3]//span[@class='dt-supervisor-name']")

  #     for j in range(1, listAssessee+1):
  #       str2 = str(j)
  #       str_element = str1 + str2 + str3
  #       check = driver.find_element_by_xpath(str_element).text
  #       if check != supervisorname[i]:
  #           checkNumError += 1
  #     driver.find_element_by_xpath("//div[@class='input-group']//div//div/a[@class ='close']").click()
  #   time1.sleep(1)

  #   Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')