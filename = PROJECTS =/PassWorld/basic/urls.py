from django.conf.urls import url
from basic import views

app_name = 'basic'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url('^logout/$', views.user_logout, name='logout'),
    url('special/', views.special, name='special'),
    # url(r'^login/$', views.login, name='login'),
]