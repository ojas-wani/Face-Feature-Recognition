from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from main.models import ToDoList, Item

def index(response, id):
    ls = ToDoList.objects.get(id = id)
    it = ls.item_set.get(id=1)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})