from django.urls import path

from .views import ProductDetailView, ProductList

urlpatterns = [
    path("", ProductList.as_view(), name="products"),
    path("<int:id>", ProductDetailView.as_view(), name="product-detail"),
]
