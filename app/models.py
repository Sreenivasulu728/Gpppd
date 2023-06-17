from django.db import models

# Create your models here.
class Product_category(models.Model):
    Cid=models.IntegerField()
    CName=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.CName

class Product(models.Model):
    CName=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pid=models.IntegerField()
    PName=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self) -> str:
        return self.PName