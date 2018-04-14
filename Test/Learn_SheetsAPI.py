import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\Kingsley\Dropbox\Kingsley\Project\Scraper\client_secret.json",scope)
client = gspread.authorize(creds)

sheet = client.open('Questionaire (Responses)').sheet1
responses = sheet.get_all_records()
# print(responses)

row = 2
userID = 'madeupuserid'
password = 'madeuppassword'

user_given_name = sheet.cell(row,2).value
print(user_given_name)

sheet.update_cell(row,6,userID)
sheet.update_cell(row,7,password)