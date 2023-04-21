So the other day I wanted to make a small web app. Django is a great framework for this, as it automatically includes a ton of stuff I know I'll need. A database, templates, routing, all the "batteries included" features I like. 

I found a [blog post](https://realpython.com/django-todo-lists/) that shows how to do a "to do app" in full Django style. I copied the code, and at the end my app worked! Unfortunately, it was a bit confusing at 640 lines of code and several identical directories. I was hoping to do better.

A "Todo" app had too many moving parts, so I chose to do a minimal app next time.I found another [blog post, by Vitor Freitas](https://simpleisbetterthancomplex.com/article/2017/08/07/a-minimal-django-application.html).  This one was much better: only 56 lines of code! Despite not being as featureful, this minimal app has most of the features I want: templates, URL routing, and convenience features. At 10% of the complexity, I'm happy with this.

Let me show you how to do it.

## Benefits of a Minimal Application

I'm a fan of feedback loops -- I'm writing a book on the subject. In building my app, I want to have a tiny core of code that I know very well. Over time, I'll add a small feature, then integrate and publish the updated app. A fast quality feedback loop, where I trust everything, is really useful.

The standard Todo App was okay, but had 10x the amount of code, and *22* files in *six* different directories. The most common issue I had was figuring out where to put files. If a template is in the wrong place, loading a page will make the app explode with a really ugly error. Not fun, and not conducive to a tight, fast feedback loop.

The Minimal App only has *two* directories. It's incredibly easy to just add code and it works, vs having to manage fiddly details that don't contribute to my app.

## Minimal Django App

The standard `django-admin startproject` command generates a basic Django project directory structure with a number of files... but they're mostly extra boilerplate. We'll dispense with all of that.

Let's write a minimal Django app from scratch.

### Setup virtualenv

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Write One-File Django Project

Copy this code into "tinyapp.py":

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

### Run App

Run the Django appserver:

    django-admin runserver --pythonpath=. --settings=step1

### Verify App

Load the web page in a browser http://localhost:8000/

XX screenshot

You're done! A fully working minimal Django app in *ten* lines of code. The traditional settings.py file from the standard boilerplate is easily quadruple that.

Let's add a few features:

XX template
XX template use locals

## Thanks

XX Vitor
XX Real Python person

## Future Directions

XX Todo quite useful

