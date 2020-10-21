from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import folium
from django.core.paginator import Paginator
import requests
import json

from django.core.paginator import Paginator

from pymongo import MongoClient
# Create your views here.

def index(request):
    #return HttpResponse("/board/list 로 가세요:)")
    return render(request, 'board/firstpage.html')   

def boardlist(request): 
   
    data = request.GET.copy()

    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        mt_list = list(client.mt_db.mt_col.find({}))
        # datas['mt_list'] = mt_list
    # data2 = {'mt_list' : mt_list}
    paginator = Paginator(mt_list, 10)
    page_number = request.GET.get('page', 1)
    data3 = {'page_obj' : paginator.get_page(page_number)}

    # return render(request, 'board/mtlist_fromdb.html', context=datas)  
    return render(request, 'board/mtlist_fromdb.html', {'page_obj' : paginator.get_page(page_number)})  


def goodpricelist(request): 
    datas={}  
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        gp_list = list(client.mt_db.goodp_col.find({}))
        
        datas['gp_list'] = gp_list


    return render(request, 'board/goodprice.html', context=datas)

def goodpriceview(request,ADDRESS): 
    datas={}  
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        gp_list = list(client.mt_db.goodp_col.find({'ADDRESS':ADDRESS}))
        datas['gp_list'] = gp_list
        title =gp_list[0]['TITLE']
        sector =gp_list[0]['SECTOR']
        tel =gp_list[0]['TEL']
        lat=gp_list[0]['X']
        lon=gp_list[0]['Y']
        print(lat,lon)
        lat_long = [lat, lon]
        m = folium.Map(lat_long, zoom_start=10)
        popText = folium.Html(f'<b>{title}({sector})</b></br>'+f'<b>{tel}</b></br>', script=True)
        popup = folium.Popup(popText, max_width=2650)
        folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
        m = m._repr_html_()
        # folium 한글 깨짐 현상 발생시 아래 패키지 설치
        # pip install git+https://github.com/python-visualization/branca.git@master
        datas['mountain_map'] = m
        
    return render(request, 'board/goodpriceview.html', context=datas)        

def boardview(request,NAME):
    
    datas={}
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        mt_list = list(client.mt_db.mt_col.find({'NAME':NAME}))
        
        name=mt_list[0]['NAME']
        height=mt_list[0]['HEIGHT']
        area=mt_list[0]['AREA']
        no=mt_list[0]['NO']
        lat=mt_list[0]['LAT']
        lon=mt_list[0]['LON']
        print(lat,lon)
        lat_long = [lat, lon]
        m = folium.Map(lat_long, zoom_start=10)
        popText = folium.Html(f'<b>{name}&nbsp;({height}m)</b></br>'+f'<b>{area}</b></br>', script=True)
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


def goodpricelist(request): 
       
    data = request.GET.copy()

    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        goop_list = list(client.mt_db.goodp_col.find({}))
    paginator = Paginator(goop_list, 10)
    page_number = request.GET.get('page', 1)
    data1 = {'page_obj' : paginator.get_page(page_number)}

    # return render(request, 'board/mtlist_fromdb.html', context=datas)  
    return render(request, 'board/goodprice.html', {'page_obj' : paginator.get_page(page_number)})


def goodpriceview(request,ADDRESS): 
    datas={}  
    with MongoClient("mongodb://127.0.0.1:27017/") as client:
        gp_list = list(client.mt_db.goodp_col.find({'ADDRESS':ADDRESS}))
        datas['gp_list'] = gp_list

    return render(request, 'board/goodpriceview.html', context=datas)        

   
    
