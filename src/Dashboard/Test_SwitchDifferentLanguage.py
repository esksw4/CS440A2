# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import Functions

class SwitchDifferentLanguage(unittest.TestCase):
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
    
    def test_switch_different_language(self):
        checkNumError = 0
        testName = "'Switch Different language'"
        driver = Functions.Functions.OPL(self, testName)

        driver.find_element_by_id("localeSelector").click()
        driver.find_element_by_link_text("Deutsch - Deutschland").click()
        time.sleep(2)
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "Assessment einrichten/ Bericht anfordern":
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=English - UK |
        driver.find_element_by_link_text("English - UK").click()
        time.sleep(2)
        # assertText | css=#dashboard-graph > svg | exact:Created with Raphaël 2.1.216%Technician11%QA engineer10%Technician_SimpleChinese8%Customer Service Representative8%Management CPRJob Title Distribution (Top 5)*
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "Order a Report/Assessment":
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=日本語 - 日本 |
        driver.find_element_by_link_text(u"日本語 - 日本").click()
        time.sleep(2)
        # assertText | css=#dashboard-graph > svg | exact:Created with Raphaël 2.1.216%Technician11%QA engineer10%Technician_SimpleChinese8%Customer Service Representative8%Management CPR職種の分布（トップ5）*
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "受検登録とレポートオーダー":
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=한국어 - 한국 |
        driver.find_element_by_link_text(u"한국어 - 한국").click()
        time.sleep(2)
        # assertText | css=#dashboard-graph > svg | exact:Created with Raphaël 2.1.216%Technician11%QA engineer10%Technician_SimpleChinese8%Customer Service Representative8%Management CPR직위 분포(상위 5)*
        check = driver.find_element_by_id("dashboardOrderReport").text
        if check != "보고서/평가 주문":
          print("Korean")
          checkNumError += 1

        # click | id=localeSelector |
        driver.find_element_by_id("localeSelector").click()
        # click | link=English - US |
        driver.find_element_by_link_text("English - US").click()
        time.sleep(2)
        # assertText | css=svg | Created with Raphaël 2.1.220Pending Assessments
        check = driver.find_element_by_id("localeSelector").text
        if check != "English - US":
          checkNumError += 1

        Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
  unittest.main(warnings ='ignore')
