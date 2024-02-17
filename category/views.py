from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CatSerializers
from .models import Category

# Create your views here.

class CategoryViews(APIView):
    def post(self, request):
        data = request.data

        # cat_data = {
        #     'cat_name' : data['cat_name'],
        #     'cat_image' : data['cat_image']

        # }
        serializer = CatSerializers(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, pk = None):
        if pk is not None : 
            try:
                category = Category.objects.get(pk = pk)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)   
            serializer = CatSerializers(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            cat_list = Category.objects.all()
            serializer = CatSerializers(cat_list, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk = pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)   
        category.delete()
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)