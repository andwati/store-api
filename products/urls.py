from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BrandViewSet

router = DefaultRouter()
router.register(r"Brands", BrandViewSet)
urlpatterns = router.urls
