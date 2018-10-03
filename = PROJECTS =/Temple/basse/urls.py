from django.conf.urls import url
from basse import views

app_name = 'basse'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
