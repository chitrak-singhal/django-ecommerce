from django.contrib import admin
from .models import User, Cart, Category, Product, Seller, ProductsSellers, Order, UserOrders, OrdersProducts, Address, UserAddresses, CartProducts

# Register your models here
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(ProductsSellers)
admin.site.register(Order)
admin.site.register(UserOrders)
admin.site.register(OrdersProducts)
admin.site.register(Address)
admin.site.register(UserAddresses)
admin.site.register(CartProducts)
