from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product
from decimal import Decimal
import os
from django.conf import settings
from django.core.files import File
from PIL import Image, ImageDraw, ImageFont
import random


class Command(BaseCommand):
    help = 'Creates sample data for the store'

    def create_product_image(self, product_name, category_name):
        # Create a new image with a white background
        width = 800
        height = 600
        background_color = (240, 240, 240)
        img = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(img)

        # Draw a rectangle
        rect_color = (200, 200, 200)
        draw.rectangle([(50, 50), (width-50, height-50)],
                       outline=rect_color, width=2)

        # Add category name at the top
        category_color = (100, 100, 100)
        category_position = (width//2, 100)
        draw.text(category_position, category_name,
                  fill=category_color, anchor="mm")

        # Add product name in the center
        product_color = (50, 50, 50)
        product_position = (width//2, height//2)
        draw.text(product_position, product_name,
                  fill=product_color, anchor="mm")

        # Add a decorative element based on category
        if category_name == 'Electronics':
            # Draw a circuit-like pattern
            for _ in range(5):
                x1 = random.randint(100, width-100)
                y1 = random.randint(100, height-100)
                x2 = random.randint(100, width-100)
                y2 = random.randint(100, height-100)
                draw.line([(x1, y1), (x2, y2)], fill=(180, 180, 180), width=2)
        elif category_name == 'Clothing':
            # Draw a clothing icon
            draw.rectangle([(width//2-50, height//2-100), (width//2+50, height//2+100)],
                           outline=(180, 180, 180), width=2)
        elif category_name == 'Books':
            # Draw a book icon
            draw.rectangle([(width//2-40, height//2-60), (width//2+40, height//2+60)],
                           outline=(180, 180, 180), width=2)
            draw.line([(width//2, height//2-60), (width//2, height//2+60)],
                      fill=(180, 180, 180), width=2)
        elif category_name == 'Home & Garden':
            # Draw a house icon
            draw.polygon([(width//2, height//2-50), (width//2-50, height//2+50),
                         (width//2+50, height//2+50)], outline=(180, 180, 180), width=2)
        elif category_name == 'Sports & Outdoors':
            # Draw a ball
            draw.ellipse([(width//2-40, height//2-40), (width//2+40, height//2+40)],
                         outline=(180, 180, 180), width=2)
        elif category_name == 'Toys & Games':
            # Draw a game piece
            draw.rectangle([(width//2-30, height//2-30), (width//2+30, height//2+30)],
                           outline=(180, 180, 180), width=2)

        # Save the image
        img_path = os.path.join(
            settings.MEDIA_ROOT, 'products', f'{product_name.lower().replace(" ", "_")}.jpg')
        img.save(img_path, 'JPEG', quality=95)
        return img_path

    def handle(self, *args, **kwargs):
        # Create categories
        categories = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Home & Garden', 'slug': 'home-garden'},
            {'name': 'Sports & Outdoors', 'slug': 'sports-outdoors'},
            {'name': 'Toys & Games', 'slug': 'toys-games'},
        ]

        for category_data in categories:
            Category.objects.get_or_create(
                name=category_data['name'],
                slug=category_data['slug']
            )

        # Create products
        products = [
            {
                'name': 'Smartphone X',
                'slug': 'smartphone-x',
                'category': 'electronics',
                'description': 'Latest smartphone with amazing features. 6.5" OLED display, 5G capable, 128GB storage.',
                'price': Decimal('699.99'),
                'stock': 50,
            },
            {
                'name': 'Laptop Pro',
                'slug': 'laptop-pro',
                'category': 'electronics',
                'description': 'Powerful laptop for professionals. Intel i7, 16GB RAM, 512GB SSD, NVIDIA Graphics.',
                'price': Decimal('1299.99'),
                'stock': 30,
            },
            {
                'name': 'Cotton T-Shirt',
                'slug': 'cotton-tshirt',
                'category': 'clothing',
                'description': 'Comfortable 100% cotton t-shirt. Available in multiple colors and sizes.',
                'price': Decimal('19.99'),
                'stock': 100,
            },
            {
                'name': 'Python Programming Guide',
                'slug': 'python-programming-guide',
                'category': 'books',
                'description': 'Comprehensive guide to Python programming. Perfect for beginners and intermediate developers.',
                'price': Decimal('39.99'),
                'stock': 75,
            },
            {
                'name': 'Garden Tools Set',
                'slug': 'garden-tools-set',
                'category': 'home-garden',
                'description': 'Complete set of garden tools including shovel, rake, pruning shears, and gloves.',
                'price': Decimal('49.99'),
                'stock': 40,
            },
            {
                'name': 'Basketball',
                'slug': 'basketball',
                'category': 'sports-outdoors',
                'description': 'Professional grade basketball. Official size and weight.',
                'price': Decimal('29.99'),
                'stock': 60,
            },
            {
                'name': 'Board Game Collection',
                'slug': 'board-game-collection',
                'category': 'toys-games',
                'description': 'Collection of classic board games including chess, checkers, and backgammon.',
                'price': Decimal('34.99'),
                'stock': 45,
            },
            {
                'name': 'Smart Watch',
                'slug': 'smart-watch',
                'category': 'electronics',
                'description': 'Feature-rich smartwatch with health tracking, notifications, and GPS.',
                'price': Decimal('199.99'),
                'stock': 55,
            },
            {
                'name': 'Denim Jeans',
                'slug': 'denim-jeans',
                'category': 'clothing',
                'description': 'Classic fit denim jeans. Durable and comfortable for everyday wear.',
                'price': Decimal('59.99'),
                'stock': 80,
            },
            {
                'name': 'Cooking Book Set',
                'slug': 'cooking-book-set',
                'category': 'books',
                'description': 'Collection of international cuisine cookbooks with easy-to-follow recipes.',
                'price': Decimal('45.99'),
                'stock': 35,
            },
        ]

        # Ensure media directory exists
        os.makedirs(os.path.join(settings.MEDIA_ROOT,
                    'products'), exist_ok=True)

        for product_data in products:
            category = Category.objects.get(slug=product_data['category'])

            # Create product image
            image_path = self.create_product_image(
                product_data['name'], category.name)

            # Create or update product
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                slug=product_data['slug'],
                defaults={
                    'category': category,
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'available': True,
                }
            )

            # Add image to product
            if not product.image:
                with open(image_path, 'rb') as f:
                    product.image.save(
                        f'product_{product.id}.jpg', File(f), save=True)

        self.stdout.write(self.style.SUCCESS(
            'Successfully created sample data with product images'))
