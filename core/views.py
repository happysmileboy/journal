from django.shortcuts import render
import urllib.request
from urllib import parse
import json
# Create your views here.


def home(request):
    seoul_district = {}
    url = "http://openapi.seoul.go.kr:8088/4543496e6b743335343742466c496d/json/ListAirQualityByDistrictService/1/25"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
    i = 1
    for x in data['ListAirQualityByDistrictService']['row']:
        k = x["MSRSTENAME"]
        try:
            pm = int(x["PM10"])
        except:
            pm = 1000
        if pm < 40:
            color = 'green'
        elif pm < 50:
            color = 'yellow'
        elif pm < 999:
            color = 'red'
        else:
            color = 'black'
        seoul_district[i] = [k, pm, color]
        i+=1
    date = data['ListAirQualityByDistrictService']["row"][0]["MSRDATE"]
    date = date[:4] + "년 " + date[4:6] + "월 " + date[6:8] + "일 " + date[8:10] + "시"
    csv = {'seoul_district': seoul_district, 'date':date}
    print(csv)

    return render(request, "home.html", csv)
