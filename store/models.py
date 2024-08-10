from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    porfile_pic = models.ImageField(upload_to="users", blank= True)
    phone = models.CharField(max_length=14,default=0,blank=True,null=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
            Customer.objects.create(user=instance)
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null = False)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='product')
    description = models.TextField()
    image = models.ImageField(upload_to="products")
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1)
    address =models.CharField(max_length=250, blank=True, default='')
    phone = models.CharField(max_length=15, default='', blank= True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.products.name
    

    

    