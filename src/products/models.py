import os
import string 
import random 
from django.urls import reverse
from django.db import models

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = ''.join(random.choices(string.digits, k = 10))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename,
    )


    
class Product(models.Model):
    title           = models.CharField(max_length=120)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    slug            = models.SlugField(blank=True,null=True, unique=True)
    description     = models.TextField(blank=True,null=True)
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    in_stock        = models.IntegerField(default=1, primary_key=False)
    # in Stock default is 1 field type same as quantity

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        # return reverse('productDetail',args=str(self.id))
        return reverse('products:productDetail',kwargs={'slug': self.slug})