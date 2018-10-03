from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from CRM.views import (UserViewSet, CompanyViewSet,
                       MasterViewSet, SkillViewSet, OrderViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'masters', MasterViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]


