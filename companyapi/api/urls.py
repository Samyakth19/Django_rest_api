from  django.contrib import admin
from django.urls import path
from api.views import CompanyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)
urlpattrens = [
    path('',include(router.urls))

]