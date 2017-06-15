from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import GUItkinter

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, string, sys
import time as time1

class OrderNewReport(unittest.TestCase):
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

  def test_order_Exist_Job_Title(self):
    import Functions
    checkNumError = 0
    testName = "'Order for existing job title'"
    driver = Functions.Functions.OPL(self, testName)
    driver.get(self.base_url + "/")

    print(Functions.Functions.firstName)

    # click | id=dashboardOrderReport |
    driver.find_element_by_id("dashboardOrderReport").click()
    time1.sleep(2)
    
    # Enter existing JobTitle
    driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys("QA engineer")
    driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys(Keys.ENTER)
    time1.sleep(1)

    # Enter new Assessee
    driver.find_element_by_id('assesseeBtn').click()
    time1.sleep(2)

    driver.find_element_by_id('assesseeFirstName').send_keys(Functions.Functions.firstName)
    driver.find_element_by_id('assesseeLastName').send_keys(Functions.Functions.lastName)
    driver.find_element_by_id('assesseeEmail').send_keys(Functions.Functions.emailAddress)
    driver.find_element_by_xpath("//div[@class='row assesseePoNumberRow']/div[2]/input[@id='assesseePoNumber']").send_keys(Functions.Functions.poBox)
    driver.find_element_by_xpath("//div[@class='row assesseeCostCenterRow']/div[2]/input[@id='assesseeCostCenter']").send_keys(Functions.Functions.costCenter)
    driver.find_element_by_xpath("//div[@class='row assesseeCostCenterRow']/div[2]/input[@id='assesseeCustomField1']").send_keys(Functions.Functions.coLor)
    driver.find_element_by_xpath("//div[@class='row assesseeCostCenterRow']/div[2]/input[@id='assesseeCustomField2']").send_keys(Functions.Functions.positionNum)
    driver.find_element_by_xpath("//div[@class='row assesseeCostCenterRow']/div[2]/input[@id='assesseeCustomField3']").send_keys(Functions.Functions.favNum)
    driver.find_element_by_xpath("//div[@class='row assesseeSpecialInstructionsRow']/div[2]/textarea[@id='assesseeSpecialInstructions']").send_keys(msgConsultant)
    driver.find_element_by_xpath("//div[@class='row assesseeEmailMessageRow']/div[2]/textarea[@id='assesseeEmailMessage']").send_keys(msgPersonalized)
    # click save
    driver.find_element_by_id('assesseeSaveButton').click()

    # check if also notify present and if it does, then put the user in there.
    alsoNotifyLocation = "//div[@id='deliverToDiv']/div[1]/span[1]/input[1]"
    checkAlsoNotify = OrderNewReport.is_element_present(self, By.XPATH, alsoNotifyLocation)
    if (checkAlsoNotify):
      driver.find_element_by_xpath(alsoNotifyInput).send_keys(Functions.Functions.alsoNotify)
      driver.find_element_by_xpath(alsoNotifyInput).send_keys(Keys.ARROW_DOWN)
      driver.find_element_by_xpath(alsoNotifyInput).send_keys(Keys.ENTER)
    
    # Click Prodctored Assessment
    driver.find_element_by_xpath("//input[@id='proctored']").click()
    driver.find_element_by_xpath("//div[@id='sendToMeDiv']/input[@id='sendToMe']").click()

    #Click "Place Order"


    # Check if assessee exists
    errorAlertLocation = "//div[@id='alertMsgContainer']/div[@class='alert alert-error alert-dismissable']"
    checkExistingAssessee = OrderNewReport.is_element_present(self, By.XPATH, errorAlertLocation)

    #Functions.Functions.orderReportCheck(driver, firstNum, lastNum, emailNum, 





    #time1.sleep(5)

if __name__ == "__main__":
  unittest.main(warnings ='ignore')