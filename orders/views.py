from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from laptop.models import Product
from accounts.models import User
from .serializers import OrderSerializers
from rest_framework import status
from laptop.serializers import ProductSerializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BuyNowView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, product_id):        
        user = request.user
        order_data = request.data

        try:
            product = Product.objects.get(id=product_id)
            user_order = User.objects.get(id = user.id)
            print('hi', user_order)
            print('hi', order_data)
            print('hi', product)
            print('hi', user_order.first_name)
        except Product.DoesNotExist:
            return Response({'error': 'Product does not found'}, status=status.HTTP_404_NOT_FOUND)
        

        total_price = product.price * order_data['product_count']
        order_data_final = {
            'user': user_order.id,
            "full_name" :f" {user_order.first_name}  {user_order.last_name}",
            "product" : order_data["product"],
            "product_count" : order_data["product_count"],
            "total_price" : total_price,
            "address" : order_data["address"],
            "mobile_phone" : user_order.mobile_number
            
        }
        serializer = OrderSerializers(data=order_data_final)
        if serializer.is_valid():
            if product.quant <= 0:
                return Response({'error': 'Product out of stock'}, status=status.HTTP_400_BAD_REQUEST)
            product.quant -= int(order_data['product_count']) 
            product.save()
            serializer.save()
            product_serializer = ProductSerializers(product)
            print('serializer',product_serializer)
            return Response({
                'order': serializer.data,
                'updated_product': product_serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    