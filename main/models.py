from django.db import models

# Create your models here.
#username: superuser
#password : superuser
class Category(models.Model):
 Name = models.CharField(max_length=20)

 def __str__(self):
    return self.Name
   

class about(models.Model):
   description = models.TextField(blank = True)

class Book(models.Model):
   name = models.CharField(max_length=15)
   Phone_number = models.IntegerField()
   Email = models.EmailField()
   Booking_Date = models.DateField()

class Items(models.Model):
   Item_name = models.CharField(max_length=15)
   description = models.TextField(blank=False)
   price = models.IntegerField()
   category = models.ForeignKey(Category,related_name="Category_name", on_delete=models.CASCADE)
   image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

   def __str__(self):
      return self.Item_name



