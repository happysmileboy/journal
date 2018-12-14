from django.shortcuts import render
import urllib.request
from urllib import parse
import json
import csv
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
        if pm < 30:
            color = '#00c9fa'
        elif pm < 80:
            color = '#72da00'
        elif pm < 120:
            color = '#ffbd00'
        elif pm < 200:
            color = '#ff5a00'
        elif pm < 900:
            color = '#ff0000'
        else:
            color = 'black'
        seoul_district[i] = [k, pm, color]
        i += 1
    date = data['ListAirQualityByDistrictService']["row"][0]["MSRDATE"]
    date = date[:4] + "년 " + date[4:6] + "월 " + date[6:8] + "일 " + date[8:10] + "시"
    cs = {'seoul_district': seoul_district, 'date': date}

    return render(request, "home.html", cs)


def get_data_k(request):
    url = "http://kweather.co.kr/data/AIR/AIRMAP_DATA.json"
    with urllib.request.urlopen(url) as response:
        dc = json.loads(response.read().decode("utf-8"))
        ls = dc["list"][0]["sList"]

    f = open('seoul_k.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(['name', 'lat', 'lon', 'val', 'clr'])
    for x in ls:
        if int(x["pm10Val"]) < 30:
            color = 'rgb(0,201,250)'
        elif int(x["pm10Val"]) < 80:
            color = 'rgb(116,217,0)'
        elif int(x["pm10Val"]) < 120:
            color = 'rgb(255,189,0)'
        elif int(x["pm10Val"]) < 200:
            color = 'rgb(255,90,0)'
        elif int(x["pm10Val"]) < 900:
            color = 'rgb(255,0,0)'
        else:
            color = 'rgb(0,0,0)'
        wr.writerow([x["sName"], x["sLat"], x["sLon"], x["pm10Val"], color])
    f.close()

