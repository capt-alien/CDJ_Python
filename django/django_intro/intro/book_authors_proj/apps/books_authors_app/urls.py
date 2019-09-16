from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_book$', views.process_book),
    url(r'^process_author$', views.process_new_author),
    url(r'^book/(?P<id>\d+)$', views.view_book),
    url(r'^authors$', views.view_authors),
    url(r'^author/(?P<id>\d+)$', views.view_author),

    ]
