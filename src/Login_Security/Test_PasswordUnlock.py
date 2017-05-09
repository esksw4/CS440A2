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
class Test_PasswordUnlock(unittest.TestCase):
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

  def test_resend_password_unlock(self):
      checkNumError = 0
      testName = "'Resend Password Unlock'"
      i = 0
      driver = self.driver
      while i < 2:
        originalLocked = "Your account is locked."
        if i == 0:
          driver.get(Functions.URL)
        if i == 1:
          driver = webdriver.Firefox()
          driver.get(Functions.URL)
        driver.find_element_by_id("user_email").send_keys("ekim+ABC2@calipercorp.com")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("1")
        driver.find_element_by_xpath("//div[@id ='main-content']/div[3]/div[1]/div[1]/form[1]/div[5]/div[1]/a[@id='login-btn']").click()
        time.sleep(2)
        testingCondition = driver.find_element_by_css_selector("div.alert.alert-alert").text

        while originalLocked != testingCondition:
          time.sleep(2)
          driver.find_element_by_id("user_email").clear()
          driver.find_element_by_id("user_email").send_keys("ekim+ABC2@calipercorp.com")
          time.sleep(1)
          driver.find_element_by_id("user_password").clear()
          driver.find_element_by_id("user_password").send_keys("1")
          driver.find_element_by_xpath("//div[@id ='main-content']/div[3]/div[1]/div[1]/form[1]/div[5]/div[1]/a[@id='login-btn']").click()
          time.sleep(2)
          testingCondition = driver.find_element_by_css_selector("div.alert.alert-alert").text
          # print("testingCondiution2: " + testingCondition)

        if originalLocked == testingCondition:
          driver.find_element_by_link_text("Didn't receive unlock instructions?").click()
          time.sleep(1)
          driver.find_element_by_id("user_email").send_keys("ekim+ABC2@calipercorp.com")
          driver.find_element_by_css_selector("input.btn.btn-primary").click()

          Ori_correct_GoogleLink = "https://mail.google.com/mail/u/0/#inbox"
          driver.get("http://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1")
          TestingGoogleLink = driver.current_url

          if TestingGoogleLink != Ori_correct_GoogleLink:
            driver.find_element_by_id("Email").send_keys(Functions.OPLINfo['Email Address'])
            driver.find_element_by_id("next").click()
            time.sleep(1)
            if i == 0:
              driver.find_element_by_id("Passwd").send_keys(Functions.OPLINfo['Email Password'])
              driver.find_element_by_id("signIn").click()
            if i == 1:
              driver.find_element_by_id("Passwd").send_keys(Functions.OPLINfo['Email Password'])
              driver.find_element_by_id("signIn").click()

          time.sleep(3)
          driver.find_element_by_id("gbqfq").click()
          driver.find_element_by_id("gbqfq").clear()
          driver.find_element_by_id("gbqfq").send_keys("unlock Instructions")
          driver.find_element_by_id("gbqfb").click()
        time.sleep(3)#//div[@class='AO']//div[@class'nH']/div[2]/div[5]/div[@class='Cp']
        driver.find_element_by_xpath("//tbody/tr[1]/td[6]/div[1]/div[1]/div[2]").click()
        window_before = driver.window_handles[0]
        time.sleep(3)
        if i == 0:
          driver.find_element_by_xpath("//div[@class = 'iH']/div/div[2]/div[3]").click()
          driver.quit()
        i += 1
      driver.find_element_by_link_text("Unlock My Account").click()
      window_after = driver.window_handles[1]
      driver.switch_to.window(window_after)

      time.sleep(2)
      check = driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[1]").text
      if check != "Your account has been unlocked successfully. Please sign in to continue.":
        checkNumError += 1

      driver.quit()
      Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')
