# step1.py

from django.urls import re_path
from django.http import HttpResponse

DEBUG = True
SECRET_KEY = '1234'
ROOT_URLCONF = __name__


def home(request):
    return HttpResponse("WE LOVE BEER")


urlpatterns = [
    re_path(r'^$', home, name='homepage'),
]
