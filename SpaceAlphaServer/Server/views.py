from django.shortcuts import render
from django.http import HttpResponse
from .models import users, HWID
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def get_users(request):
    try:
        if users.objects.get(login=request.GET.get('login')).password == request.GET.get('pass'):
            return HttpResponse("true")
        else:
            return HttpResponse("false")
    except ObjectDoesNotExist:
        return HttpResponse("false!!!")