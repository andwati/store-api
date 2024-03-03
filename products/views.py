from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Brand, Product, Supplier
from .serializers import BrandSerializer, ProductSerializer, SupplierSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        data = list(Brand.objects.all().values())
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        data = list(Brand.objects.filter(id=kwargs["pk"]).values())
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        brand_serializer_data = BrandSerializer(data=request.data)
        if brand_serializer_data.is_valid():
            brand_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Brand added successfully"}, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the details"}, status=status_code)

    def destroy(self, request, *args, **kwargs):
        brand_data = Brand.objects.filter(id=kwargs["pk"])
        if brand_data:
            brand_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Brand deleted succesfully"}, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Brand not found"}, status=status_code)

    def update(self, request, *args, **kwargs):
        brand_details = Brand.objects.get(id=kwargs["pk"])
        brand_serializer_data = BrandSerializer(brand_details, data=request, partial=True)
        if brand_serializer_data.is_valid():
            brand_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Brand updated successfully"}, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Brand not found"}, status=status)
