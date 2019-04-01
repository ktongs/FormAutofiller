"""
April 14, 2018
Description: Macro to fill out study permit and temporary visa application using google sheets api
MUST EDIT THE PATH OF CHROMEDRIVER IN ORDER TO COMPILE
REQUIRES 'client_secret.json' FILE FOR GOOGLE SHEETS API
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import string
from random import *
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def Generate_UserID(count):
    min_char = 8
    max_char = 16
    userIDChar = string.ascii_letters + string.digits
    userID =  "".join(choice(userIDChar) for x in range(randint(min_char, max_char)))
    # if count<=1:
    #     userID = 'asd'
    driver.find_element_by_name('uid').send_keys(userID)
    driver.find_element_by_name('_eventId_submit').click()
    newCount = count + 1
    userID = Check_UserID(newCount,userID)
    return userID

def Check_UserID(count,userID):
    try:
        driver.find_element_by_id("password")
        return userID
    except NoSuchElementException:
        if count < 3:
            print('UserID invalid. I will try again. Times tried: ', count)
            driver.find_element_by_id('userID').clear()
            return Generate_UserID(count)
        else:
            print('Creating userID failed.')
            exit()

def Generate_password(count):
    min_char_head = 8; max_char_head = 11
    min_char_tail = 1; max_char_tail = 4
    passwordCharHead = string.ascii_letters
    passwordCharTail = string.digits
    passwordHead = "".join(choice(passwordCharHead) for x in range(randint(min_char_head, max_char_head)))
    passwordTail = "".join(choice(passwordCharTail) for x in range(randint(min_char_tail, max_char_tail)))
    password = passwordHead + passwordTail
    # if count<=1:
    #     password = 'asd'
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('confirmPassword').send_keys(password)
    driver.find_element_by_name('_eventId_submit').click()
    newCount = count + 1
    password = Check_Password(newCount,password)
    return password

def Check_Password(count,password):
    try:
        driver.find_element_by_id('recoveryAnswer')
        return password
    except NoSuchElementException:
        if count < 3:
            print('Password invalid. I will try again. Times tried: ', count)
            driver.find_element_by_name('password').clear()
            driver.find_element_by_name('confirmPassword').clear()
            return Generate_password(count)
        else:
            print('Creating password failed.')
            exit()


def Create_Account ():
    driver.find_element_by_xpath("//*[@title='Sign Up / Register for a new GCKey'][@class='btn btn-primary']").click()
    driver.find_element_by_name('_eventId_accept').click()

def Generate_Recovery_Questions():
    recoveryQuestion = 'Pet'
    recoveryAnswer = 'answer 1'
    memorablePerson = 'answer 2'
    memorableDate = '20000101'
    driver.find_element_by_xpath("//select[@id='recoveryQuestion']/option[@value='2']").click()
    # e1 = driver.find_element_by_id('recoveryQuestion')
    # for option in e1.find_elements_by_tag_name('option'):
    #     if option.text == "What was my first pet's name?":
    #         option.click()
    #         break
    driver.find_element_by_id('recoveryAnswer').send_keys(recoveryAnswer)
    driver.find_element_by_id('memorablePerson').send_keys(memorablePerson)
    driver.find_element_by_id('memorableDate').send_keys(memorableDate)
    driver.find_element_by_name('_eventId_submit').click()
    return (recoveryQuestion,recoveryAnswer,memorablePerson,memorableDate)

def Sign_Up():
    Create_Account()
    userID = Generate_UserID(0)
    password = Generate_password(0)
    [recoveryQuestion, recoveryAnswer, memorablePerson, memorableDate] = Generate_Recovery_Questions()
    driver.find_element_by_id('continue').click() #Finish with account creation
    driver.find_element_by_id('_continue').click()

    return (userID,password,recoveryQuestion, recoveryAnswer, memorablePerson, memorableDate)

def Fill_Name(givenName,lastName,email):
    driver.find_element_by_id('givenName').send_keys(givenName)
    driver.find_element_by_id('familyName').send_keys(lastName)
    driver.find_element_by_id('emailAddress').send_keys(email)
    driver.find_element_by_xpath("//option[@value='3034']").click() #English as language
    driver.find_element_by_id('_continue').click()
def Fill_Security_Questions():
    driver.find_element_by_id('question1').send_keys('Security Question 1')
    driver.find_element_by_id('answer1').send_keys('Answer 1')
    driver.find_element_by_id('question2').send_keys('Security Question 2')
    driver.find_element_by_id('answer2').send_keys('Answer 2')
    driver.find_element_by_id('question3').send_keys('Security Question 3')
    driver.find_element_by_id('answer3').send_keys('Answer 3')
    driver.find_element_by_id('question4').send_keys('Security Question 4')
    driver.find_element_by_id('answer4').send_keys('Answer 4')
    driver.find_element_by_id('_continue').click()

def Fill_Apply_Eligible(countryCode,DoB,province): #Commands to apply for study permit
    driver.get('https://onlineservices-servicesenligne.cic.gc.ca/mycic/home/kitReferenceClaim') # Select apply to come to Canada
    driver.find_element_by_xpath("//input[@title='Visitor visa, study and/or work permit']").click()
    # driver.find_element_by_xpath("//input[@title='Visitor visa, study and/or work permit']").click()
    driver.find_element_by_xpath("//option[@value='7120']").click() #What would you like to do in Canada? = Study
    driver.find_element_by_xpath("//option[@value='7347']").click() #How long are you planning to stay in Canada? = Temporarily >6 months

    #Select the code that matches the one on your passport.
    if countryCode == 'Hong Kong':
        driver.find_element_by_xpath("//option[@value='13401']").click()
    elif countryCode == 'China':
        driver.find_element_by_xpath("//option[@value='13403']").click()

    driver.find_element_by_xpath("//option[@value='2001']").click() #Current country=Canada
    driver.find_element_by_xpath("//option[@value='997']").click() #Canadian family member=No

    yearDict = {}
    for i in range(1913, 2008):
        yearDict[i] = i - 1017
    for i in range(2008, 2011):
        yearDict[i] = i + 895
    for i in range(2011, 2019):
        yearDict[i] = i + 2352

    monthDict = {1:1819,2:1818,3:1822,4:1827,5:1823,6:1821,7:1820,8:1816,9:1826,10:1825,11:1824,12:1817}
    dayDict = {}
    for i in range(1, 32):
        dayDict[i] = i + 546

    [month, day, year] = Date_Str_To_Int(DoB)
    driver.find_element_by_xpath('//option[@value="'+str(yearDict[year])+'"]').click()
    driver.find_element_by_xpath('//option[@value="' + str(monthDict[month]) + '"]').click()
    driver.find_element_by_xpath('//option[@value="' + str(dayDict[day]) + '"]').click()
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click() #Resident of US with Grean Card = No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='7124']").click() #Current status = student
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='4677']").click() #Marital status = single
    if province == 'British Columbia':
        driver.find_element_by_xpath("//option[@value='2721']").click()
    elif province == 'Ontario':
        driver.find_element_by_xpath("//option[@value='2731']").click()
    driver.find_element_by_id('_next').click()
    born = date(year,month,day)
    age = calculate_age(born)
    if province == 'British Columbia':
        if age < 19:
            driver.find_element_by_xpath("//option[@value='997']").click() #Living with parent or guardian = No
            driver.find_element_by_id('_next').click()
    else:
        if age < 18:
            driver.find_element_by_xpath("//option[@value='997']").click()  # Living with parent or guardian = No
            driver.find_element_by_id('_next').click()

def Apply_Study_Permit(expiryDate):
    driver.get('https://onlineservices-servicesenligne.cic.gc.ca/eapp/comeToCanadaHowToApply.do?rtValue=7569&nextQuestionId=994')
    driver.get('https://onlineservices-servicesenligne.cic.gc.ca/eapp/action.do?action=returnToApplication&questionId=994')
    driver.find_element_by_xpath("//option[@value='997']").click() #Accompanying a family member with status in Canada? = No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='7515']").click()  # Apply for work permit = No
    driver.find_element_by_id('_next').click()

    [month,day,year] = Date_Str_To_Int(expiryDate)
    yearDict = {}
    for i in range(2041, 2067):
        yearDict[i] = -i + 20271
    for i in range(2029, 2041):
        yearDict[i] = i + 4802
    for i in range(2011, 2029):
        yearDict[i] = i + 2352
    monthDict = {1: 1819, 2: 1818, 3: 1822, 4: 1827, 5: 1823, 6: 1821, 7: 1820, 8: 1816, 9: 1826, 10: 1825, 11: 1824, 12: 1817}
    dayDict = {}
    for i in range(1, 32):
        dayDict[i] = i + 546

    driver.find_element_by_xpath('//option[@value="' + str(yearDict[year]) + '"]').click()
    driver.find_element_by_xpath('//option[@value="' + str(monthDict[month]) + '"]').click()
    driver.find_element_by_xpath('//option[@value="' + str(dayDict[day]) + '"]').click()
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click() #Had a medical exam performed? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  #Lived in designated country? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  #Submit for family member? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_id('answerlist[0]-radiobutton1').click() #Give someone access to application? = Yes, appointing a rep
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  #Submission letter provided? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='7644']").click()  #Paying fees? =Yes
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='991']").click()  #Digital copy of documents? =Yes
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='991']").click()  #Pay online? =Yes
    driver.find_element_by_id('_next').click()

def Apply_Temporary_Resident_Visa():
    driver.get('https://onlineservices-servicesenligne.cic.gc.ca/eapp/comeToCanadaHowToApply.do?rtValue=7572&nextQuestionId=985')
    driver.get('https://onlineservices-servicesenligne.cic.gc.ca/eapp/action.do?action=returnToApplication&questionId=985')
    driver.find_element_by_xpath("//option[@value='7517']").click()  # Your situation? =I have a study permit
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  # Had a medical exam performed? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  # Lived in designated country? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  # Work in following jobs? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  # Submit for family member? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_id('answerlist[0]-radiobutton1').click()  # Give someone access to application? = Yes, appointing a rep
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='997']").click()  #Submission letter provided? =No
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='7644']").click()  #Paying fees? =Yes
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='991']").click()  #Digital copy of documents? =Yes
    driver.find_element_by_id('_next').click()
    driver.find_element_by_xpath("//option[@value='991']").click()  #Pay online? =Yes
    driver.find_element_by_id('_next').click()

def WriteToSheet(userID, password, recoveryQuestion, recoveryAnswer, memorablePerson, memorableDate,row):
    featureToColumn = {userID:10,password:11,recoveryQuestion:12,recoveryAnswer:13,memorablePerson:14,memorableDate:15}
    for i in featureToColumn.items():
        sheet.update_cell(row,i[1],i[0])

def ReadFromSheet(row):
    firstName = sheet.cell(row, 2).value
    lastName = sheet.cell(row, 3).value
    email = sheet.cell(row, 4).value
    countryFrom = sheet.cell(row, 5).value
    dateOfBirth = sheet.cell(row, 6).value
    provinceTo = sheet.cell(row, 7).value
    statusExpiryDate = sheet.cell(row, 8).value
    application = sheet.cell(row,9).value
    return (firstName,lastName,email,countryFrom,dateOfBirth,provinceTo,statusExpiryDate,application)

def Date_Str_To_Int(dateStr):
    splitDateStr = dateStr.split('/')
    month = int(splitDateStr[0]); day = int(splitDateStr[1]); year = int(splitDateStr[2])
    return month,day,year

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def GetSheetInfo():
    row = input("Enter the row number in 'Questionaire (Responses)' spreadsheet: ")
    return row


if __name__ == '__main__':

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        r"client_secret.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open('Questionaire (Responses)').sheet1

    row = GetSheetInfo()
    [firstName,lastName,email,countryFrom,dateOfBirth,provinceTo,statusExpiryDate,application] = ReadFromSheet(row)

    options = webdriver.ChromeOptions()
    options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' #path to Chrome
    driver = webdriver.Chrome(executable_path=r"..\Drivers\chromedriver.exe",chrome_options=options) #path the chromedriver
    driver.maximize_window()
    url = 'https://onlineservices-servicesenligne-cic.fjgc-gccf.gc.ca/mycic/gccf?lang=eng&idp=gckey&svc=/mycic/start'
    driver.get(url)
    [userID, password, recoveryQuestion, recoveryAnswer, memorablePerson, memorableDate] = Sign_Up()
    Fill_Name(firstName,lastName,email)
    Fill_Security_Questions()
    Fill_Apply_Eligible(countryFrom,dateOfBirth,provinceTo)
    if application == 'Temporary resident visa':
        Apply_Temporary_Resident_Visa()
    elif application == 'Study permit':
        Apply_Study_Permit(statusExpiryDate)

    WriteToSheet(userID,password,recoveryQuestion,recoveryAnswer,memorablePerson,memorableDate,row)

    # input("Press 'enter' to close application.")
    # sys.exit(0)
