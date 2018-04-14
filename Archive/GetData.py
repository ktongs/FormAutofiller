import string
from random import *
from splinter import Browser
import csv

#Sign up for account
# driver = webdriver.Chrome(executable_path=r"C:\Users\Kingsley\Dropbox\Kingsley\Project\Scraper\chromedriver.exe")

browser = Browser('chrome')
browser.visit('https://onlineservices-servicesenligne-cic.fjgc-gccf.gc.ca/mycic/gccf?lang=eng&idp=gckey&svc=/mycic/start')
browser.find_by_xpath("//a[@title='Sign Up / Register for a new GCKey']").click() #Need to check if it's full screen or not full screen
browser.find_by_name('_eventId_accept').click()

#Generate random password
min_char = 8
max_char = 16
userIDChar = string.ascii_letters + string.digits
passwordChar = string.ascii_letters + string.punctuation + string.digits
#Generate ID and Password
userID = "".join(choice(userIDChar) for x in range(randint(min_char, max_char)))
password = "".join(choice(passwordChar) for x in range(randint(min_char, max_char)))

browser.fill('uid', userID)
browser.find_by_name('_eventId_submit').click()

count = 0
while (browser.is_text_present('Create Your Password')== False and count <=2):
    print ('Invalid name, make new ID. count = ',count)
    userID = "".join(choice(userIDChar) for x in range(randint(min_char, max_char)))
    browser.fill('uid', userID)
    browser.find_by_name('_eventId_submit').click()
    count += 1
if browser.is_text_present('Create Your Password'):
    print ("Success!")
    print('This is your userID : ', userID)

else:
    print ('I gave up making userID.')

browser.fill('password', password)
browser.fill('confirmPassword', password)
browser.find_by_name('_eventId_submit').click()

while (browser.is_text_present('Create Your Recovery Questions, Answers and Hints')== False and count <=5):
    password = "".join(choice(passwordChar) for x in range(randint(min_char, max_char)))
    print ('Invalid password, make new password. count = ',count)
    print('New password:',password)
    browser.fill('password', password)
    browser.fill('confirmPassword', password)
    browser.find_by_name('_eventId_submit').click()
    count += 1
if browser.is_text_present('Create Your Recovery Questions, Answers and Hints'):
    print ("Success!")
    print('This is your password : ', password)

else:
    print ('I gave up making password.')

#Set up recovery questions
recoveryQuestion = 'Pet'
recoveryAnswer = 'answer 1'
memorablePerson = 'answer 2'
memorableDate = '20000101'
browser.find_by_id('recoveryQuestion').select('2')
browser.fill('recoveryAnswer', recoveryAnswer)
browser.fill('memorablePerson', memorablePerson)
browser.fill('memorableDate', memorableDate)
print('Done!')

#Read/Write Account List
def updateAccountLog(data, path):
    with open(path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)

accountData = [userID, password, recoveryAnswer, memorablePerson, memorableDate]
accountlogPath = 'C:\\Users\\Kingsley\\Dropbox\\Kingsley\\Project\\Scraper\\AccountLog.csv'
updateAccountLog(data = accountData,path = accountlogPath)

# browser.quit()