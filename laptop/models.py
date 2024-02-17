from django.db import models
from djmoney.models.fields import MoneyField
from category.models import Category

# Create your models here.


def image_upload(instance, filename):
    image_name, extension = filename.split('.')
    return '%s/%s/%s.%s'%('images',instance.__class__.__name__,image_name, extension)


class Product(models.Model):
    brand = models.CharField(max_length = 120, default = 'unKnown')
    status = models.CharField(max_length = 255, default = 'unKnowm')
    cat = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 120, default = 'unKnown')
    model = models.CharField(max_length = 120, default = 'unKnown')
    color = models.CharField(max_length = 120, default = 'unKnown')
    processor = models.CharField(max_length = 120, default = 'unKnown')
    gpu = models.CharField(max_length = 120, default = 'unKnown')
    screen = models.CharField(max_length = 120, default = 'unKnown')
    ram = models.CharField(max_length = 120, default = 'unKnown')
    hard = models.CharField(max_length = 120, default = 'unKnown')
    os = models.CharField(max_length = 120, default = 'unKnown')
    guranti = models.CharField(max_length = 120, default = 'unKnown')
    quant = models.PositiveIntegerField()
    price = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    picture = models.ImageField(upload_to=image_upload)
    desc = models.CharField(max_length = 120, default = 'unKnown')    

    def __str__(self): 
        return self.name
    


class PictureProduct(models.Model):
    laptop = models.ForeignKey(Product, on_delete = models.CASCADE)
    picture_one = models.ImageField(upload_to=image_upload)
    picture_tow = models.ImageField(upload_to=image_upload)
    picture_three = models.ImageField(upload_to=image_upload)
    picture_four = models.ImageField(upload_to=image_upload)
    picture_five = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.picture_one.url