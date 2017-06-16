# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test_OrderReportButton(unittest.TestCase):
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

    def test_does_ordera_report_work(self):
        import Functions
        import automatedSmokeTest

        Functions.GUIdisplay.testName = "Order Report Button"
        driver = Functions.Functions.OPL(self)
        time.sleep(2)
        # click | id=dashboardOrderReport |
        driver.find_element_by_id("dashboardOrderReport").click()
        time.sleep(2)
        check = driver.title
        if check == "Caliper: Order Reports/Assessments":
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("Order Report Button successfully directs you to Order page.", Functions.GUIdisplay.testName,'s')
        # click | link=Caliper |
        else: 
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("Order Report Button DOES NOT directs you to Order page.", Functions.GUIdisplay.testName,'se')
          # driver.find_element_by_link_text("Caliper").click()

        # Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')
