# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import Functions

# def doTest():
class Test_Login_Logout(unittest.TestCase):
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

  def test_log_inlog_out(self):
    checkNumError = 0
    testName = "'Login and Logout'"
    driver = Functions.Functions.OPL(self, testName)
    # click | link=Log out |
    driver.find_element_by_link_text("Log out").click()
    # verifyTitle | exact:Caliper: Login |
    try:
      if driver.current_url != Ori_correct_PortalLink:
        print(driver.current_url)
        print(Ori_correct_PortalLink)
        checkNumError += 1
    except AssertionError as e:
      self.verificationErrors.append(str(e))

    driver.quit()
    Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')