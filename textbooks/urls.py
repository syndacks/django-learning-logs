from django.conf.urls import url
from . import views

app_name = 'textbooks'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about', views.about, name='about'),

    # ex: /polls/5/
    url(r'^(?P<isbn>[0-9]+)/$', views.textbook_detail, name='textbook_detail'),

    url(r'^(?P<isbn>[0-9]+)/new/$', views.new_exercise, name='new_exercise')
]
