# step2.py

from django.urls import re_path
from django.shortcuts import redirect, render as django_render

DEBUG = True
SECRET_KEY = '1234'
ROOT_URLCONF = __name__
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates/'
        ],
    },
]


def about(request):
    title = 'Tinyapp'
    return django_render(request, 'about.html', locals())


def home(request):
    return redirect('aboutpage')


urlpatterns = [
    re_path(r'^$', home, name='homepage'),
    re_path(r'^about/$', about, name='aboutpage'),
]
