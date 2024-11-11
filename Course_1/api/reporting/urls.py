from reporting.views import OrderViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('orders',OrderViewSet, basename='orders')


urlpatterns = [
    path('', include(router.urls))              
]