import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page
from random import randint

def populate():
    python_pages = [
        {"title": "Official Python Tutorial", "url": "http://docs.python.org/3/tutorial"},
        {"title": "How to think like a computer scientist", "url": "http://www.greenteapress.com/thinkpython"},
        {"title": "Learn python in 10 minutes", "url": "http://www.korokithakis.net/tutorials/python"}
    ]

    django_pages = [
        {"title": "Official django tutorial", "url": "https//docs.djangoproject.com/en/1.9/intro/tutorial01"},
        {"title": "Django Rocks", "url": "http://www.djangorocks.com"},
        {"title": "How to tango with django", "url": "http://www.tangowithdjango.com"}
    ]

    other_pages = [
        {"title": "Bottle", "url": "http://bottepy.org/docs/dev"},
        {"title": "Flashk", "url": "http://flask.pocoo.org"},
    ]

    cats = {
        "Python": {"pages": python_pages},
        "Django": {"pages": django_pages},
        "Other Frameworks": {"pages": other_pages}
    }
    cat_views = {
        "Python": 128,
        "Django": 64,
        "Other Frameworks": 32
    }

    cat_likes = {
        "Python": 64,
        "Django": 32,
        "Other Frameworks": 16
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_views[cat], cat_likes[cat])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1} - Views: {2} Likes: {3}".format(str(c), str(p), str(c.views), str(c.likes)))

def add_page(cat, title, url):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = randint(0, 100)
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()