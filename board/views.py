from django.shortcuts import render
from django.http import HttpResponse
import folium
import requests
import json

from pymongo import MongoClient
# Create your views here.

def index(request):
    #return HttpResponse("/board/list 로 가세요:)")
    return render(request, 'board/firstpage.html')   

def boardlist(request): 
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        mt_list = list(client.mt_db.mt_col.find({'NAME':"지리산"}))
        
        no=mt_list[0]['NO']
        lat=mt_list[0]['LAT']
        lon=mt_list[0]['LON']
        
    lat_long = [lat, lon]  
#    lat_long = [35.3369, 127.7306]
    m = folium.Map(lat_long, zoom_start=10)
    popText = folium.Html('<b>Jirisan</b></br>'+str(lat_long), script=True)
    popup = folium.Popup(popText, max_width=2650)
    folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
    m = m._repr_html_() #  updated

    data = request.GET.copy()
    datas = {'mountain_map': m}
    
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        mt_list = list(client.mt_db.mt_col.find({}))
        
        datas['mt_list'] = mt_list


    return render(request, 'board/mtlist_fromdb.html', context=datas)   


def boardview(request,NAME):
    
    datas={}
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        mt_list = list(client.mt_db.mt_col.find({'NAME':NAME}))
        
        no=mt_list[0]['NO']
        lat=mt_list[0]['LAT']
        lon=mt_list[0]['LON']
        print(lat,lon)
        lat_long = [lat, lon]
        m = folium.Map(lat_long, zoom_start=10)
        popText = folium.Html('<b>Jirisan</b></br>'+str(lat_long), script=True)
        popup = folium.Popup(popText, max_width=2650)
        folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
        m = m._repr_html_() #  updated

        #data = request.GET.copy()
        #ma = {'mountain_map': m}
        header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        url = f'http://mtweather.nifos.go.kr/famous/mountainOne?stnId={no}'
        res = requests.get(url, headers=header).json()
        cont = res.get("famousMTSDTO")  
        weather2 = [cont.get("forestAWS10Min")]
        weather1 = [res.get("others")]    
        
        
        datas['mt_list'] = mt_list
        datas['weather1'] = weather1
        datas['weather2'] = weather2
        datas['mountain_map'] = m
        
    
    return render(request, 'board/boardview.html', context=datas)      
    