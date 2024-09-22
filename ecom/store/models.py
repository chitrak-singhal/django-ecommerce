from django.db import models
import datetime

class User(models.Model):
    email_id = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    mobile = models.BigIntegerField(null=False, unique=True)
    isplusmember = models.BooleanField(default=False)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Product(models.Model):
    product_name = models.CharField(max_length=255, null=False)
    product_price = models.BigIntegerField(null=False)
    discount = models.BigIntegerField(default=0)
    product_description = models.TextField(default="No description available")
    img_id = models.BigIntegerField(null=False)

class Seller(models.Model):
    seller_name = models.CharField(max_length=255, null=False)
    account_id = models.BigIntegerField(null=False, unique=True)

class ProductsSellers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class Order(models.Model):
    order_total = models.BigIntegerField(null=False)

class UserOrders(models.Model):  # Renamed for consistency
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class OrdersProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=1)

class Address(models.Model):
    house_no = models.BigIntegerField(null=False)
    street_name = models.CharField(max_length=255, default="Unknown")
    address_lines = models.TextField(null=False)
    city = models.CharField(max_length=255, null=False)
    region = models.CharField(max_length=255, null=False)
    pincode = models.BigIntegerField(null=False)

class UserAddresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=1)
