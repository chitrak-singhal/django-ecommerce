from django.db import models
import datetime

class User(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email_id = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    mobile = models.BigIntegerField(null=False, unique=True)
    isplusmember = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=255, null=False)
    product_price = models.DecimalField(null=False, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    discount = models.BigIntegerField(default=0)
    product_description = models.TextField(default="No description available")
    img = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name

class Seller(models.Model):
    seller_name = models.CharField(max_length=255, null=False)
    account_id = models.BigIntegerField(null=False, unique=True)

class ProductsSellers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class Order(models.Model):
    order_total = models.DecimalField(null=False, decimal_places=2, max_digits=8)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

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
