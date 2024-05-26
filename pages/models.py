from django.db import models
from django.contrib.auth.models import User
import os
import datetime
# Create your models here.


def getfilename(request,filename):
    new_Date = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_filename = '%s%s'%(new_Date,filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):
    name=models.CharField(max_length=50, null=False, blank=False)
    image=models.ImageField(upload_to=getfilename,null=True, blank=True)
    status= models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=False, blank=False)
    image=models.ImageField(upload_to=getfilename,null=True, blank=True)
    status= models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    old_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True, blank=True)
    product_image_one=models.ImageField(upload_to=getfilename,null=True, blank=True)
    product_image_two=models.ImageField(upload_to=getfilename,null=True, blank=True)
    product_image_three=models.ImageField(upload_to=getfilename,null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    highlight = models.TextField(max_length=500, null=False, blank=False)
    status= models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-Trending")
    # limited_time_deal = models.BooleanField(default=False, help_text="0-default, 1-LimitedTimeDeal")
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class Cart_Items(models.Model):
    user= models.ForeignKey(User,on_delete = models.CASCADE)
    product= models.ForeignKey(Product,on_delete = models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    product_size = models.TextField(max_length=5, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add= True)

    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price

class fav_items(models.Model):
    user= models.ForeignKey(User,on_delete = models.CASCADE)
    product= models.ForeignKey(Product,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
