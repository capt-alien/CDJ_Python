from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/add_message$', views.add_message),
    url(r'^/add_comment$', views.add_comment)
]
