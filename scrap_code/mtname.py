import requests
import json

header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

for num in range (1,101):
    url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={num}'
    res = requests.get(url, headers=header).json()
    cont = res.get("famousMTSDTO")
    mtname=cont.get("stnName")    
    address=cont.get("address")
    lat=cont.get("fmtLat")
    lon=cont.get("fmtLon")
    desc =cont.get("description")


    print(num,mtname,address, lat, lon)

