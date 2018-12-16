import urllib.request
import json
import csv

url = "http://openapi.seoul.go.kr:8088/4d69426861743335313335756f7a4364/json/DailyAverageAirQuality/1/122/20181214/"
ls = ["강남구","강남구","강동구", "강북구", '강서구', '관악구','광진구','구로구','금천구',"노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성동구","성북구","송파구","양천구","영등포구","용산구","은평구","종로구", "중구","중랑구"]

url = "http://openAPI.seoul.go.kr:8088/(인증키)/json/ListAirQualityByDistrictService/1/5/ "

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))


f = open('../adata_mean.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(['구','동','평균'])

for x in data['DailyAverageAirQuality']['row']:
    if x['MSRSTE_NM'] in ls:
        wr.writerow([x['MSRSTE_NM'],'',x['PM10']])
