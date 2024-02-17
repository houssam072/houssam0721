from django.urls import path
from .views import ProductViews, ProductImageViews,CatProductView

app_name = 'laptop'

urlpatterns = [
    path('add_product', ProductViews.as_view(), name= 'add_Product'),
    path('get_product', ProductViews.as_view(), name= 'get_Product'),
    path('get_product/<int:pk>', ProductViews.as_view(), name= 'get_specific_Product'),
    path('get_product_cat/<int:cat>', CatProductView.as_view(), name= 'get_specific_Product'),
    path('get_product_image/<int:laptop>', ProductImageViews.as_view(), name= 'get_specific_Product'),
    path('get_product_image', ProductImageViews.as_view(), name= 'get_specific_Product'),
    path('delete_Product/<int:pk>', ProductViews.as_view(), name= 'delete_Product'),
    path('add_product_image', ProductImageViews.as_view(), name= 'add_image_Product'),
]