# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import Functions.Functions

# def doTest():
class Login_Security(unittest.TestCase):
  def setUp(self):
      self.driver = webdriver.Firefox()
      self.driver.implicitly_wait(30)
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

  def test_log_inlog_out(self):
    checkNumError = 0
    testName = "'Login and Logout'"
    driver = self.driver
    # open | http://portal.qa.qa.calipercorp.com/users/sign_in |
    Ori_correct_PortalLink = "http://portal.qa.calipercorp.com/#"
    driver.get(Ori_correct_PortalLink)
    # type | id=user_password | 1234567899
    driver.find_element_by_id("user_password").clear()
    driver.find_element_by_id("user_password").send_keys("123456789")
    # type | id=user_email | ekim+abc1@calipercorp.com
    driver.find_element_by_id("user_email").clear()
    driver.find_element_by_id("user_email").send_keys("ekim+abc1@calipercorp.com")
    # click | name=commit |
    driver.find_element_by_id("login-btn").click()
    time.sleep(3)
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

  def test_password_recovery_reset(self):
      checkNumError = 0
      testName = "'Reset Password'"
      driver = self.driver
      # store | https://mail.google.com/mail/u/0/#inbox | Ori_incorrect_GoogleLink
      Ori_incorrect_GoogleLink = "https://mail.google.com/mail/u/0/#inbox"
      Ori_correct_GoogleLink = "https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&service=mail&sacu=1&scc=1&passive=1209600&ignoreShadow=0&acui=0#Email=ekim%40calipercorp.com"

      # open | /users/sign_in |
      driver.get(self.base_url)
      # click | link=exact:Forgot your password? |
      driver.find_element_by_link_text("Forgot your password?").click()
      # type | id=user_email | ekim+ABC2@calipercorp.com
      time.sleep(2)
      driver.find_element_by_id("user_email").send_keys("ekim+ABC3@calipercorp.com")
      # click | name=commit |
      driver.find_element_by_xpath("//form[@id='new_user']/div[3]/div[1]").click()
      # assertText | css=div.alert.alert-notice | You will receive an email with instructions about how to reset your password in a few minutes.
      time.sleep(2)
      check = driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[1]").text
      # print(check)
      if check != "You will receive an email with instructions about how to reset your password in a few minutes.":
        checkNumError += 1
      time.sleep(2)
      # open | https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1 |
      driver.get(
        "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1")
      # storeLocation | TestingGoogleLink |
      TestingGoogleLink = driver.current_url

      driver.find_element_by_id("Email").send_keys("ekim@calipercorp.com")
      driver.find_element_by_id("next").click()
      time.sleep(2)
      driver.find_element_by_id("Passwd").send_keys("01696502330ESk")
      remember = driver.find_element_by_id("PersistentCookie")
      if remember.get_attribute("value") == "true":
         driver.find_element_by_class_name("remember").click()
      driver.find_element_by_id("signIn").click()

      # type | id=gbqfq | Request to reset password
      time.sleep(2)
      driver.find_element_by_id("gbqfq").clear()
      driver.find_element_by_id("gbqfq").send_keys("Request to reset password")
      # click | id=gbqfb |
      driver.find_element_by_id("gbqfb").click()
      # click | class=xY a4W |
      time.sleep(2)

      driver.find_element_by_xpath("//div[@class='AO']//tbody/tr[1]/td[6]/div[1]/div[1]/div[2]/span[1]").click()
      window_before = driver.window_handles[0]
      time.sleep(2)
      # click | link=Reset Password |
      driver.find_element_by_link_text("Reset Password").click()
      # click | css=span.gb_Za.gb_Xa |
      window_after = driver.window_handles[1]
      #driver.find_element_by_css_selector("span.gb_Za.gb_Xa").click()
      # type | id=user_password | 1234567899
      time.sleep(2)

      try:
        if "reset_password_token" not in driver.current_url:
          driver.switch_to.window(window_after)
          driver.find_element_by_id("user_password").send_keys("123456789")
          time.sleep(1)
          driver.find_element_by_id("user_password_confirmation").send_keys("123456789")
          time.sleep(1)
          driver.find_element_by_name("commit").click()
          time.sleep(1)
          check =  driver.find_element_by_xpath("//div[@class ='hidden-print']/div[@id='alertMsgContainer']/div[1]").text
          if "changed successfully." not in check:
            checkNumError += 1

      except AssertionError as e:
        self.verificationErrors.append(str(e))

      driver.quit()
      Functions.Functions.checkForError(checkNumError, testName)

  def test_resend_password_unlock(self):
      checkNumError = 0
      testName = "'Resend Password Unlock'"
      i = 0
      driver = self.driver
      while i < 2:
        originalLocked = "Your account is locked."
        if i == 0:
          driver.get("http://portal.qa.calipercorp.com/users/sign_in")
        if i == 1:
          driver = webdriver.Firefox()
          driver.get("http://portal.qa.calipercorp.com/users/sign_in")
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
            driver.find_element_by_id("Email").send_keys("ekim@calipercorp.com")
            driver.find_element_by_id("next").click()
            time.sleep(1)
            if i == 0:
              driver.find_element_by_id("Passwd").send_keys("01696502330ESk")
              driver.find_element_by_id("signIn").click()
            if i == 1:
              driver.find_element_by_id("Passwd").send_keys("01696502330ESk")
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

# if __name__ == "__main__":
#       unittest.main(warnings ='ignore')
#########################WAIT UNTIL THE DRIVER FIND THE ELEMENT
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "C29_W35_V37_V46_btresporg_struct.partner_no-btn")))
#     driver.find_element_by_id("C29_W35_V37_V46_btresporg_struct.partner_no-btn").click()
# except TimeoutException:
#     print("C29_W35_V37_V46_btresporg_struct.partner_no-btn not found")