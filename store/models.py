from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Custom User model extending Django's AbstractUser
# This allows us to add custom fields to the user model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


# Category model for organizing products
class Category(models.Model):
    name = models.CharField(max_length=100)  # Category name
    slug = models.SlugField(unique=True)     # URL-friendly version of name

    class Meta:
        verbose_name_plural = 'categories'   # Proper plural form in admin

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Returns URL for category detail view
        return reverse('store:category', args=[self.slug])


# Product model for store items
class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Images stored in media/products/
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Returns URL for product detail view
        return reverse('store:product_detail', args=[self.slug])


# Shopping Cart model
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.user.username}"

    def get_total_price(self):
        # Calculates total price of all items in cart
        return sum(item.get_cost() for item in self.items.all())


# Individual items in the shopping cart
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_cost(self):
        # Calculates total cost for this item
        return self.product.price * self.quantity


# Order model for completed purchases
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        # Calculates total cost of the order
        return sum(item.get_cost() for item in self.items.all())


# Individual items in an order
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_cost(self):
        # Calculates total cost for this order item
        return self.price * self.quantity
