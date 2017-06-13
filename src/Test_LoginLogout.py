# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, string, sys
import time as time1

# def doTest():
class Test_LoginLogout(unittest.TestCase):
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
    
    import Functions
    import automatedApplicaitonGUI
    testName = "Login Logout"
    driver = Functions.Functions.OPL(self, testName)
    time1.sleep(2)
    # click | link=Log out |
    driver.find_element_by_xpath("//div[@id='main-content']/div[1]/div[1]/div[2]").click()
    # verifyTitle | exact:Caliper: Login |
    time1.sleep(2)

    if str(driver.current_url) == str(Functions.GUIdisplay.URL.get() +"users/sign_in"):
      automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Logout Successfully" , "Login Logout",'s')
    else:
      driver.quit()
      automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Logout failed", "Login Logout", 'p')

if __name__ == "__main__":
    unittest.main(warnings ='ignore')