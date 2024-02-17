from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializers, ProductImage
from .models import Product, PictureProduct

# Create your views here.

class ProductViews(APIView):
    def post(self, request):
        data = request.data
        serializer = ProductSerializers(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk = None):
        if pk is not None:
            try:
                product = Product.objects.get(pk = pk)
            except Product.DoesNotExist:
                return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)   
            serializer = ProductSerializers(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            product_list = Product.objects.all()
            serializer = ProductSerializers(product_list, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)   
        product.delete()
        return Response({'message': 'Laptop deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



class ProductImageViews(APIView):
    def post(self, request):
        data = request.data
        serializer = ProductImage(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, laptop = None):
            if laptop is not None:
                try:
                    image = PictureProduct.objects.get(laptop = laptop)
                except PictureProduct.DoesNotExist:
                    return Response({'error' : 'product image not found'}, status=status.HTTP_404_NOT_FOUND)
                serializers = ProductImage(image)
                return Response(serializers.data, status=status.HTTP_200_OK)
            else:
                image_list = PictureProduct.objects.all()
                serializers = ProductImage(image_list, many = True)
                return Response(serializers.data, status=status.HTTP_200_OK)


class CatProductView(APIView):
    def get(self, request, cat):
            try:
                product = Product.objects.filter(cat = cat)
            except Product.DoesNotExist:
                return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)   
            serializer = ProductSerializers(product, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
