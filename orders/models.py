from django.db import models
from accounts.models import User
from laptop.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField



# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default = 1)
    order_date = models.DateTimeField(auto_now_add = True)
    total_price =MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    address = models.CharField(max_length = 255, null = False)
    mobile_phone = models.IntegerField(default='+971')

    
    def __str__(self):
        return f"Order #{self.id} by {self.user.email} on {self.order_date}"
