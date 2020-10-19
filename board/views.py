from django.shortcuts import render
from django.http import HttpResponse
import folium
from pymongo import MongoClient
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return HttpResponse("/board/list 로 가세요:)")

def boardlist(request):   

    lat_long = [35.3369, 127.7306]
    m = folium.Map(lat_long, zoom_start=10)
    popText = folium.Html('<b>Jirisan</b></br>'+str(lat_long), script=True)
    popup = folium.Popup(popText, max_width=2650)
    folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
    m = m._repr_html_() #  updated
    datas = {'mountain_map': m}
    return render(request, 'board/showmapwithfolium.html', context=datas)    

def detail(request):
    data=request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        gps_db=client.gps_db
        contact_list=list(gps_db.gps_collection.find({}))
        for i in contact_list:
            lat_long='GPS'
            m = folium.Map(lat_long, zoom_start=10)
            popText = folium.Html('<b>Jirisan</b></br>'+str(lat_long), script=True)
            popup = folium.Popup(popText, max_width=2650)
            folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
            m = m._repr_html_() #  updated            


        paginator = Paginator(contact_list,5)
        page_number=request.GET.get('page',1)
        data['page_obj']=paginator.get_page(page_number)   

    return render(request,"board/detail.html",context=data)