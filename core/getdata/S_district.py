import urllib.request
import json
import csv

list_url = "http://kweather.co.kr/air/data/code_data/bcode_arealist.json"
with urllib.request.urlopen(list_url) as response:
    dc = json.loads(response.read().decode("utf-8"))

list_district = []
list_district_keys = []
keylist = list(dc['11']['data'].keys())
# print(keylist)
for x in keylist:
    for y in dc['11']['data'][x]['data']:
        list_district.append(dc['11']['data'][x]['data'][y])
        list_district_keys.append(y)
print(keylist)


district_url = "http://kweather.co.kr/air/data/area_realtime/MAP_"
f = open('../kdata_s.csv', 'w', encoding='utf-8')
wr = csv.writer(f)

for x in keylist:
    with urllib.request.urlopen(district_url + x + ".json") as response:
        dc = json.loads(response.read().decode("utf-8"))
        D_key = list(dc.keys())
        for y in D_key:
            for z in range(1, len(dc[y])-1):
                pm10 = dc[y][z].split("#")[7]
                D_name = dc[y][z].split("#")[1]
                D_lat = dc[y][z].split("#")[4]
                D_lon = dc[y][z].split("#")[5]
                if int(pm10) < 30:
                    color = 'rgb(0,201,250)'
                elif int(pm10) < 80:
                    color = 'rgb(116,217,0)'
                elif int(pm10) < 120:
                    color = 'rgb(255,189,0)'
                elif int(pm10) < 200:
                    color = 'rgb(255,90,0)'
                elif int(pm10) < 900:
                    color = 'rgb(255,0,0)'
                else:
                    color = 'rgb(0,0,0)'
                wr.writerow([D_name, pm10, color, D_lat, D_lon])
f.close()
