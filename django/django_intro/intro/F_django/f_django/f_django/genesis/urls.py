from django.conf.urls import url
from . import views

#TOP LEVEL VIEWS
urlpatterns = [
    url(r'^$', views.index),
]
