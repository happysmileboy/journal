import urllib.request
import json
import csv

list_url = "http://kweather.co.kr/air/data/code_data/bcode_arealist.json"
with urllib.request.urlopen(list_url) as response:
    dc = json.loads(response.read().decode("utf-8"))

list_district = {}
list_district_keys = []
big_district = dc['11']['data']
keylist = list(dc['11']['data'].keys())
# print(keylist)
for x in keylist:
    for y in dc['11']['data'][x]['data']:
        list_district[y] = dc['11']['data'][x]['data'][y]
        list_district_keys.append(y)
# print(big_district)


district_url = "http://kweather.co.kr/air/data/area_realtime/MAP_PAST.php?code="
f = open('../kdata_mean.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(['구','동','평균'])

for x in keylist:
    big_district_name = big_district[x]['name']
    mean_big = 0
    le = 0
    for y in dc['11']['data'][x]['data']:
        with urllib.request.urlopen(district_url + y) as response:
            dc2 = json.loads(response.read().decode("utf-8"))
            ls = dc2['data']
        mean = 0
        for z in ls:
            mean += int(z.split("#")[1])
        mean = int(mean / 24)
        wr.writerow([big_district_name,list_district[y],mean])
        mean_big += mean
        le += 1
    wr.writerow([big_district_name,'', mean_big/le])
    print(big_district_name)

f.close()
