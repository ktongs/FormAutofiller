yearDict = {}
for i in range(2041, 2067):
    yearDict[i] = -i + 20271
for i in range(2029, 2041):
    yearDict[i] = i + 4802
for i in range(2011, 2029):
    yearDict[i] = i + 2352



print(yearDict[2011])