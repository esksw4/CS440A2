# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

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
    import Functions
    import automatedSmokeTest
    # checkNumError = 0
    Functions.GUIdisplay.testName = "Password Unlock"
    i = 0
    driver = self.driver
    originalLocked = "Your account is locked."

    while i < 2:
      if i == 0:
        driver.get(Functions.GUIdisplay.URL.get())
        driver.find_element_by_id("user_email").send_keys(Functions.OPLInfo['Portal Username'])
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("1")
        driver.find_element_by_xpath("//div[@id ='main-content']/div[3]/div[1]/div[1]/form[1]/div[5]/div[1]/a[@id='login-btn']").click()
        time.sleep(2)
        testingCondition = driver.find_element_by_css_selector("div.alert.alert-alert").text

        # lock the account by applying wrong password. 
        howManyLoop = 0
        while testingCondition != originalLocked:
          howManyLoop += 1
          if howManyLoop > 5:
            i = 1
            automatedSmokeTest.GUIFunctions.outputDisplayConsole("According to Error message, the password does not get locked." , Functions.GUIdisplay.testName, 'se')
          else:
            time.sleep(2)
            driver.find_element_by_id("user_email").clear()
            driver.find_element_by_id("user_email").send_keys(Functions.OPLInfo['Portal Username'])
            time.sleep(1)
            driver.find_element_by_id("user_password").clear()
            driver.find_element_by_id("user_password").send_keys("1")
            driver.find_element_by_xpath("//div[@id ='main-content']/div[3]/div[1]/div[1]/form[1]/div[5]/div[1]/a[@id='login-btn']").click()
            time.sleep(2)
            testingCondition = driver.find_element_by_css_selector("div.alert.alert-alert").text
      # Since the account is already locked, you need to re-lock the account.
      # Now just check if "Resend Unlock Instruction" is working or not.
      if i == 1:
        driver = self.driver
        driver.get(Functions.GUIdisplay.URL.get())
        time.sleep(2)
        # print("testingCondiution2: " + testingCondition)
        driver.find_element_by_link_text("Didn't receive unlock instructions?").click()
        time.sleep(1)
        driver.find_element_by_id("user_email").send_keys(Functions.OPLInfo['Portal Username'])
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

      # either if this statement reached from locking the account or trying to "resend the unlock instruction", perform this lines
      time.sleep(1)
      Ori_correct_GoogleLink = "https://mail.google.com/mail/u/0/#inbox"
      driver.get("http://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1")
      time.sleep(2)
      TestingGoogleLink = driver.current_url
      print("i: ", i)
      # if the gmail is not logged in, log in.
      if TestingGoogleLink != Ori_correct_GoogleLink:
        driver.find_element_by_id("identifierId").send_keys(Functions.OPLInfo['Email Address'])
        driver.find_element_by_class_name("RveJvd.snByac").click()
        time.sleep(1)
        # if there is error occur during email address
        if Test_PasswordUnlock.is_element_present(self, By.XPATH, "//div[@class='rFrNMe uIZQNc og3oZc sdJrJc Tyc9J CDELXb k0tWj IYewr']/div[@class='LXRPh']/div[@class='dEOOab RxsGPe']"):
          i = 100
          driver.quit()
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("Input Error: Email Address is invalid. Please enter the valid email address" , Functions.GUIdisplay.testName, 'ie')
        # if there is no error during email address, process with email password
        else:
          # if i == 0 or i == 1:
          time.sleep(2)
          driver.find_element_by_xpath("//form[@class='RFjuSb bxPAYd k6Zj8d']/div[2]//div[@class='Xb9hP']/input[1]").send_keys(Functions.OPLInfo['Email Password'])
          time.sleep(2)
          driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
          # if there is error inputing the email password, throw the error and make user to re-input the password
          if Test_PasswordUnlock.is_element_present(self, By.XPATH, "//div[@id='password']/div[@class='LXRPh']/div[@class='dEOOab RxsGPe']"):
            i = 100
            driver.quit()
            automatedSmokeTest.GUIFunctions.outputDisplayConsole("Input Error: Email Password is invalid. Please enter the valid email Password" , Functions.GUIdisplay.testName, 'ie')
      # if gmail is logged in,
      # search the "unlock Instruction" email
      time.sleep(3)
      driver.find_element_by_id("gbqfq").click()
      driver.find_element_by_id("gbqfq").clear()
      driver.find_element_by_id("gbqfq").send_keys("unlock Instructions")
      driver.find_element_by_id("gbqfb").click()
      time.sleep(3)
      # click the first line of the list
      driver.find_element_by_xpath("//div[@class='nH bkK nn']//div[@class='nH ar4 B']/div[1]/div[@class='AO']/div[1]/div[1]/div[1]/div[2]/div[@class='ae4 UI']//tbody/tr[1]/td[6]/div[1]/div[1]/div[2]/span[1]").click()
      window_before = driver.window_handles[0]
      time.sleep(3)
      # if this is first time testing (meaning i = 0), just check if email went through or not.
      if i == 0:
        if Test_PasswordUnlock.is_element_present(self, By.LINK_TEXT,"Unlock My Account") == False:
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("First email was not received on the email(%s). I'm checking for second time." %Functions.OPLInfo['Email Address'], Functions.GUIdisplay.testName, 'se')
        # driver.quit()
      i += 1 # now going back to very beginning. Need to check for 2nd time.

    if i != 100:
      # Since "resend unlock instructions" and locking account are passed succesfully, Now try to unlock it.
      driver.find_element_by_link_text("Unlock My Account").click()
      window_after = driver.window_handles[1]
      driver.switch_to.window(window_after)

      time.sleep(2)
      check = driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[1]").text
      print("check: ", check)

      if check == "Your account has been unlocked successfully. Please sign in to continue.":
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("Account is unlocked succesfully." , Functions.GUIdisplay.testName, 's')
      else:
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("Was not able to unlock the account. " , Functions.GUIdisplay.testName, 'se')
        # if check != "Your account has been unlocked successfully. Please sign in to continue.":
        #   checkNumError += 1

        # driver.quit()
        # Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')
