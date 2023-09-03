from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from django.urls import path, include
from .views import APIResponseView


router = DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
     path('api/', APIResponseView.as_view(), name='api_response'),
]

