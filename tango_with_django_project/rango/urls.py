from django.conf.urls import url
from rango import views

app_name = 'rango'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^like/$', views.like_category, name="like_category"),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    # url(r'^register/$', views.register, name="register"),
    # url(r'^login/$', views.user_login, name="login"),
    # url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^restricted/$', views.restricted, name="restricted"),
    url(r'^suggest/$', views.suggest_category, name="suggest_category"),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name="profile"),
    url(r'^profiles/$', views.list_profiles, name="list_profiles"),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
]