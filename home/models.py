from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'Menu'
    
class Food(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="media/food")

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'Food'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'Contact'
    
class Order(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone =  models.CharField(max_length=10)
    address = models.CharField(max_length=256)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'Order'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.order.name + " " + self.food.name + " " + str(self.quantity)
    
    class Meta:
        managed = True
        db_table = 'OrderItem'
    
class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount =  models.IntegerField()

    def __str__(self):
        return self.code
    
    class Meta:
        managed = True
        db_table = 'Coupon'