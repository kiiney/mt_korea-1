from django.shortcuts import render
from django.http import HttpResponse
import folium
# Create your views here.

def index(request):
    #return HttpResponse("/board/list 로 가세요:)")
    
    return render(request, 'board/firstpage.html')   

def boardlist(request):   

    lat_long = [35.3369, 127.7306]
    m = folium.Map(lat_long, zoom_start=10)
    popText = folium.Html('<b>Jirisan</b></br>'+str(lat_long), script=True)
    popup = folium.Popup(popText, max_width=2650)
    folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
    m = m._repr_html_() #  updated
    datas = {'mountain_map': m}
    return render(request, 'board/showmapwithfolium.html')    