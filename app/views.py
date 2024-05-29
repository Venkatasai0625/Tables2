from django.shortcuts import render
from app.models import *

from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    topic_name=input("Enter topic_name:")
    TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
    TO.save()
    QLTO= Topic.objects.all()
    d={"QLTO":QLTO}
    return render(request,'display_topic.html',d)


def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)


def insert_webpage(request):
    topic_name=input("Enter Topic name:")
    name=input("Enter name: ")
    url=input("Enter urlname: ")
    wpages=input("Enter wpage: ")
    LTO=Topic.objects.filter(topic_name=topic_name)
    print(LTO)
    if LTO:
        TO=LTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,wpages=wpages)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d={"QLWO":QLWO}
        return render(request,'display_webpage.html',d)
    else:
        return HttpResponse ('Given topic is not present in table topic')
        
    
def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={"QLWO":QLWO}
    return render(request,'display_webpage.html',d)