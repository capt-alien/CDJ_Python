from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_order$', views.process_order),
    url(r'^checkout$', views.checkout)
]
