from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import pre_save
# Create your models here.









class Customer(models.Model):
    user= models.OneToOneField(User, null=True , on_delete=models.CASCADE , blank=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='profile'  , default='profile/default.png')

    def __str__(self):
        return str(self.user)

class Tag(models.Model):
    name= models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    Cat = (('indoor','indoor'),('outdoor','outdoor'))
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True , choices=Cat)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    class Meta:
            verbose_name = "Product"
            verbose_name_plural = "Products"

    def __str__(self):
            return self.name

# tag

class Order(models.Model):
    STATUS = (('pending' , 'pending') , ('out for delvired' ,'out for delvired'  ) , ('delvired' ,'delvired'  ))
    product = models.ForeignKey(Product , null=True , on_delete=models.CASCADE)
    cutomer = models.ForeignKey(Customer , null=True , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True , choices=STATUS)
    note = models.CharField(max_length=200, null=True)
    class Meta:
            verbose_name = "Order"
            verbose_name_plural = "Orders"



    def __str__(self):
            return str(self.product)
