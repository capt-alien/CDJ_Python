from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.regester),
    url(r'^loggin$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout)
    ]
