# tinyapp.py

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


# wrapper renders django template
def render(template_name):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            context = func(request, *args, **kwargs)
            return django_render(request, template_name, context)
        return wrapper
    return decorator


@render(template_name='about.html')
def about(request):
    title = 'Tinyapp'
    author = 'John Mitchell'
    return locals()


def home(request):
    return redirect('aboutpage')


urlpatterns = [
    re_path(r'^$', home, name='homepage'),
    re_path(r'^about/$', about, name='aboutpage'),
]
