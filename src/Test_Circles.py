# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test_Circles(unittest.TestCase):
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

    def test_click_a_circle(self):
        import Functions
        import automatedSmokeTest


        # checkNumError = 0
        Functions.GUIdisplay.testName = "Click Circles"
        driver = Functions.Functions.OPL(self)

        time.sleep(1)

        # Click Pending Assessement circle
        driver.find_element_by_xpath("//div[@id='dashboard-chart1']").click()
        time.sleep(2)
        if "Caliper: Reports" not in driver.title:
          automatedSmokeTest.GUIFunctions.outputDisplayConsole("Pending Assessment circle does not lead to report page", Functions.GUIdisplay.testName,'se')
        # Click Caliper logo
        else:
          driver.find_element_by_link_text("Caliper").click()
          time.sleep(2)

          # Click Pending Report circle
          driver.find_element_by_xpath("//div[@id='dashboard-chart2']").click()
          time.sleep(2)
          if "Caliper: Reports" not in driver.title:
            automatedSmokeTest.GUIFunctions.outputDisplayConsole("Pending Report circle does not lead to report page", Functions.GUIdisplay.testName,'se')
          else:
            # Click Caliper logo
            driver.find_element_by_link_text("Caliper").click()
            time.sleep(2)
            
            # Click Completed Reports
            driver.find_element_by_xpath("//div[@id='dashboard-chart3']").click()
            time.sleep(2)
            if "Caliper: Reports" not in driver.title:
              automatedSmokeTest.GUIFunctions.outputDisplayConsole("Complete Report circle does not lead to report page", Functions.GUIdisplay.testName,'se')
            else:
              # Click Caliper logo
              driver.find_element_by_link_text("Caliper").click()
              time.sleep(2)

              # Click Total Report
              driver.find_element_by_xpath("//div[@id='dashboard-chart4']").click()
              time.sleep(2)
              if "Caliper: Reports" not in driver.title:
                automatedSmokeTest.GUIFunctions.outputDisplayConsole("Total Report circle does not lead to report page", Functions.GUIdisplay.testName,'se')
              # Click Caliper logo
              driver.find_element_by_link_text("Caliper").click()
              time.sleep(2)
              if "Caliper: Dashboard" not in driver.title:
                automatedSmokeTest.GUIFunctions.outputDisplayConsole("Caliper Logo on left top corner does not lead to Dashboard page", Functions.GUIdisplay.testName,'se')
              else:
                automatedSmokeTest.GUIFunctions.outputDisplayConsole("All the circles are sucessfully directed to report page", Functions.GUIdisplay.testName,'s')

if __name__ == "__main__":
    unittest.main(warnings ='ignore')