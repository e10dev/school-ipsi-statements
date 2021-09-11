from django.contrib.auth import login
from django.http.response import JsonResponse
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import json
from datetime import datetime
from .models import Major
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def mainPage(request):
    todayTime = datetime.today().strftime("%Y-%m-%d")

    majorData = ''
    with open('/var/www/dashboard/firstUI/jsonData/major.json', 'r') as f:
        majorData = json.load(f)

    interestJSONData = ''
    with open('/var/www/dashboard/firstUI/jsonData/interestStudents.json', 'r') as f:
        interestJSONData = json.load(f)["DATA"]

    counselJSONData = ''
    with open('/var/www/dashboard/firstUI/jsonData/counselStudents.json', 'r') as f:
        counselJSONData = json.load(f)["DATA"]

    #print(interestJSONData, counselJSONData)




    ### 관심학과
    interestMajor = []
    for i, item in enumerate(majorData):
        interestMajor.append({"major": item["major"], "data": [0, 0, 0]})

    interestHighSchools = {}
    interestseltAppr = {}
    interestTotal = 0

    for item in interestJSONData:
        if item["sustNm"] != None:
            interestHighSchools[item["schNm"]] = 0
        if item["seltApprNm"] != None:
            interestseltAppr[item["seltApprNm"]] = 0

    for item in interestJSONData:
        interestHighSchools[item["schNm"]] += 1
        if item["seltApprNm"] != None:
            interestseltAppr[item["seltApprNm"]] += 1
        if item["sustNm"] != None:
            interestMajor[next((idx for (idx, data) in enumerate(interestMajor) if data["major"] == item["sustNm"]))]["data"][0] += 1
            interestTotal += 1

    sorted_interestHighSchools = sorted(interestHighSchools.items(), key=lambda item: item[1], reverse=True)[:10]



    ### 상담인원
    counselTotal = 0

    for item in counselJSONData:
        if item["sustNm"] != None:
            interestMajor[next((idx for (idx, data) in enumerate(interestMajor) if data["major"] == item["sustNm"]))]["data"][1] += 1
            counselTotal += 1


    ### 모집인원
    limitTotal = 0

    for item in majorData:
        limitTotal += item["limit"]
        interestMajor[next((idx for (idx, data) in enumerate(interestMajor) if data["major"] == item["major"]))]["data"][2] = item["limit"]


    # 지원 예정 학생 상담 일자
    totalDate = sorted(list(set([item["cnslDt"] for item in counselJSONData])))

    def getDataFunc(totalDate):
        aplyData = [item for item in counselJSONData if int(item["cnslRstCd"]) < 3]
        limitList = [limitTotal] * len(totalDate)
        
        cnslAplyCnt = {}
        cnslTotalCnt = {}

        for item in totalDate:
            cnslAplyCnt[item] = 0
            cnslTotalCnt[item] = 0
        print(cnslAplyCnt)

        for item in sorted(list(set([item["cnslDt"] for item in aplyData if item["cnslDt"] in totalDate]))):
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

        return limitList, applyGradient, councelGradient

    limitList, applyGradient, councelGradient = getDataFunc(totalDate)

    if request.POST:
        getData = request.POST.get('dateList')

        totalDate = sorted(list(set([item["cnslDt"] for item in counselJSONData])))
        tempDate = [datetime.strptime(item, '%Y%m%d') for item in totalDate]
        nowDate = datetime.now()

        if getData != '0':
            totalDate = []
            if getData == '1':
                totalDate = [item.strftime("%Y%m%d") for item in tempDate if (nowDate - item).days <= 30]
                limitList, applyGradient, councelGradient = getDataFunc(totalDate)
            elif getData == '2':
                totalDate = [item.strftime("%Y%m%d") for item in tempDate if (nowDate - item).days <= 90]
                limitList, applyGradient, councelGradient = getDataFunc(totalDate)
            elif getData == '3':
                totalDate = [item.strftime("%Y%m%d") for item in tempDate if (nowDate - item).days <= 180]
                limitList, applyGradient, councelGradient = getDataFunc(totalDate)
        else:
            limitList, applyGradient, councelGradient = getDataFunc(totalDate)

        return JsonResponse({'cnslAplyData':[[item[4:6]+'.'+item[6:8] for item in totalDate], limitList, councelGradient, applyGradient]})

    # majorData 0 : 과 이름, 1 : 관심인원, 2: 모집인원 - 관심인원, 3 : 모집인원
    context = {
        'todayTime': todayTime,
        'totals':[limitTotal, interestTotal, counselTotal],
        'schoolIdx':[item[0] for item in sorted_interestHighSchools],
        'schoolData':[item[1] for item in sorted_interestHighSchools],
        'majorData1':[ [item["major"] for item in interestMajor][:25], [item["data"][0] for item in interestMajor][:25], [item["data"][2] - item["data"][0] for item in interestMajor][:25], [item["data"][2] for item in interestMajor][:25] ],
        'majorData2':[ [item["major"] for item in interestMajor][25:], [item["data"][0] for item in interestMajor][25:], [item["data"][2] - item["data"][0] for item in interestMajor][25:], [item["data"][2] for item in interestMajor][25:] ],
        'interestseltAppr':interestseltAppr,
        'cnslAplyData':[[item[4:6]+'.'+item[6:8] for item in totalDate], limitList, councelGradient, applyGradient]
    }

    return render(request, "index.html", context=context)
















