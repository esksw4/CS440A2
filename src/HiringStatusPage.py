from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import Functions.Functions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, string, sys
import time as time1
from datetime import date
from datetime import time 
from datetime import datetime
from datetime import timedelta

class HiringStatusPage(unittest.TestCase):
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
    
  # def checkDateList(driver, checkNumError, listAssessee, tothis, fromthis):
  #   checkdateinRange = driver.find_element_by_xpath("//tbody/tr[1]/td[3]//div[@class='second-line']").text
  #   checkdateinRange = datetime.strptime(checkdateinRange, '%m/%d/%Y')
  #   checkdateinRange = checkdateinRange.date()

  #   if listAssessee == 1 and checkdateinRange >= fromthis and checkdateinRange <= tothis:
  #     pass

  #   elif listAssessee == 1 and (checkdateinRange <= fromthis or checkdateinRange >= tothis):
  #     checkNumError += 1

  #   else:
  #     for i in range(1, listAssessee+1):
  #       time1.sleep(1)
  #       #print("i: " + str(i))
  #       checkdateinRange = driver.find_element_by_xpath("//tbody/tr[%d]/td[3]//div[@class='second-line']" % (i)).text
  #       checkdateinRange = datetime.strptime(checkdateinRange, '%m/%d/%Y')
  #       checkdateinRange = checkdateinRange.date()

  #       if checkdateinRange < fromthis or checkdateinRange > tothis :
  #         checkNumError += 2
  #     return checkNumError

  # def checkStatusList(driver, checkNumError, listAssessee, filterStatus):
  #   whatStatus = driver.find_element_by_xpath("//tbody/tr[1]/td[4]/div[1]//div[@class='matchText status']").text

  #   if listAssessee == 1 and (whatStatus is filterStatus):
  #     return checkNumError

  #   elif listAssessee == 1 and (whatStatus is not filterStatus):
  #     checkNumError += 1
  #     return checkNumError

  #   else:
  #     for i in range(1, listAssessee+1):
  #       whatStatus = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]/div[1]//div[@class='matchText status']" % (i)).text
  #       if whatStatus != filterStatus:
  #         checkNumError += 1
  #         return checkNumError
  #     return checkNumError

  def compareAlphabeticorer(f, l, mustbesmaller, mustbelarger):
    # 1 is true
    # 0 is false
    #print(mustbesmaller,'*', mustbesmaller[f][l],'*',mustbelarger, '*',mustbelarger[f][l],'*')
    if mustbesmaller == mustbelarger:
      returnthis = 1
      return returnthis
    if ord(mustbesmaller[f][l]) == ord(mustbelarger[f][l]):   
        while l < min(len(mustbesmaller[f]), len(mustbelarger[f]))-1:
          l += 1
          whatReturned = HiringStatusPage.compareAlphabeticorer(f,l,mustbesmaller,mustbelarger)
          if whatReturned == 1:
            #print('1')
            returnthis = 1
            return returnthis
          else:
            #print('2')
            returnthis = 0
            return returnthis
        if len(mustbesmaller[f]) == len(mustbelarger[f]):
          if f == 0:
            #print('3')
            print('assessee names are same')
            returnthis = 1
            return returnthis
          else:
            #print('4')
            HiringStatusPage.compareAlphabeticorer(f-1,0,mustbesmaller,mustbelarger)
        elif len(mustbesmaller[f]) < len(mustbelarger[f]):
          #print('5')
          returnthis = 1
          return returnthis
        else:
          #print('6')
          returnthis = 0
          return returnthis
    elif ord(mustbesmaller[f][l]) < ord(mustbelarger[f][l]):
      #print('7')
      returnthis = 1
      return returnthis
    elif ord(mustbesmaller[f][l]) > ord(mustbelarger[f][l]):
        #print('8')
        print('First Name is not sorted correctly')
    else:
      #print('9')
      print('Last Name is not sorted correctly')
      returnthis = 0
      return returnthis
    #print('10')
    return returnthis

  # def howmanyAssesseeListSystem(tableText):
  #   tableText = re.split('\s+', tableText)
  #   global systemAssessee, listAssessee
  #   systemAssessee = int(tableText[5])
  #   listAssessee = int(tableText[3]) - int(tableText[1]) + 1
  #   return systemAssessee, listAssessee

  def sortingCheck(driver, whatToSort, listAssessee, checkNumError):
    i = 1
    if (whatToSort == 'Name'):
      str1 = str("//tbody/tr[")
      str3 = str("]/td[2]/div/div")
      while i < listAssessee:
        str2 = str(i)
        str_element = str1 + str2 + str3
        mustbesmaller = driver.find_element_by_xpath(str_element).text.upper()
        # split the Firstname and Lastname
        # Firstname : mustbesmaller[0]
        # Lastname : mustbesmaller[1]
        mustbesmaller = re.split('\s+', mustbesmaller)
        
        i = i+1
        str2 = str(i)
        str_element = str1 + str2 + str3
        mustbelarger = driver.find_element_by_xpath(str_element).text.upper()
        # split the Firstname and Lastname
        # Firstname : mustbesmaller[0]
        # Lastname : mustbesmaller[1]
        mustbelarger = re.split('\s+', mustbelarger)

        alphabeticWorks = HiringStatusPage.compareAlphabeticorer(1, 0, mustbesmaller, mustbelarger)

        if (alphabeticWorks == 'False'):
          checkNumError += 1
          colorama.init(autoreset=True)
          print(colorama.Fore.RED + 'The row ' + str(i-1) + ' and ' + str(i) + ' are not sorted correctly')
          return checkNumError
            
    elif (whatToSort == 'Date'):
      str1 = str("//tbody/tr[")
      str3 = str("]/td[3]//div[@class='second-line']")
      
      while i < listAssessee:
        str2 = str(i)
        str_element = str1 + str2 + str3
        mustbelarger = driver.find_element_by_xpath(str_element).text
        mustbelarger = datetime.strptime(mustbelarger, '%m/%d/%Y')
        i = i+1
        str2 = str(i)
        str_element = str1 + str2 + str3
        mustbesmaller = driver.find_element_by_xpath(str_element).text
        mustbesmaller = datetime.strptime(mustbesmaller, '%m/%d/%Y')
        
        if (mustbelarger < mustbesmaller):
          checkNumError += 1
          colorama.init(autoreset=True)
          print(colorama.Fore.RED + 'The row ' + str(i-1) + ' and ' + str(i) + ' are not sorted correctly')
          return checkNumError

    elif (whatToSort == 'Supervisor'):
      str1 = str("//tbody/tr[")
      str3 = str("]/td[3]//span[@class='dt-supervisor-name']")
      tableText = driver.find_element_by_id("table_info").text
      systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
      
      if listAssessee != 100:
        driver.find_element_by_xpath("//select[@name='table_length']").click()
        time1.sleep(1)
        driver.find_element_by_xpath("//select[@name='table_length']").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath("//select[@name='table_length']").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath("//select[@name='table_length']").send_keys(Keys.ARROW_DOWN)
        time1.sleep(1)
        driver.find_element_by_xpath("//select[@name='table_length']").send_keys(Keys.ENTER)
        time1.sleep(2)
        tableText = driver.find_element_by_id("table_info").text
        systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
        
        if (listAssessee != 100):
          checkNumError += 1
          colorama.init(autoreset=True)
          print(colorama.Fore.RED + 'The number of entries do not change.')
      
      while i < listAssessee:
        str2 = str(i)
        str_element = str1 + str2 + str3

        while driver.find_element_by_xpath(str_element).text == 'Supervisor not available':
          #print(driver.find_element_by_xpath(str_element).text)
          i += 1
          str2 = str(i)
          str_element = str1 + str2 + str3
        i = i-1;
        str2 = str(i)
        str_element = str1 + str2 + str3
        mustbesmaller = driver.find_element_by_xpath(str_element).text.upper()
        # split the Firstname and Lastname
        # Firstname : mustbesmaller[0]
        # Lastname : mustbesmaller[1]
        mustbesmaller = re.split('\s+', mustbesmaller)
        
        if mustbesmaller[0] == 'SUPERVISOR':
          mustbesmaller.pop(1)
        
        i = i+1
        str2 = str(i)
        str_element = str1 + str2 + str3
        mustbelarger = driver.find_element_by_xpath(str_element).text.upper()
        # split the Firstname and Lastname
        # Firstname : mustbesmaller[0]
        # Lastname : mustbesmaller[1]
        mustbelarger = re.split('\s+', mustbelarger)

        #print('row ' + str(i-1) + ' vs ' + str(i))
        alphabeticWorks = HiringStatusPage.compareAlphabeticorer(1, 0, mustbesmaller, mustbelarger)
        #print(alphabeticWorks)
        
        if alphabeticWorks == 0:
          checkNumError += 1
          return checkNumError
        else:
          i += 1
    
    return checkNumError

  def test_FilterByHiringStatus(self):
    checkNumError = 0
    testName = "'Filter by Hiring Status'"
    driver = Functions.Functions.hiringOPL(self, testName)

    # filter by Pending
    buttonStatus = 'Pending'
    print('1. ', buttonStatus)
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    time1.sleep(4)

    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    try: 
      if checkEmpty == False:
        tableText = driver.find_element_by_id("table_info").text
        systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
        checkNumError = Functions.Functions.checkStatusList(driver,checkNumError, listAssessee, buttonStatus)
      else:
        print("There are no " + buttonStatus + " assessees.")
    except AssertionError as e:
      self.verificationErrors.append(str(e))

    Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    # filter by Hired
    buttonStatus = 'Hired'
    print('2. ', buttonStatus)
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[2]/label[1]").click()
    time1.sleep(4)

    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    try: 
      if checkEmpty == False:
        tableText = driver.find_element_by_id("table_info").text
        systemAssessee, listAssessee =Functions.Functions.howmanyAssesseeListSystem(tableText)
        checkNumError = Functions.Functions.checkStatusList(driver,checkNumError, listAssessee, buttonStatus)
      else:
        print("There are no " + buttonStatus + " assessees.")
    except AssertionError as e:
      self.verificationErrors.append(str(e))

    Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    # filter by Hired
    buttonStatus = 'Not hired'
    print('3. ', buttonStatus)
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[2]/label[1]").click()
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[3]/label[1]").click()
    time1.sleep(4)

    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    try: 
      if checkEmpty == False:
        tableText = driver.find_element_by_id("table_info").text
        systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
        checkNumError = Functions.Functions.checkStatusList(driver,checkNumError, listAssessee, buttonStatus)
      else:
        print("There are no " + buttonStatus + " assessees.")
    except AssertionError as e:
      self.verificationErrors.append(str(e))

    Functions.Functions.checkForError(checkNumError, testName)

  def test_FilterbyDateRange(self):
    checkNumError = 0
    testName = "'Filter by Date Range'"
    driver = Functions.Functions.hiringOPL(self, testName)

    ############################################## testing 'Last 7 Days'
    buttonStatus = 'Last 7 Days'
    print('1. ' + buttonStatus)
    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
    # click "last 7 days"
    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[1]").text
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[1]").click()

    time1.sleep(7)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

    # check if filter has the specific duration of the month
    # click "select Date Range"
    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates,checkNumError)

    tothis = date.today()
    # calculate what would be the beginning range to compare with
    fromthis = tothis + timedelta(-6)
    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    if checkEmpty == False:
      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    #############################################testing 'Last 30 Days'
    buttonStatus = 'Last 30 Days'
    print('2. ' + buttonStatus)
    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
    # click "last 30 days"
    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[2]").text
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[2]").click()

    time1.sleep(7)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

    # check if filter has the specific duration of the month
    # click "select Date Range"
    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates,checkNumError)

    tothis = date.today()
    # calculate what would be the beginning range to compare with
    fromthis = tothis + timedelta(-29)
    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    if checkEmpty == False:
      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    ############################################## testing 'this Month'
    buttonStatus = 'This Month'
    print('3. ' + buttonStatus)
    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
    # click "Last 6 Months"
    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[3]").text
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[3]").click()

    time1.sleep(7)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

    # check if filter has the specific duration of the month
    # click "select Date Range"
    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates, checkNumError)

    # end date range to compare with
    tothis = date.today()
    # calculate what would be the beginning range to compare with
    fromthis1 = str(tothis.month)
    fromthis2 = str(1)
    fromthis3 = str(tothis.year)
    fromthis = fromthis1 + fromthis2 + fromthis3
    # put it as date form
    fromthis = datetime.strptime(fromthis, '%m%d%Y')
    fromthis = fromthis.date()
    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    if checkEmpty == False:
      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    ############################################## testing 'last 6 months'
    buttonStatus = 'Last 6 months'
    print('4. ' + buttonStatus)

    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
    # click "Last 6 Months"
    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[4]").text
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[4]").click()

    time1.sleep(7)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

    # check if filter has the specific duration of the month
    # click "select Date Range"
    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates, checkNumError)

    # end date range to compare with
    tothis = date.today()
    # calculate what would be the beginning range to compare with
    if tothis.month < 6:
      fromthis1 = str(tothis.month + 12 - 5)
      fromthis2 = str(1)
      fromthis3 = str(tothis.year - 1)
    else:
      fromthis1 = str(tothis.month - 5)
      fromthis2 = str(1)
      fromthis3 = str(tothis.year)

    fromthis = fromthis1 + fromthis2 + fromthis3
    # put it as date form
    fromthis = datetime.strptime(fromthis, '%m%d%Y')
    fromthis = fromthis.date()
    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')
    if checkEmpty == False:
      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    ############################################# testing 'Custom Range'
    buttonStatus = 'Custom Range'
    print('5. ' + buttonStatus)
    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").click()
    # click "Custom Range"
    selectedDateRange = driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[6]").text
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/ul[1]/li[6]").click()

    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_start_input']/input[@class='input-mini']").clear()
    time1.sleep(2)
    fromthis = "01/05/2016"
    tothis = "08/05/2016"
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_start_input']/input[@class='input-mini']").send_keys(fromthis)
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_start_input']/input[@class='input-mini']").send_keys(Keys.TAB)
    time1.sleep(2)

    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_end_input']/input[@class='input-mini']").clear()
    time1.sleep(1)
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_end_input']/input[@class='input-mini']").send_keys(tothis)
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/div[@class='daterangepicker_end_input']/input[@class='input-mini']").send_keys(Keys.TAB)
    time1.sleep(1)
    # click apply
    driver.find_element_by_xpath("//body/div[7]/div[@class='ranges']/div[@class='range_inputs']/button[1]").click()
    # check if filter has the specific duration of the month
    # click "select Date Range"
    checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusContainer']//div[@id='dateRange']").text
    checkNumError = Functions.Functions.hiringEmptyCheck(checkDates, checkNumError)

    # change RANGE DATES to date form
    fromthis = datetime.strptime(fromthis, '%m/%d/%Y')
    fromthis = fromthis.date()
    tothis = datetime.strptime(tothis, '%m/%d/%Y')
    tothis = tothis.date()
    checkEmpty = HiringStatusPage.is_element_present(self, By.XPATH, '//div[@id="hiringStatusContainer"]/div/div[2]/div[4]//tbody/tr[1]/td[@class="dataTables_empty"]')

    if checkEmpty == False:
      checkNumError = Functions.Functions.checkDateList(driver, checkNumError, listAssessee, tothis, fromthis)
      Functions.Functions.hiringButtonCheck(checkNumError, buttonStatus)

    Functions.Functions.checkForError(checkNumError, testName)

  def test_FilterBySupervisor(self):
    ##PUT THE code to verify total number of entries with summation of each status entries
    checkNumError = 0
    testName = "'Filter By Supervisor'"
    driver = Functions.Functions.hiringOPL(self, testName)

    supervisorname = ["Young Kim", "Kendra Barnett", "Marley Bee"]

    for i in range(0,3):
      driver.find_element_by_id("supervisorSearch-tokenfield").send_keys(supervisorname[i])
      time1.sleep(1)
      driver.find_element_by_id("supervisorSearch-tokenfield").send_keys(Keys.ARROW_DOWN)
      driver.find_element_by_id("supervisorSearch-tokenfield").send_keys(Keys.ENTER)
      time1.sleep(2)

      tableText = driver.find_element_by_id("table_info").text
      systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)

      str1 = str("//tbody/tr[")
      str3 = str("]/td[3]//span[@class='dt-supervisor-name']")

      for j in range(1, listAssessee+1):
        str2 = str(j)
        str_element = str1 + str2 + str3
        check = driver.find_element_by_xpath(str_element).text
        if check != supervisorname[i]:
            checkNumError += 1
      driver.find_element_by_xpath("//div[@class='input-group']//div//div/a[@class ='close']").click()
    time1.sleep(1)

    Functions.Functions.checkForError(checkNumError, testName)

  def test_HiringSomeone(self):
    checkNumError = 0
    testName = "'Hiring Someone'"
    driver = Functions.Functions.hiringOPL(self, testName)

    # filter by pending to only view pending assesseess
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    time1.sleep(2)
    driver.find_element_by_xpath("//div[@class='btn-group']/a").click()
    driver.find_element_by_xpath("//ul[@class='dropdown-menu']//a").click()
    time1.sleep(1)
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='container-fluid']/div[2]/div[1]/div[2]/div[1]").click()
    time1.sleep(1)
    originalHiredAlert = "Once changed to Hired, Hiring Status cannot be reverted back to Not Hired. Proceed with this change?"
    checkHiredAlert = driver.find_element_by_xpath("//div[@class='bootbox modal fade in']//div[@class='bootbox-body']").text
    
    # check if hiredalert was given
    if checkHiredAlert != originalHiredAlert:
      checkNumError += 1
      errorMessage = str("'Hired Alert' is different")
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + errorMessage)

    driver.find_element_by_xpath("//div[@class='bootbox modal fade in']//div[@class='modal-footer']/button[1]").click()
    time1.sleep(2)
    # click the calendar to put hired date
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[3]/div[1]/div[1]/div[1]").click()
    # click the number on the first row
    driver.find_element_by_xpath("//body/div[6]//table[@class='table-condensed']/tbody/tr[2]/td[2]").click()
    # put the supervisor name
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//input[@id='supervising_contact_id-tokenfield']").send_keys("Young Kim")
    time1.sleep(1)
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//input[@id='supervising_contact_id-tokenfield']").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//input[@id='supervising_contact_id-tokenfield']").send_keys(Keys.ENTER)
    # may we contact the supervisor? -> Yes
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='container-fluid']/div[12]/div[1]/label[1]/div[1]").click()
    # Save it
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//div[@class='modal-footer']/button[1]").click()
    time1.sleep(2)
    checkStatus = driver.find_element_by_xpath("//tbody/tr[1]/td[4]").text
    assesseeName = driver.find_element_by_xpath("//tbody/tr[1]/td[2]/div/div").text
    # check if hired assesseename has been removed from the list (remember that I clicked the "Pending")
    # if the assesseename is still on the list, it is the error
    
    # if checkStatus != 'Hired':
    #   checkNumError += 1
    #   colorama.init(autoreset=True)
    #   print(colorama.Fore.RED + 'Hired button does not work')

    print("Check Hired data in Pivotal if " + assesseeName + " has been marked as 'Hired' or not.")
    Functions.Functions.checkForError(checkNumError, testName)
  
  def test_DontHiringSomeone(self):
    checkNumError = 0
    testName = "'Don't Hire Someone'"
    driver = Functions.Functions.hiringOPL(self, testName)

    # filter by pending to only view pending assesseess
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    time1.sleep(1)
    # open frame
    driver.find_element_by_xpath("//tbody/tr[1]//div[@class='btn-group']/a").click()
    driver.find_element_by_xpath("//ul[@class='dropdown-menu']//a").click()
    time1.sleep(2)
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='container-fluid']/div[2]/div[1]/div[2]/div[2]").click()
    time1.sleep(1)

    # Save it
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//div[@class='modal-footer']/button[1]").click()
    time1.sleep(2)
    checkStatus = driver.find_element_by_xpath("//tbody/tr[1]/td[4]").text
    time1.sleep(1)
    # check if hired assesseename has been removed from the list (remember that I clicked the "Pending")
    # if the assesseename is still on the list, it is the error
    if checkStatus != 'Not hired':
      checkNumError += 1
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + 'Not Hired button does not work')

    Functions.Functions.checkForError(checkNumError, testName)

  def test_RetireSomeone(self):
    checkNumError = 0
    testName = "'Retire Someone'"
    driver = Functions.Functions.hiringOPL(self, testName)
    # filter by Hired to only view Hired assesseess
    driver.find_element_by_xpath("//div[@id = 'hiringStatusContainer']/div[1]/div[1]/div[1]/div[2]/label[1]").click()
    time1.sleep(2)
    # how many assessees are in list?
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    i = 1

    # open 1st assessee  frame
    assesseeName = driver.find_element_by_xpath("//tbody/tr[%d]/td[2]/div/div" % (i)).text
    driver.find_element_by_xpath("//tbody/tr[%d]//div[@class='btn-group']/a" % (i)).click()
    time1.sleep(1)
    driver.find_element_by_xpath("//ul[@class='dropdown-menu']//a").click()
    time1.sleep(1)

    leavingDate = driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[4]/div[1]/div[1]").text

    # while the leaving date is Not empty, go to next assessee and do it.
    while leavingDate != "":
      # click cancel
      driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//div[@class='modal-footer']/button[@id='hiringStatusCancelButton']").click()
      time1.sleep(2)
      # proceed to next assessee
      i += 1
      # save next assesseeName
      assesseeName = driver.find_element_by_xpath("//tbody/tr[%d]/td[2]/div/div" % (i)).text
      # open assessee's frame
      driver.find_element_by_xpath("//tbody/tr[%d]//div[@class='btn-group']/a" % (i)).click()
      driver.find_element_by_xpath("//tbody/tr[%d]//ul[@class='dropdown-menu']//a" % (i)).click()
      time1.sleep(1)
      leavingDate = driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[4]/div[1]/div[1]").text
      # if i is out of range in list, then click next list and reset i as 1.
      if i == listAssessee:
        driver.find_element_by_xpath("//div[@id='table_paginate']//li[@class='next']/a[1]").click()
        i = 1
    
    time1.sleep(1)  
    # if assesse is NOT retired,click Leaving Date Calendar
    driver.find_element_by_xpath("//div[@id='separation_date_row']//div[@id='separation_date']").click()
    time1.sleep(2)
    # click 2nd Wednesday of the month
    driver.find_element_by_xpath("//body/div[5]//table[@class='table-condensed']/tbody/tr[2]/td[4]").click()
    time1.sleep(2)
    # click voluntary
    driver.find_element_by_xpath("//div[@id='leaving_reason_row']/div[1]/div[2]/div[1]").click()
    # click save
    driver.find_element_by_xpath("//div[@id='hiringStatusDlg']//div[@class='modal-footer']/button[1]").click()
    time1.sleep(1)

    # # check if the date is there.
    # checkDates = driver.find_element_by_xpath("//div[@id='hiringStatusDlg']/div[1]/div[1]/div[@class='modal-body']/div[2]/div[4]/div[1]/div[1]/div[1]").text
    # if checkDates == []:
    #    checkNumError += 1
    # time1.sleep(1)

    print("Check Hired data in Pivotal if " + assesseeName + " is retired or not.")
    Functions.Functions.checkForError(checkNumError, testName)
  
  def test_searchForAssessee(self):
    checkNumError = 0
    testName = "'Search For Assessee'"
    driver = Functions.Functions.hiringOPL(self, testName)

    str1 = str("//body/div[@id='main-content']/div[@id='hiringStatusContainer']/div/div[2]/div[4]//table[@id='table']/tbody/tr[")
    str2 = str(1)
    str3 = str("]/td[2]/div/div")
    str_element = str1 + str2 + str3
    existAssesseeName = driver.find_element_by_xpath(str_element).text
    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']/div/div[2]/div/div[2]//input[@id='mainSearch']").send_keys(existAssesseeName)
    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']/div/div[2]/div/div[2]//input[@id='mainSearch']").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath("//div[@id='hiringStatusContainer']/div/div[2]/div/div[2]//input[@id='mainSearch']").send_keys(Keys.ENTER)
    time1.sleep(2)

    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(1)
    for j in range(1, listAssessee+1):
      str2 = str(j)
      str_element = str1 + str2 + str3
      check = driver.find_element_by_xpath(str_element).text
      if check != existAssesseeName:
        checkNumError += 1

    Functions.Functions.checkForError(checkNumError, testName)

  def test_sortingDropdown(self):
    checkNumError = 0
    testName = "'Sorting Dropdown'"
    driver = Functions.Functions.hiringOPL(self, testName)

    whatToSort = 'Name'
    print('1. Sort by', whatToSort)
    driver.find_element_by_class_name("data-grid-filter").click()
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_DOWN)
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ENTER)
    time1.sleep(5)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(2)
    checkNumError = HiringStatusPage.sortingCheck(driver, whatToSort, listAssessee, checkNumError)
    if checkNumError != 0:
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + whatToSort + str(" button doesn't work"))

    whatToSort = 'Date'
    print('2. Sort by', whatToSort)
    driver.find_element_by_class_name("data-grid-filter").click()
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_UP)
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ENTER)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(2)
    checkNumError = HiringStatusPage.sortingCheck(driver, whatToSort, listAssessee, checkNumError)
    if checkNumError != 0:
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + whatToSort + str(" button doesn't work"))

    whatToSort = 'Supervisor'
    print('3. Sort by', whatToSort)
    driver.find_element_by_class_name("data-grid-filter").click()
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ARROW_DOWN)
    time1.sleep(1)
    driver.find_element_by_class_name("data-grid-filter").send_keys(Keys.ENTER)
    time1.sleep(3)
    tableText = driver.find_element_by_id("table_info").text
    systemAssessee, listAssessee = Functions.Functions.howmanyAssesseeListSystem(tableText)
    time1.sleep(5)
    
    checkNumError = HiringStatusPage.sortingCheck(driver, whatToSort, listAssessee, checkNumError)
    if checkNumError != 0:
      colorama.init(autoreset=True)
      print(colorama.Fore.RED + whatToSort + str(" button doesn't work"))

    Functions.Functions.checkForError(checkNumError, testName)

if __name__ == "__main__":
  unittest.main()
