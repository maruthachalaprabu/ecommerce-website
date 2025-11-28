import os
import django
import shutil
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Category, Product
from django.core.files import File

# Clear existing data
Product.objects.all().delete()
Category.objects.all().delete()

# Create categories
categories_data = [
    {'name': 'Electronics', 'slug': 'electronics'},
    {'name': 'Clothing', 'slug': 'clothing'},
    {'name': 'Books', 'slug': 'books'},
    {'name': 'Furniture', 'slug': 'furniture'},
    {'name': 'Sports', 'slug': 'sports'},
]

categories = {}
for cat_data in categories_data:
    cat = Category.objects.create(**cat_data)
    categories[cat_data['slug']] = cat
    print(f"Created category: {cat.name}")

# Define products with their categories
products_data = [
    # Electronics
    {'name': 'iPhone 13', 'slug': 'iphone-13', 'category': 'electronics', 'price': 799.99, 'description': 'Latest iPhone with A15 Bionic chip', 'image': 'iphone13.png'},
    {'name': 'iPhone 14', 'slug': 'iphone-14', 'category': 'electronics', 'price': 899.99, 'description': 'iPhone 14 with advanced camera system', 'image': 'iphone14.png'},
    {'name': 'iPhone 14 Pro', 'slug': 'iphone-14-pro', 'category': 'electronics', 'price': 999.99, 'description': 'Pro model with Dynamic Island', 'image': 'iphone14pro.png'},
    {'name': 'iPhone 15', 'slug': 'iphone-15', 'category': 'electronics', 'price': 999.99, 'description': 'iPhone 15 with USB-C', 'image': 'iphone15.png'},
    {'name': 'iPhone 16', 'slug': 'iphone-16', 'category': 'electronics', 'price': 1099.99, 'description': 'Latest iPhone 16', 'image': 'iphone16.png'},
    {'name': 'Gaming Laptop', 'slug': 'gaming-laptop', 'category': 'electronics', 'price': 1299.99, 'description': 'High-performance gaming laptop', 'image': 'laptop.png'},
    {'name': 'Business Laptop', 'slug': 'business-laptop', 'category': 'electronics', 'price': 899.99, 'description': 'Professional laptop for work', 'image': 'laptop1.png'},
    {'name': 'Smart TV 55"', 'slug': 'smart-tv-55', 'category': 'electronics', 'price': 699.99, 'description': '4K Smart TV with HDR', 'image': 'tv1.png'},
    {'name': 'Smart TV 65"', 'slug': 'smart-tv-65', 'category': 'electronics', 'price': 899.99, 'description': 'Large 4K Smart TV', 'image': 'tv2.png'},
    
    # Clothing
    {'name': 'Cotton T-Shirt', 'slug': 'cotton-tshirt', 'category': 'clothing', 'price': 19.99, 'description': 'Comfortable cotton t-shirt', 'image': 'colthes1.png'},
    {'name': 'Denim Jeans', 'slug': 'denim-jeans', 'category': 'clothing', 'price': 49.99, 'description': 'Classic denim jeans', 'image': 'colthes2.png'},
    {'name': 'Casual Shirt', 'slug': 'casual-shirt', 'category': 'clothing', 'price': 29.99, 'description': 'Stylish casual shirt', 'image': 'colthes3.png'},
    {'name': 'Hoodie', 'slug': 'hoodie', 'category': 'clothing', 'price': 39.99, 'description': 'Warm and cozy hoodie', 'image': 'colthes4.png'},
    {'name': 'Summer Dress', 'slug': 'summer-dress', 'category': 'clothing', 'price': 59.99, 'description': 'Light summer dress', 'image': 'colthes5.png'},
    
    # Books
    {'name': 'Python Programming', 'slug': 'python-programming', 'category': 'books', 'price': 34.99, 'description': 'Learn Python from scratch', 'image': 'book1.png'},
    {'name': 'Web Development', 'slug': 'web-development', 'category': 'books', 'price': 39.99, 'description': 'Complete web development guide', 'image': 'book2.png'},
    {'name': 'Data Science', 'slug': 'data-science', 'category': 'books', 'price': 44.99, 'description': 'Introduction to data science', 'image': 'book3.png'},
    {'name': 'Machine Learning', 'slug': 'machine-learning', 'category': 'books', 'price': 49.99, 'description': 'ML algorithms and applications', 'image': 'book4.png'},
    {'name': 'Django Guide', 'slug': 'django-guide', 'category': 'books', 'price': 29.99, 'description': 'Build web apps with Django', 'image': 'book5.png'},
    
    # Furniture
    {'name': 'Office Chair', 'slug': 'office-chair', 'category': 'furniture', 'price': 199.99, 'description': 'Ergonomic office chair', 'image': 'furniture1.png'},
    {'name': 'Desk Lamp', 'slug': 'desk-lamp', 'category': 'furniture', 'price': 49.99, 'description': 'LED desk lamp', 'image': 'furniture2.png'},
    {'name': 'Bookshelf', 'slug': 'bookshelf', 'category': 'furniture', 'price': 149.99, 'description': 'Wooden bookshelf', 'image': 'furniture3.png'},
    {'name': 'Coffee Table', 'slug': 'coffee-table', 'category': 'furniture', 'price': 129.99, 'description': 'Modern coffee table', 'image': 'furniture4.png'},
    {'name': 'Sofa', 'slug': 'sofa', 'category': 'furniture', 'price': 599.99, 'description': 'Comfortable 3-seater sofa', 'image': 'furniture5.png'},
    
    # Sports
    {'name': 'Running Shoes', 'slug': 'running-shoes', 'category': 'sports', 'price': 89.99, 'description': 'Professional running shoes', 'image': 'sport1.png'},
    {'name': 'Yoga Mat', 'slug': 'yoga-mat', 'category': 'sports', 'price': 29.99, 'description': 'Non-slip yoga mat', 'image': 'sport2.png'},
    {'name': 'Dumbbell Set', 'slug': 'dumbbell-set', 'category': 'sports', 'price': 79.99, 'description': 'Adjustable dumbbell set', 'image': 'sport3.png'},
    {'name': 'Tennis Racket', 'slug': 'tennis-racket', 'category': 'sports', 'price': 119.99, 'description': 'Professional tennis racket', 'image': 'sport4.png'},
    {'name': 'Basketball', 'slug': 'basketball', 'category': 'sports', 'price': 24.99, 'description': 'Official size basketball', 'image': 'sport5.png'},
]

# Create products
pictures_dir = Path('pictures')
media_products_dir = Path('media/products')

# Create media directory structure
import datetime
today = datetime.date.today()
media_target_dir = media_products_dir / str(today.year) / f"{today.month:02d}" / f"{today.day:02d}"
media_target_dir.mkdir(parents=True, exist_ok=True)

for prod_data in products_data:
    image_name = prod_data.pop('image')
    category_slug = prod_data.pop('category')
    
    # Create product
    product = Product.objects.create(
        category=categories[category_slug],
        **prod_data
    )
    
    # Copy image to media folder
    source_image = pictures_dir / image_name
    if source_image.exists():
        target_image = media_target_dir / image_name
        shutil.copy(source_image, target_image)
        
        # Update product image field
        relative_path = f"products/{today.year}/{today.month:02d}/{today.day:02d}/{image_name}"
        product.image = relative_path
        product.save()
        print(f"Created product: {product.name} with image")
    else:
        print(f"Created product: {product.name} (image not found: {image_name})")

print(f"\nTotal products created: {Product.objects.count()}")
print(f"Total categories created: {Category.objects.count()}")
