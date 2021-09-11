import json
import requests
import datetime

url='https://rpt.ync.ac.kr:8444/api/cyber/Api.json?fg=1&dataType=json'
data=requests.get(url).json()

with open('/var/www/dashboard/firstUI/jsonData/counselStudents.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent="\t")

url='https://rpt.ync.ac.kr:8444/api/cyber/Api.json?fg=2&dataType=json'
data=requests.get(url).json()

with open('/var/www/dashboard/firstUI/jsonData/interestStudents.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent="\t")

with open('/var/www/dashboard/firstUI/logs/parse.log', 'a') as f:
    f.write("[ "+str(datetime.datetime.now())+" ==> JSON DATA UPDATE SUCCESS! ]\n")