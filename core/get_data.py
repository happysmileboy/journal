import urllib.request
import json
import csv

url = "http://kweather.co.kr/data/AIR/AIRMAP_DATA.json"
with urllib.request.urlopen(url) as response:
    dc = json.loads(response.read().decode("utf-8"))
    ls = dc["list"][0]["sList"]

time = ls[0]['uTime']

f = open('../static/seoul_k.csv'.format(ls[0]['uTime']), 'w', encoding='utf-8', newline='')
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

f = open('../kdata.csv', 'a', encoding='utf-8')
wr = csv.writer(f)
li = [x["pm10Val"] for x in ls]

li.insert(0, time)
wr.writerow([x for x in li])
f.close()