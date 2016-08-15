# home/urls.py

from django.conf.urls import url

from apps.home import views

urlpatterns = [
   	 url(r'^$', views.index_view, name='gym.index'),
   	 url(regex=r'^about/$', view=views.AboutView.as_view(), name='about'),
   	 url(regex=r'^contact/$', view=views.ContactView.as_view(), name='contact'),
]