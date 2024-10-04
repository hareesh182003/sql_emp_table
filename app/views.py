from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    top_name = input("enter the topic_name: ")
    Tobj = Topic.objects.get_or_create(topic_name = top_name)
    if Tobj[1]:
        return HttpResponse("The Row is Inserted in table")
    else:
        return HttpResponse("The data already exits")
'''
def insert_webpage(request):
    top_name = input("Enter the topic_name: ")
    name_r = input("Enter your Name: ")
    url_r = input("Enter the urls: ")

    Tobj = Topic.objects.get_or_create(topic_name = top_name)
    wobj = Webpage.objects.get_or_create(topic_name = Tobj[0],name=name_r,url=url_r)
    return HttpResponse("ur webpage object is created successfully")

def insert_webpage(request):
    top_name = input("Enter the topic_name: ")
    name_r = input("Enter your Name: ")
    url_r = input("Enter the urls: ")

    Tobj = Topic.objects.get(topic_name = top_name)
    wobj = Webpage.objects.get_or_create(topic_name=Tobj,name=name_r,url=url_r)
    return HttpResponse('Webpage Object Created')
'''
def insert_webpage(request):
    top_name = input("Enter the topic_name: ")
    name_r = input("Enter your Name: ")
    url_r = input("Enter the urls: ")

    Tobj = Topic.objects.filter(topic_name = top_name)
    # return HttpResponse(Tobj)
    if Tobj:
        obj = Tobj[0]
        Wobj = Webpage.objects.get_or_create(topic_name = obj,name = name_r,url = url_r)
        return HttpResponse('webpage is created successfully')
    else:
        return HttpResponse('The webpage object is not created check the database correctly')

def insert_access(request):
    id_r = input("Enter the parent id: ")
    # name_r = input("Enter the name: ")
    author_r = input("Enter the Author name: ")
    date_r = input("Enter the date: ")

    Wobj = Webpage.objects.filter(id = id_r)
    if Wobj:
        obj = Wobj[0]
        Arobj = AccessRecord.objects.get_or_create(name = obj,author = author_r,date = date_r)
        # return HttpResponse("Record enterd into accessrecord")
        d = {'access':AccessRecord.objects.all()}
        return render(request,'access_display.html',d)
    else:
        return HttpResponse("The mentioned id is not present in the webpage table")

def display_topic(request):
    d = {'topic_objects':Topic.objects.all()}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    d = {'webpage_objects':Webpage.objects.all()}
    return render(request,'display_webpage.html',d)
def access_display(request):
    d = {'access':AccessRecord.objects.all()}
    return render(request,'access_display.html',d)
