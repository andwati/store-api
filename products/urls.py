# from django.urls import include, path
# from rest_framework.routers import DefaultRouter

# from .views import ProductViewSet

# router = DefaultRouter()
# router.register(r"Products", ProductViewSet)
# urlpatterns = router.urls

from django.urls import path

from .views import ProductDetailView, ProductList

urlpatterns = [
    path("", ProductList.as_view(), name="products"),
    path("<int:id>", ProductDetailView.as_view(), name="product-detail"),
]
