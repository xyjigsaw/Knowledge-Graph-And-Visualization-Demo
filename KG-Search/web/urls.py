from django.conf.urls import url
from . import entity

urlpatterns = [
    url(r'^$', entity.search_entity, name='index'),
]
