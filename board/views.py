from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("/board/list 로 가세요:)")

def boardlist(request):
    return HttpResponse("List 페이지 입니다")