from django.db import models

# Create your models here.
class ItemList(models.Model):
 Category_Name = models.CharField(max_length=20)

class about(models.Model):
   pass

class Book(models.Model):
   pass

class Items(models.Model):
   Item_name = models.CharField(max_length=15)
   description = models.TextField(blank=False)
   price = models.IntegerField()
   Category = models.ForeignKey(ItemList,related_name="Category_name", on_delete=models.CASCADE)
   Images = models.ImageField(upload_to="")


