from django.conf.urls import url
from basic import views

app_name = 'basic'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]


a=1