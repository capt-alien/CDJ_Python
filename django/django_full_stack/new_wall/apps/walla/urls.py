from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.regester),
    url(r'^loggin$', views.login),
    url(r'^wall$', views.wall),
    url(r'^logout$', views.logout),
    url(r'^add_message$', views.add_message),
    url(r'^wall/add_comment$', views.add_comment),
    url(r'^message/delete/(?P<id>\d+)$', views.delete_message)

    ]
