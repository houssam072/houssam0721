from django.urls import path
from .views import BuyNowView

app_name = 'orders'

urlpatterns = [
    path('buy-now/<int:product_id>/', BuyNowView.as_view(), name='create-order'),
]