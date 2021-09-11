import json
from datetime import datetime
'''
data = {}

with open('/var/www/dashboard/firstUI/jsonData/highschoolGeoData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('/var/www/dashboard/firstUI/jsonData/highschoolGeoData1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent="\t")
'''

counselJSONData = ''
with open('/var/www/dashboard/firstUI/jsonData/counselStudents.json', 'r') as f:
    counselJSONData = json.load(f)["DATA"]

interestJSONData = ''
with open('/var/www/dashboard/firstUI/jsonData/interestStudents.json', 'r') as f:
    interestJSONData = json.load(f)["DATA"]

majorData = ''
with open('/var/www/dashboard/firstUI/jsonData/major.json', 'r') as f:
    majorData = json.load(f)
    
limitTotal = 0

interestMajor = []
for i, item in enumerate(majorData):
    interestMajor.append({"major": item["major"], "data": [0, 0, 0]})

for item in majorData:
    limitTotal += item["limit"]
    interestMajor[next((idx for (idx, data) in enumerate(interestMajor) if data["major"] == item["major"]))]["data"][2] = item["limit"]

totalDate = sorted(list(set([item["cnslDt"] for item in counselJSONData])))
print(totalDate)
test = [datetime.strptime(item, '%Y%m%d') for item in totalDate]
nowDate = datetime.now()


totalDate = []
for idx, item in enumerate(test):
    if (nowDate - item).days <= 30:
        totalDate.append(item.strftime("%Y%m%d"))
        print(item.strftime("%Y%m%d"))


aplyData = [item for item in counselJSONData if int(item["cnslRstCd"]) < 3]
limitList = [limitTotal] * len(totalDate)

cnslAplyCnt = {}
cnslTotalCnt = {}

for item in totalDate:
    cnslAplyCnt[item] = 0
    cnslTotalCnt[item] = 0

print(cnslAplyCnt, cnslTotalCnt)

for item in sorted(list(set([item["cnslDt"] for item in aplyData]))):
    cnslAplyCnt[item] += 1

for item in sorted([item["cnslDt"] for item in counselJSONData if item["cnslDt"] in totalDate]):
    cnslTotalCnt[item] += 1

applyGradient = [list(cnslAplyCnt.values())[0]]
councelGradient = [list(cnslTotalCnt.values())[0]]
for i, item in enumerate(totalDate[1:], start=1):
    if cnslAplyCnt[item] != 0:
        applyGradient.append(applyGradient[i - 1] + cnslAplyCnt[item])
    else:
        applyGradient.append(applyGradient[i - 1])
    councelGradient.append(councelGradient[i - 1] + cnslTotalCnt[item])

print(applyGradient, councelGradient)