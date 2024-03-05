# from rest_framework import status, viewsets
# from rest_framework.response import Response

# from .models import Product
# from .serializers import ProductSerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def list(self, request, *args, **kwargs):
#         data = list(Product.objects.all().values())
#         return Response(data, status=status.HTTP_200_OK)

#     def retrieve(self, request, *args, **kwargs):
#         data = list(Product.objects.filter(id=kwargs["pk"]).values())
#         return Response(data, status=status.HTTP_200_OK)

#     def create(self, request, *args, **kwargs):
#         product_serializer_data = ProductSerializer(data=request.data)
#         if product_serializer_data.is_valid():
#             product_serializer_data.save()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "Product added successfully"}, status=status_code)
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "please fill the details"}, status=status_code)

#     def destroy(self, request, *args, **kwargs):
#         product_data = Product.objects.filter(id=kwargs["pk"])
#         if product_data:
#             product_data.delete()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "Product deleted successfully"}, status=status_code)
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "Product not found"}, status=status_code)

#     def update(self, request, *args, **kwargs):
#         product_details = Product.objects.get(id=kwargs["pk"])
#         product_serializer_data = ProductSerializer(product_details, data=request, partial=True)
#         if product_serializer_data.is_valid():
#             product_serializer_data.save()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "Product updated successfully"}, status=status_code)
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "Product not found"}, status=status_code)

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer


class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)
