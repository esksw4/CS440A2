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
class Test_PasswordRecovery(unittest.TestCase):
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

  def test_password_recovery_reset(self):
      import Functions
      import automatedSmokeTest

      testName = "Password Recovery"
      
      driver = self.driver
      # driver = Functions.Functions.OPL(self, testName)
      driver.get(Functions.GUIdisplay.URL.get())

      Ori_incorrect_GoogleLink = "https://mail.google.com/mail/u/0/#inbox"
      Ori_correct_GoogleLink = "https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&service=mail&sacu=1&scc=1&passive=1209600&ignoreShadow=0&acui=0#Email=ekim%40calipercorp.com"

      # click | link=exact:Forgot your password? |
      driver.find_element_by_link_text("Forgot your password?").click()
      # type | id=user_email | ekim+ABC2@calipercorp.com
      time.sleep(2)
      driver.find_element_by_id("user_email").send_keys(Functions.OPLInfo['Portal Username'])
      # click | name=commit |
      driver.find_element_by_xpath("//form[@id='new_user']/div[3]/div[1]").click()
      # assertText | css=div.alert.alert-notice | You will receive an email with instructions about how to reset your password in a few minutes.
      time.sleep(2)
      check = driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[1]").text
      # print(check)
      if check != "You will receive an email with instructions about how to reset your password in a few minutes.":
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("The confirmation message saying 'You will receive an email with instructions about how to reset your password in a few minutes.' is not displayed correctly" , testName, 's')
      time.sleep(2)
      # open | https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1 |
      driver.get(
        "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1")
      # storeLocation | TestingGoogleLink |
      TestingGoogleLink = driver.current_url

      driver.find_element_by_id("identifierId").send_keys(Functions.OPLInfo['Email Address'])
      driver.find_element_by_class_name("RveJvd.snByac").click()
      if Test_PasswordRecovery.is_element_present(self, By.XPATH, "//div[@class='rFrNMe uIZQNc og3oZc sdJrJc Tyc9J CDELXb k0tWj IYewr']/div[@class='LXRPh']/div[@class='dEOOab RxsGPe']"):
        driver.quit()
        automatedSmokeTest.GUIFunctions.outputDisplayConsole("Input Error: Email Address is invalid. Please enter the valid email address" , testName, 'ie')
      else:
        time.sleep(2)
        driver.find_element_by_xpath("//form[@class='RFjuSb bxPAYd k6Zj8d']/div[2]//div[@class='Xb9hP']/input[1]").send_keys(Functions.OPLInfo['Email Password'])
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
        time.sleep(2)
        if Test_PasswordRecovery.is_element_present(self, By.XPATH, "//div[@id='password']/div[@class='LXRPh']/div[@class='dEOOab RxsGPe']"):
          driver.quit()
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("Input Error: Email Password is invalid. Please enter the valid email Password" , testName, 'ie')
        else:
          # search "Request to reset password" on the gmail
          time.sleep(2)
          driver.find_element_by_id("gbqfq").clear()
          driver.find_element_by_id("gbqfq").send_keys("Request to reset password")
          driver.find_element_by_id("gbqfb").click()
          
          time.sleep(2)
          driver.find_element_by_xpath("//div[@class='AO']//tbody/tr[1]/td[6]/div[1]/div[1]/div[2]/span[1]").click()
          window_before = driver.window_handles[0]
          time.sleep(2)
          # click "Reset Password" inside of email sent
          driver.find_element_by_link_text("Reset Password").click()
          time.sleep(1)
          window_after = driver.window_handles[1]
          driver.switch_to.window(window_after)
          time.sleep(2)
          # print("Text Token expired: ", driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[@class='alert alert-error']").text)
          if "reset_password_token" in driver.current_url:
            driver.find_element_by_id("user_password").send_keys(Functions.OPLInfo['Portal Password to change'])
            time.sleep(1)
            driver.find_element_by_id("user_password_confirmation").send_keys(Functions.OPLInfo['Portal Password to change'])
            time.sleep(1)
            driver.find_element_by_name("commit").click()
            time.sleep(2)
            # print("is_element_present: ", Test_PasswordRecovery.is_element_present(self, By.XPATH, "//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[@class='alert alert-error alert-dismissable']"))
            # print(driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[@class='alert alert-error alert-dismissable']").text)

            if Test_PasswordRecovery.is_element_present(self, By.XPATH, "//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[@class='alert alert-notice']"):
              automatedSmokeTest.GUIFunctions.outputDisplayConsole("Password was succesfully resetted." , testName, 's')
            elif Test_PasswordRecovery.is_element_present(self, By.XPATH, "//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[@class='alert alert-error']"):
              # print('\n')
              # print("check: ", driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[@class='alert alert-error]").text)
              driver.quit()
              automatedSmokeTest.GUIFunctions.outputDisplayConsole("Password needed to be contain certain characters. Please re-write the password to change." , testName, 'ie')
            else:
              driver.quit()
              automatedSmokeTest.GUIFunctions.outputDisplayConsole("Password did not get reset." , testName, 'se')
          elif Test_PasswordRecovery.is_element_present(self, By.XPATH, "//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[@class='alert alert-error']"):
            driver.quit()
            automatedSmokeTest.GUIFunctions.outputDisplayConsole("The 'Reset Password' token is expired.", testName, 'se')
          else:
            driver.quit()
            automatedSmokeTest.GUIFunctions.outputDisplayConsole("'Reset Password' button from email is not working correctly." , testName, 'se')



if __name__ == "__main__":
    unittest.main(warnings ='ignore')