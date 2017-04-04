import re, string, sys
import colorama
import time as time1

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Functions:
	global timeAfterLogin
	timeAfterLogin = 7

	global orderNewReportResult
	orderNewReportResult = {}

	# global orderNewReportCheckErrorMsg
	# orderNewReportCheckErrorMsg = None

	# global GUIuserInputErrorRow_Frame
	# GUIuserInputErrorRow_Frame = None

	global GUImainFrame
	GUImainFrame = None

	# global GUIdisplay
	# GUIdisplay = None

	# global GUIConsoleText
	# GUIConsoleText = None

	global GUIEvaluationText
	GUIEvaluationText = None

	# global GUIuserInputFrame
	# GUIuserInputFrame = None

	# global GUIconsoleFrame
	# GUIconsoleFrame = None

	global GUIallFieldError
	GUIallFieldError = None

	def checkForError(checkNumError, testName):
		colorama.init(autoreset=True)
		print(colorama.Fore.BLACK + colorama.Back.YELLOW + str(testName) + " with " + str(checkNumError) + " error(s).")

	def hiringOPL(self, testName):
		print('Testing ', testName)
		driver = self.driver
		driver.get(self.base_url)
		# type | id=user_password | 1234567899s
		driver.find_element_by_id("user_password").clear()
		driver.find_element_by_id("user_password").send_keys("123456789")
		# type | id=user_email | ekim+abc1@calipercorp.com
		driver.find_element_by_id("user_email").clear()
		driver.find_element_by_id("user_email").send_keys("ekim+abc1@calipercorp.com")
		# click | name=commit |
		driver.find_element_by_id("login-btn").click()
		time1.sleep(timeAfterLogin)

		driver.find_element_by_link_text("Hiring Status").click()
		time1.sleep(2)

		return driver

	def hiringButtonCheck(checkNumError, filterStatus):
		#print("checkNumError: " + str(checkNumError) + ",  FilterStatsu: " + filterStatus)
		if checkNumError > 0:
			colorama.init(autoreset=True)
			print(colorama.Fore.RED + filterStatus + str(" button doesn't work"))

	def hiringEmptyCheck(varToCheckIfEmpty,checkNumError):
		if varToCheckIfEmpty == []:
			checkNumError += 1
		
		return checkNumError

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






	def howmanyAssesseeListSystem(tableText):
	    tableText = re.split('\s+', tableText)
	    global systemAssessee, listAssessee
	    systemAssessee = int(tableText[5])
	    listAssessee = int(tableText[3]) - int(tableText[1]) + 1
	    return systemAssessee, listAssessee

	def OPL(self, testName):
		print('Testing ', testName)
		driver = self.driver

		## can use it after zoom out
		# driver.set_window_size(600,400)

		## NEED TO ZOOM OUT!
		# html = driver.find_element(By.TAG_NAME,'html');
		# html.send_keys(Keys.Chord(Keys.CONTROL, Keys.ADD))
		
		driver.get("https://portal.calipercorp.com/users/sign_in")

		driver.find_element_by_id("user_email").clear()
		driver.find_element_by_id("user_email").send_keys("ekim+ABC1@calipercorp.com")
		# type User Password
		driver.find_element_by_id("user_password").clear()
		driver.find_element_by_id("user_password").send_keys("123456789")
		# click Ente
		driver.find_element_by_id("login-btn").click()
		time1.sleep(timeAfterLogin)

		return driver



#########################WAIT UNTIL THE DRIVER FIND THE ELEMENT
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "C29_W35_V37_V46_btresporg_struct.partner_no-btn")))
#     driver.find_element_by_id("C29_W35_V37_V46_btresporg_struct.partner_no-btn").click()
# except TimeoutException:
#     print("C29_W35_V37_V46_btresporg_struct.partner_no-btn not found")