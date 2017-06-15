# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import Functions

class Test_ViewReport(unittest.TestCase):
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

    def test_view_a_report(self):
        checkNumError = 0
        testName = "View Report Tab"
        driver = Functions.Functions.OPL(self, testName)

        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        check = driver.title
        if check != "Caliper: Reports":
          checkNumError += 1

        driver.find_element_by_link_text("Caliper").click()
        time.sleep(2)
        # click 1st report to see
        assesseeName = driver.find_element_by_xpath("//div[@class='dashboard-orders']/div[1]/div[2]/a[1]").text
        assesseeName = assesseeName.split(" ")
        assesseeName = assesseeName[0] + "_" + assesseeName[1]
        driver.find_element_by_xpath("//div[@class='dashboard-orders']/div[1]/div[2]/a[1]").click()
        driver.switch_to.window(driver.window_handles[1])
        # FselectWindow | title=4207867 |
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | title=4207867 | ]]
        # assertTitle | 4207867 |
        time.sleep(2)
        #check = driver.current_url
        if assesseeName not in driver.current_url:
          checkNumError += 1

        driver.quit()
        Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
    unittest.main(warnings ='ignore')        