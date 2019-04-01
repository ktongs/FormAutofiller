import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    r"C:\Users\Kingsley\Dropbox\Kingsley\Project\Scraper\client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open('Questionaire (Responses)').sheet1

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
