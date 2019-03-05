# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from test_test.models import Event,Guest
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def index(request):
    return render(request,"index.html")
def login_action(request):
    if request.method =='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,'index.html',{'error':'username or password error!'})
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user','')

    return render(request,"event_manage.html",{"user":username,"event":event_list})
def search_name(request):
    username = request.session.get('user','')
    search_name =request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user":username,"guests":contacts})

def logout(request):
    #auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response
