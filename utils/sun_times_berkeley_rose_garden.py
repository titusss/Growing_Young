# Gets various timestamps of sun-related events for Berkeley Rose Garden from public API

import requests
import json
from datetime import datetime
import time

def utc2local(utc):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc + offset

dict = {}
for i in range(1, 53):
    print("Week: ", i)
    d = "2022-W" + str(i)
    r = datetime.strptime(d + '-1', "%Y-W%W-%w").date()
    url = "https://api.sunrise-sunset.org/json?lat=37.885592&lng=-122.262403&date=" + str(r)
    print("GET request to: ", url)
    response = requests.get(url)
    res = response.json() # This method is convenient when the API returns JSON
    dict[i] = res
    print(res)
    dict[i]["date"] = str(r)
    for entry in dict[i]["results"]:
        if 'PM' in dict[i]["results"][entry] or 'AM' in dict[i]["results"][entry]: # Check if it's a date format
            print('#### ', entry)
            print('utc: ', dict[i]["results"][entry])
            converted = datetime.strptime(str(r) + ' ' + dict[i]["results"][entry], '%Y-%m-%d %I:%M:%S %p')
            print('converted: ', converted)
            dict[i]["results"][entry] 
            localTime = utc2local(converted)
            dict[i]["results"][entry] = "%s:%s:%s" % (str(localTime.hour), str(localTime.minute), str(localTime.second)) # Remove date
            print('pst: ', dict[i]["results"][entry])
   
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dict, f, ensure_ascii=False, indent=4)