@login_required(login_url='/accounts/login/')
def majorPage(request):
    todayTime = datetime.today().strftime("%Y-%m-%d")

    # Data Initialization
    majorData = ''
    with open('/var/www/dashboard/firstUI/jsonData/major.json', 'r') as f:
        majorData = json.load(f)

    interestJSONData = ''
    with open('/var/www/dashboard/firstUI/jsonData/interestStudents.json', 'r') as f:
        interestJSONData = json.load(f)["DATA"]

    counselJSONData = ''
    with open('/var/www/dashboard/firstUI/jsonData/counselStudents.json', 'r') as f:
        counselJSONData = json.load(f)["DATA"]

    

    # Interest list, cnslRstData
    is_interest_exist = False
    is_cnslRstData_exist = False

    selected_data = ''
    cnslRstData = []
    totals = []
    interestHighSchools = {}
    sorted_interestHighSchools = []
    sorted_seltApprNmData = {}
    listsOfInterest = []
    listsOfCounsel = []


    # 관심학교 Top 10

    if request.POST:
        getData = request.POST.get('majorList')
        if getData != 'None':
            selected_list = Major.objects.filter(id=int(getData[1:-1])).values()
            selected_data = list(selected_list)[0]["name"]
            listsOfInterest = [item for item in interestJSONData if selected_data == item["sustNm"]]
            listsOfCounsel = [item for item in counselJSONData if selected_data == item["sustNm"]]

            # 관심인원 존재 여부 확인
            if len(listsOfInterest) != 0:
                is_interest_exist = True

            # 모집인원, 관심인원, 상담인원
            temp = [item for item in majorData if selected_data == item["major"]]
            print(temp)
            totals = [temp[0]["limit"], len(listsOfInterest), len(listsOfCounsel)]

            # 관심학교 Top 10
            seltApprNm = []
            for item in listsOfInterest:
                interestHighSchools[item["schNm"]] = 0
                if item["seltApprNm"] != None:
                    seltApprNm.append(item["seltApprNm"])

            for item in listsOfInterest:
                interestHighSchools[item["schNm"]] += 1

            if len(interestHighSchools) > 10:
                sorted_interestHighSchools = sorted(interestHighSchools.items(), key=lambda item: item[1], reverse=True)[:10]
            else:
                sorted_interestHighSchools = sorted(interestHighSchools.items(), key=lambda item: item[1], reverse=True)

            # 상담 결과
            cnslRstData = [0, 0, 0, 0]
            for item in listsOfCounsel:
                cnslRstData[int(item["cnslRstCd"]) - 1] += 1
            if cnslRstData != [0, 0, 0, 0]:
                is_cnslRstData_exist = True

            # 지원 전형
            seltApprNmData = {}
            for item in seltApprNm:
                seltApprNmData[item] = 0
            
            for item in seltApprNm:
                seltApprNmData[item] += 1
            sorted_seltApprNmData = sorted(seltApprNmData.items(), key=lambda x : x[1], reverse=True)

    context = {
        'todayTime': todayTime,
        'selected_data': selected_data,
        'all_major': Major.objects.order_by('name'),
        'totals': totals,
        'cnslRstData': cnslRstData,
        'is_interest_exist': is_interest_exist,
        'is_cnslRstData_exist': is_cnslRstData_exist,
        'schoolIdx':[item[0] for item in sorted_interestHighSchools],
        'schoolData':[item[1] for item in sorted_interestHighSchools],
        'seltApprNmData':[[item[0] for item in sorted_seltApprNmData], [item[1] for item in sorted_seltApprNmData]]
    }

    return render(request, "majorPage.html", context=context)






















