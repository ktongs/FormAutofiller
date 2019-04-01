from selenium import webdriver
from Test.TalkingToGoogle import WriteToSheet
from Test.TalkingToGoogle import ReadFromSheet

userID = 'user'
password = 'pass'
recoveryQuestion='rq'
recoveryAnswer='ra'
memorablePerson='rp'
memorableDate='rd'
row=10

WriteToSheet(userID,password,recoveryQuestion,recoveryAnswer,memorablePerson,memorableDate,row)
[firstName,lastName,email,countryFrom,dateOfBirth,provinceTo,statusExpiryDate] = ReadFromSheet(2)

print(firstName,lastName,email,countryFrom,dateOfBirth,provinceTo,statusExpiryDate)