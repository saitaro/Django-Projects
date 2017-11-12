from django.conf.urls import url
from . import views

app_name = 'tasklist'

urlpatterns = (
    url(r'^$', views.GroceryList.as_view(), name='mainlist'),
    url(r'^create/$', views.GroceryCreate.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', views.GroceryDelete.as_view(), name='delete'),
    url(r'^detail/(?P<pk>\d+)/$', views.GroceryDetail.as_view(), name='detail'),
)

