from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet


router = DefaultRouter()

router.register('', UserViewSet, basename='users')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]
