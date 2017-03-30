from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
    import GUI

    #import Functions.Variable as fv 
    checkNumError = 0
    testName = "'Order for existing job title'"
    driver = Functions.Functions.OPL(self, testName)
    #driver.get(self.base_url + "/")

    # print("Print result with key called first Name: ". Functions.result.keys() == "firstName")

    # click | id=dashboardOrderReport |
    driver.find_element_by_id("dashboardOrderReport").click()
    time1.sleep(2)
    
    # Enter existing JobTitle
    driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys("QA engineer")
    time1.sleep(1)
    driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath("//div[@id='newOrderForm']/div[1]/div[1]/div[1]/span[1]/input[@id='jobTitle-tokenfield']").send_keys(Keys.ENTER)
    time1.sleep(1)

    # Enter new Assessee
    driver.find_element_by_id('assesseeBtn').click()
    time1.sleep(2)

    driver.find_element_by_id('assesseeFirstName').send_keys(Functions.orderNewReportResult['First Name'])
    driver.find_element_by_id('assesseeLastName').send_keys(Functions.orderNewReportResult['Last Name'])
    driver.find_element_by_id('assesseeEmail').send_keys(Functions.orderNewReportResult['Email Address'])
    driver.find_element_by_xpath("//div[@class='row assesseePoNumberRow']/div[2]/input[@id='assesseePoNumber']").send_keys(Functions.orderNewReportResult['PO Box'])
    driver.find_element_by_xpath("//div[@class='row assesseeCostCenterRow']/div[2]/input[@id='assesseeCostCenter']").send_keys(Functions.orderNewReportResult['Cost Center'])
    driver.find_element_by_xpath("//div[@class='row assesseeCustomFieldRow1']/div[2]/textarea[@id='assesseeCustomField1']").send_keys(Functions.orderNewReportResult['Color'])
    driver.find_element_by_xpath("//div[@class='row assesseeCustomFieldRow2']/div[2]/textarea[@id='assesseeCustomField2']").send_keys(Functions.orderNewReportResult['Position Number'])
    driver.find_element_by_xpath("//div[@class='row assesseeCustomFieldRow3']/div[2]/textarea[@id='assesseeCustomField3']").send_keys(Functions.orderNewReportResult['Favorite Number'])
    driver.find_element_by_xpath("//div[@class='row assesseeSpecialInstructionsRow']/div[2]/textarea[@id='assesseeSpecialInstructions']").send_keys(Functions.orderNewReportResult['Message to Consultant'])
    driver.find_element_by_xpath("//div[@class='row assesseeEmailMessageRow']/div[2]/textarea[@id='assesseeEmailMessage']").send_keys(Functions.orderNewReportResult['Message to Assessee'])
    # click save
    driver.find_element_by_id('assesseeSaveButton').click()
    time1.sleep(2)

    #check if Error occurs
    checkErrorMsg = OrderNewReport.is_element_present(self, By.CLASS_NAME, "alert.alert-error.alert-dismissable")
    # print("ErrorMessage Exists? ", checkErrorMessage)
    # according to erro occurs, display error message in the tkinter file.
    if (checkErrorMsg == True):
      driver.quit()
      # Functions.Functions.orderNewStopTest()
      GUI.GUIFunctions.orderNewReportErrorMessageCheck(False, "Please Enter inputs in valid format")
      # print(GUItkinter.py)
      # from GUItkinter import inputFrame
      # GUItkinter.getUserInputSendFunction

    	# check if also notify present and if it does, then put the user in there.
    alsoNotifyLocation = "//div[@id='deliverToDiv']/div[1]/span[1]/input[1]"
    checkAlsoNotify = OrderNewReport.is_element_present(self, By.XPATH, alsoNotifyLocation)
    print("checkAlsoNotify: ", checkAlsoNotify)
    if checkAlsoNotify == True:
    	driver.find_element_by_xpath(alsoNotifyLocation).send_keys(Functions.orderNewReportResult['Also Notify'])
    	time1.sleep(2)
    	driver.find_element_by_xpath(alsoNotifyLocation).send_keys(Keys.ARROW_DOWN)
    	time1.sleep(2)
    	driver.find_element_by_xpath(alsoNotifyLocation).send_keys(Keys.ENTER)
    	time1.sleep(2)


    # Click Prodctored Assessment
    try: 
    	driver.find_element_by_xpath("//div[@id='newOrderForm']/div[6]/div[1]/div[1]/input[@id='proctored']").click()
    	driver.find_element_by_xpath("//div[@id='sendToMeDiv']/input[@id='sendToMe']").click()
    	#Click "Place Order"
    except:
      GUI.GUIFunctions.outputDisplayConsole("Proctored checkbox cannot be pressed automatically. Please manually test the proctored checkbox")
      driver.find_element_by_id("newOrderBtn").click()
      time1.sleep(3)

    ############################CHECK FORMAT HERE. Try-Except and If-Else
    checkErrorMsg = OrderNewReport.is_element_present(self, By.CLASS_NAME, "alert.alert-error.alert-dismissable")
    if checkErrorMsg == True:
      driver.quit()
      GUI.GUIFunctions.outputDisplayConsole("Please choose different email for assessee. That email address already exists in the system.")

    else:
      #click OK on order confirmation dlg box
      driver.find_element_by_id("okButton").click()
      time1.sleep(3)
      if 'reports' in driver.current_url:
        fullName = Functions.orderNewReportResult['First Name'] + " " + Functions.orderNewReportResult['Last Name']
        print(fullName)
        checkfullName = driver.find_element_by_xpath("//tbody/tr[1]/td[4]/div[1]/div[@class='main-text assessee-name']").text
        try: 
          if fullName == checkfullName:
            # click the dropdown
            driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/a[1]").click()
            time1.sleep(1)
            # test "Copy assessment URL"
            assessmentURL =  driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/ul[1]/li[5]").get_attribute('data-clipboard-text')
            # click "Copy assessment URL"
            driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/ul[1]/li[5]").click()
            tab_before = driver.window_handles[0]
            driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL +"t")
            tab_after = driver.window_handles[1]
            driver.switch_to.window(tab_after)
            driver.get(assessmentURL)
            time1.sleep(3)
            registerCheck = driver.find_element_by_xpath("//div[@class='container container-min-height']/div[2]/legend[1]/h4[1]").text
            if "Register" == registerCheck:
              print(registerCheck)
              driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL + Keys.F4)
              driver.switch_to.window(tab_before)
              # Cancel It
              driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/ul[1]/li[3]").click()
              driver.find_element_by_xpath("//div[@class='modal-dialog']/div[1]/div[3]/button[1]").click()
              try:
                checkConfirmationMessage = driver.find_element(self, By.CLASS_NAME, "alert.alert-success.alert-dismissable").text
                if fullName in checkConfirmationMessage:
                  print("Does it come here")
                  driver.close()
                  GUI.GUIFunctions.outputDisplayConsole("CHECKED!")
              except:









    # Check if assessee exists
    # errorAlertLocation = "//div[@id='alertMsgContainer']/div[@class='alert alert-error alert-dismissable']"
    # checkExistingAssessee = OrderNewReport.is_element_present(self, By.XPATH, errorAlertLocation)







    #time1.sleep(5)

if __name__ == "__main__":
  unittest.main(warnings='ignore')