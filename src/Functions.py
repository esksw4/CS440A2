import re, string, sys
import colorama
import time as time1
import collections

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import tkinter
from tkinter import *

class Functions:
	global timeAfterLogin
	timeAfterLogin = 7

	global OPLInfo
	OPLInfo = collections.OrderedDict()

	global CustomInfo
	CustomInfo = collections.OrderedDict()

	global GUImainFrame
	GUImainFrame = None

	global GUIdisplay
	GUIdisplay = None

	global GUIEvaluationText
	GUIEvaluationText = None

	global GUIallFieldError
	GUIallFieldError = None

	def checkForError(checkNumError, testName):
		colorama.init(autoreset=True)
		print(colorama.Fore.BLACK + colorama.Back.YELLOW + str(testName) + " with " + str(checkNumError) + " error(s).")

# Hiring Stauts
	# Used inside of "sortingCheck" function
	def compareAlphabeticOrder(f, l, mustbesmaller, mustbelarger):
	    if mustbesmaller == mustbelarger:
	      returnthis = 1
	      return returnthis
	    if ord(mustbesmaller[f][l]) == ord(mustbelarger[f][l]):   
	        while l < min(len(mustbesmaller[f]), len(mustbelarger[f]))-1:
	          l += 1
	          whatReturned = Functions.compareAlphabeticOrder(f,l,mustbesmaller,mustbelarger)
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
	            # print('assessee names are same')
	            returnthis = 1
	            return returnthis
	          else:
	            #print('4')
	            Functions.compareAlphabeticOrder(f-1,0,mustbesmaller,mustbelarger)
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

	# Used inside of "sortingCheck" function, Test_SortingDropdown, Test_SearchForAssessee, Test_HiringFunction, Test_Filters
	def howmanyAssesseeListSystem(tableText):
	    tableText = re.split('\s+', tableText)
	    global systemAssessee, listAssessee
	    systemAssessee = int(tableText[5])
	    listAssessee = int(tableText[3]) - int(tableText[1]) + 1
	    return systemAssessee, listAssessee

	# Used in Test_SortingDropdown
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

	        alphabeticWorks = Functions.compareAlphabeticOrder(1, 0, mustbesmaller, mustbelarger)

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
	        alphabeticWorks = Functions.compareAlphabeticOrder(1, 0, mustbesmaller, mustbelarger)
	        #print(alphabeticWorks)
	        
	        if alphabeticWorks == 0:
	          checkNumError += 1
	          return checkNumError
	        else:
	          i += 1
	    
	    return checkNumError

	# Used in Test_Filters
	def checkStatusList(driver, checkNumError, listAssessee, filterStatus):
	    whatStatus = driver.find_element_by_xpath("//tbody/tr[1]/td[4]/div[1]//div[@class='matchText status']").text

	    if listAssessee == 1 and (whatStatus is filterStatus):
	      return checkNumError

	    elif listAssessee == 1 and (whatStatus is not filterStatus):
	      checkNumError += 1
	      return checkNumError

	    else:
	      for i in range(1, listAssessee+1):
	        whatStatus = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]/div[1]//div[@class='matchText status']" % (i)).text
	        if whatStatus != filterStatus:
	          checkNumError += 1
	          return checkNumError
	      return checkNumError

	# Used in Test_Filters
	def hiringButtonCheck(checkNumError, filterStatus):
		#print("checkNumError: " + str(checkNumError) + ",  FilterStatsu: " + filterStatus)
		if checkNumError > 0:
			colorama.init(autoreset=True)
			print(colorama.Fore.RED + filterStatus + str(" button doesn't work"))

	# Used in Test_Filters
	def hiringEmptyCheck(varToCheckIfEmpty,checkNumError):
		if varToCheckIfEmpty == []:
			checkNumError += 1
		return checkNumError

	# Used in Test_Filters
	def checkDateList(driver, checkNumError, listAssessee, tothis, fromthis):
	    checkdateinRange = driver.find_element_by_xpath("//tbody/tr[1]/td[3]//div[@class='second-line']").text
	    checkdateinRange = datetime.strptime(checkdateinRange, '%m/%d/%Y')
	    checkdateinRange = checkdateinRange.date()

	    if listAssessee == 1 and checkdateinRange >= fromthis and checkdateinRange <= tothis:
	      pass

	    elif listAssessee == 1 and (checkdateinRange <= fromthis or checkdateinRange >= tothis):
	      checkNumError += 1

	    else:
	      for i in range(1, listAssessee+1):
	        time1.sleep(1)
	        #print("i: " + str(i))
	        checkdateinRange = driver.find_element_by_xpath("//tbody/tr[%d]/td[3]//div[@class='second-line']" % (i)).text
	        checkdateinRange = datetime.strptime(checkdateinRange, '%m/%d/%Y')
	        checkdateinRange = checkdateinRange.date()

	        if checkdateinRange < fromthis or checkdateinRange > tothis :
	          checkNumError += 2
	      return checkNumError

	def findWhichRow(driver, byWhat, findValue, listAssessee):
		if byWhat == "Name": 
			row = 1
			check = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]/div[1]/div[@class='main-text assessee-name']" % row).text
			while check != findValue and  row < listAssessee:
				row += 1
				check = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]/div[1]/div[@class='main-text assessee-name']" % row).text
				if row == listAssessee and check != findValue:
					row = 9999

			return row 

	# Used inside of "sortingCheck" function, Test_SortingDropdown, Test_SearchForAssessee, Test_HiringFunction, Test_Filters
	def hiringOPL(self, testName):
		print('Testing ', testName)
		driver = self.driver
		driver.get(GUIdisplay.URL.get())
		# type | id=user_password | 1234567899s
		driver.find_element_by_id("user_password").clear()
		driver.find_element_by_id("user_password").send_keys(OPLInfo['Portal Password'])
		# type | id=user_email | ekim+abc1@calipercorp.com
		driver.find_element_by_id("user_email").clear()
		driver.find_element_by_id("user_email").send_keys(OPLInfo['Portal Username'])
		# click | name=commit |
		driver.find_element_by_id("login-btn").click()
		time1.sleep(timeAfterLogin)

		driver.find_element_by_link_text("Hiring Status").click()
		time1.sleep(2)

		return driver

	# Used inside of function "OPL"
	def is_element_present(driver, how, what):
	    try:
	      driver.find_element(by=how, value=what)
	    except NoSuchElementException as e:
	      return False
	    return True

	def OPL(self, testName):
		import automatedApplicaitonGUI

		# print('Testing ', testName)
		# print(GUIdisplay.URL.get())
		driver = self.driver
		
		driver.get(GUIdisplay.URL.get())

		driver.find_element_by_id("user_email").clear()
		driver.find_element_by_id("user_email").send_keys(OPLInfo['Portal Username'])
		# type User Password
		driver.find_element_by_id("user_password").clear()
		driver.find_element_by_id("user_password").send_keys(OPLInfo['Portal Password'])
		# click Ente
		driver.find_element_by_id("login-btn").click()
		time1.sleep(timeAfterLogin)

		try: 
			time1.sleep(2)
			# print(0)
			if Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-error"):
				# print(Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-error"))
				# print(1)
				GUIdisplay.OPL_Input_Frame_Frame.config(relief=GROOVE)
				# print(2)
				automatedApplicaitonGUI.GUIFunctions.outputDisplayConsole("Please check user's email address/password.", 'e')
				# print(3)
				driver.quit()
				# print(4)

		except:
			time1.sleep(2)
			return driver




#########################WAIT UNTIL THE DRIVER FIND THE ELEMENT
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "C29_W35_V37_V46_btresporg_struct.partner_no-btn")))
#     driver.find_element_by_id("C29_W35_V37_V46_btresporg_struct.partner_no-btn").click()
# except TimeoutException:
#     print("C29_W35_V37_V46_btresporg_struct.partner_no-btn not found")