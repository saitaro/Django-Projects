from django.conf.urls import url
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    url(r'^$', views.help, name='help'),
    url(r'^doom(?P<ok>\d{3})/', views.newpage, name='doom')
]