def ksh(request):
    todayTime = datetime.today().strftime("%Y-%m-%d")

    majorData = ''
    with open('/var/www/dashboard/firstUI/jsonData/major.json', 'r') as f:
        majorData = json.load(f)

    interestJSONData = ''
    with open('/var/www/dashboard/firstUI/jsonData/interestStudents.json', 'r') as f:
        interestJSONData = json.load(f)["DATA"]

    counselJSONData = ''
    with open('/var/www/dashboard/firstUI/jsonData/counselStudents.json', 'r') as f:
        counselJSONData = json.load(f)["DATA"]

    #print(interestJSONData, counselJSONData)




    ### 관심학과
    interestMajor = []
    for i, item in enumerate(majorData):
        interestMajor.append({"major": item["major"], "data": [0, 0, 0]})

    interestHighSchools = {}
    interestseltAppr = {}
    interestTotal = 0

    for item in interestJSONData:
        if item["sustNm"] != None:
            interestHighSchools[item["schNm"]] = 0
        if item["seltApprNm"] != None:
            interestseltAppr[item["seltApprNm"]] = 0

    for item in interestJSONData:
        interestHighSchools[item["schNm"]] += 1
        if item["seltApprNm"] != None:
            interestseltAppr[item["seltApprNm"]] += 1
        if item["sustNm"] != None:
            interestMajor[next((idx for (idx, data) in enumerate(interestMajor) if data["major"] == item["sustNm"]))]["data"][0] += 1
            interestTotal += 1

    sorted_interestHighSchools = sorted(interestHighSchools.items(), key=lambda item: item[1], reverse=True)[:10]



    ### 상담인원
    counselTotal = 0

    for item in counselJSONData:
        if item["sustNm"] != None:
            interestMajor[next((idx for (idx, data) in enumerate(interestMajor) if data["major"] == item["sustNm"]))]["data"][1] += 1
            counselTotal += 1


    ### 모집인원
    limitTotal = 0

    for item in majorData:
        limitTotal += item["limit"]
        interestMajor[next((idx for (idx, data) in enumerate(interestMajor) if data["major"] == item["major"]))]["data"][2] = item["limit"]


    # 지원 예정 학생 상담 일자
    aplyData = [item for item in counselJSONData if int(item["cnslRstCd"]) < 3]
    totalDate = sorted(list(set([item["cnslDt"] for item in counselJSONData])))
    fmtDate = [item[4:6]+'.'+item[6:8] for item in totalDate]
    limitList = [limitTotal] * len(totalDate)

    cnslAplyCnt = {}
    cnslTotalCnt = {}

    for item in totalDate:
        cnslAplyCnt[item] = 0
        cnslTotalCnt[item] = 0

    for item in sorted(list(set([item["cnslDt"] for item in aplyData]))):
        cnslAplyCnt[item] += 1

    for item in sorted([item["cnslDt"] for item in counselJSONData]):
        cnslTotalCnt[item] += 1

    applyGradient = [list(cnslAplyCnt.values())[0]]
    councelGradient = [list(cnslTotalCnt.values())[0]]
    for i, item in enumerate(totalDate[1:], start=1):
        if cnslAplyCnt[item] != 0:
            applyGradient.append(applyGradient[i - 1] + cnslAplyCnt[item])
        else:
            applyGradient.append(applyGradient[i - 1])
        councelGradient.append(councelGradient[i - 1] + cnslTotalCnt[item])

    #majorData 0 : 과 이름, 1 : 관심인원, 2: 모집인원 - 관심인원, 3 : 모집인원

    context = {
        'todayTime': todayTime,
        'totals':[limitTotal, interestTotal, counselTotal],
        'schoolIdx':[item[0] for item in sorted_interestHighSchools],
        'schoolData':[item[1] for item in sorted_interestHighSchools],
        'majorData1':[ [item["major"] for item in interestMajor][:25], [item["data"][0] for item in interestMajor][:25], [item["data"][2] - item["data"][0] for item in interestMajor][:25], [item["data"][2] for item in interestMajor][:25] ],
        'majorData2':[ [item["major"] for item in interestMajor][25:], [item["data"][0] for item in interestMajor][25:], [item["data"][2] - item["data"][0] for item in interestMajor][25:], [item["data"][2] for item in interestMajor][25:] ],
        'interestseltAppr':interestseltAppr,
        'cnslAplyData':[fmtDate, limitList, councelGradient, applyGradient]
    }

    return render(request, "ksh.html", context=context)