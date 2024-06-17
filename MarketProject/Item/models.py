from django.contrib.auth.models import User # user authentication import
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) # for arranging alphabetical order or arranging names.
        verbose_name_plural = 'Categories' # correcting name on the database admin portal.

    def __str__(self):
        return self.name     # funtion that allow name to show on the portal
    

class Item(models.Model):
     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
     name = models.CharField(max_length=255)
     description = models.TextField(blank=True, null=True)
     price = models.FloatField()
     image = models.ImageField(upload_to='item_images', blank=True, null=True)
     is_sold = models.BooleanField(default=False)
     created_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now=True)
     
     def __str__(self):
        return self.name 