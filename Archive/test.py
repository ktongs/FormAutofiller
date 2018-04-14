import csv

def updateAccountLog(data,path):
    with open(path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)

data1 = ['userID','password','recoveryAnswer','memorablePerson','memorableDate']
path2 = 'C:\\Users\\Kingsley\\Dropbox\\Kingsley\\Project\\Scraper\\test.csv'

updateAccountLog(data = data1,path = path2)


# # with open(r'C:\Users\Kingsley\Dropbox\Kingsley\Project\Scraper\AccountLog.csv',encoding='utf-8') as csvfile:
#
#
# data = [1,2,3]
# with open(path,'a',newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(data)
#
#
# # with open('C:\Users\Kingsley\Dropbox\Kingsley\Project\Scraper\AccountLog.csv',encoding='utf-8') as csvfile:
# #     writer = csv.writer(csvfile)
# #     for row in writer:
# #         writer.writerows('test')
#
# #     for column in reader:
# #         # print (column)
# #         # print(lat[0])
# #         if errCheck != 0:
# #             errCheck += 1
# #         else:
# #             lat.insert(count, column['lat'])
# #             lon.insert(count, column['lon'])
# #         count += 1
# #     csvfile.close()
# # print(lat)
# # print(lon)

