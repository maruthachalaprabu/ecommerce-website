import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Product

# Updated descriptions for products
descriptions = {
    'iphone-13': 'Experience the power of A15 Bionic chip with advanced dual-camera system. Features 6.1-inch Super Retina XDR display, Ceramic Shield, and all-day battery life. Available in stunning colors with 5G capability for superfast downloads and high-quality streaming.',
    
    'iphone-14': 'The iPhone 14 brings you groundbreaking safety features including Crash Detection and Emergency SOS via satellite. Powered by A15 Bionic chip with 5-core GPU, featuring an advanced camera system for stunning photos in any light. Enjoy all-day battery life and beautiful design.',
    
    'iphone-14-pro': 'Meet Dynamic Island - a magical new way to interact with iPhone. The 48MP Main camera is our biggest leap ever, with ProRAW and ProRes video. Always-On display keeps your Lock Screen glanceable. Powered by A16 Bionic, the fastest chip in a smartphone.',
    
    'iphone-15': 'All-new design featuring durable color-infused glass and aluminum. Dynamic Island bubbles up alerts and Live Activities. 48MP Main camera with 2x Telephoto. USB-C connectivity. A16 Bionic powers advanced features like computational photography and smooth gaming.',
    
    'iphone-16': 'The latest iPhone with cutting-edge technology. Features advanced camera system, lightning-fast A17 chip, and innovative design. Experience next-level performance, incredible battery life, and stunning display quality. Perfect for photography, gaming, and productivity.',
    
    'gaming-laptop': 'Dominate the competition with this high-performance gaming laptop. Features latest-gen processor, dedicated graphics card, high refresh rate display, and advanced cooling system. RGB backlit keyboard, ample storage, and premium build quality for serious gamers.',
    
    'business-laptop': 'Professional-grade laptop designed for productivity. Lightweight and portable with long battery life. Features powerful processor, ample RAM, fast SSD storage, and crisp display. Perfect for business professionals, students, and remote workers.',
    
    'smart-tv-55': 'Immerse yourself in stunning 4K Ultra HD picture quality with HDR support. Smart TV features built-in streaming apps, voice control, and seamless connectivity. 55-inch display perfect for living rooms. Enjoy vibrant colors and deep blacks with advanced display technology.',
    
    'smart-tv-65': 'Experience cinema-quality entertainment at home with this 65-inch 4K Smart TV. Features HDR10+, Dolby Vision, and advanced upscaling technology. Built-in streaming apps, voice assistant, and multiple HDMI ports. Perfect for movie enthusiasts and sports fans.',
    
    'cotton-tshirt': 'Premium 100% cotton t-shirt offering superior comfort and breathability. Classic fit with reinforced stitching for durability. Soft fabric that gets better with every wash. Available in multiple colors. Perfect for casual wear, layering, or everyday comfort.',
    
    'denim-jeans': 'Classic denim jeans crafted from premium quality fabric. Features comfortable fit, durable construction, and timeless style. Five-pocket design with reinforced stitching. Perfect for casual outings or dressed-up occasions. Available in various sizes and washes.',
    
    'casual-shirt': 'Stylish casual shirt perfect for any occasion. Made from breathable fabric with modern fit. Features quality buttons, neat stitching, and versatile design. Easy to pair with jeans or chinos. Ideal for work, weekend outings, or casual events.',
    
    'hoodie': 'Cozy and comfortable hoodie made from soft fleece material. Features adjustable drawstring hood, kangaroo pocket, and ribbed cuffs. Perfect for layering or wearing alone. Ideal for cool weather, lounging, or casual outings. Machine washable and durable.',
    
    'summer-dress': 'Light and breezy summer dress perfect for warm weather. Features flattering silhouette, comfortable fabric, and beautiful design. Easy to wear and maintain. Ideal for beach trips, garden parties, or casual summer outings. Available in vibrant colors.',
    
    'python-programming': 'Comprehensive guide to Python programming from basics to advanced concepts. Covers data structures, algorithms, object-oriented programming, and real-world applications. Includes hands-on exercises and projects. Perfect for beginners and intermediate programmers.',
    
    'web-development': 'Complete web development guide covering HTML, CSS, JavaScript, and modern frameworks. Learn responsive design, backend development, databases, and deployment. Includes practical projects and industry best practices. Ideal for aspiring web developers.',
    
    'data-science': 'Introduction to data science covering statistics, Python libraries, data visualization, and machine learning basics. Learn to analyze data, create insights, and build predictive models. Includes real-world case studies and hands-on projects.',
    
    'machine-learning': 'Comprehensive guide to machine learning algorithms and applications. Covers supervised and unsupervised learning, neural networks, and deep learning. Includes Python implementations and practical examples. Perfect for data scientists and ML enthusiasts.',
    
    'django-guide': 'Master Django web framework with this comprehensive guide. Learn to build robust web applications, work with databases, implement authentication, and deploy to production. Includes best practices and real-world projects. Perfect for Python developers.',
    
    'office-chair': 'Ergonomic office chair designed for all-day comfort. Features adjustable height, lumbar support, breathable mesh back, and smooth-rolling casters. Durable construction with premium materials. Perfect for home offices or professional workspaces. Reduces back strain.',
    
    'desk-lamp': 'Modern LED desk lamp with adjustable brightness and color temperature. Energy-efficient with long-lasting LED bulbs. Features flexible arm, stable base, and touch controls. Perfect for reading, studying, or working. Eye-friendly lighting reduces strain.',
    
    'bookshelf': 'Sturdy wooden bookshelf with multiple shelves for books and decorative items. Classic design that complements any room decor. Easy to assemble with quality hardware included. Durable construction supports heavy books. Perfect for home libraries or offices.',
    
    'coffee-table': 'Modern coffee table with sleek design and sturdy construction. Features spacious tabletop and optional storage. Made from quality materials with smooth finish. Perfect centerpiece for living rooms. Easy to clean and maintain. Complements various decor styles.',
    
    'sofa': 'Comfortable 3-seater sofa with plush cushions and durable upholstery. Features solid wood frame, high-density foam, and elegant design. Perfect for living rooms or family spaces. Easy to maintain fabric. Provides excellent support and comfort for relaxation.',
    
    'running-shoes': 'Professional running shoes designed for performance and comfort. Features responsive cushioning, breathable mesh upper, and durable rubber outsole. Provides excellent support and shock absorption. Perfect for runners of all levels. Lightweight and flexible design.',
    
    'yoga-mat': 'Premium non-slip yoga mat with excellent cushioning and grip. Made from eco-friendly materials, durable and easy to clean. Features optimal thickness for comfort and stability. Perfect for yoga, pilates, stretching, or meditation. Includes carrying strap.',
    
    'dumbbell-set': 'Adjustable dumbbell set perfect for home workouts. Features quick-change weight system, comfortable grip handles, and compact design. Durable construction with quality materials. Ideal for strength training, toning, and building muscle. Space-saving solution.',
    
    'tennis-racket': 'Professional tennis racket designed for power and control. Features lightweight frame, comfortable grip, and optimal string tension. Suitable for intermediate to advanced players. Durable construction with premium materials. Enhances your game performance.',
    
    'basketball': 'Official size basketball with excellent grip and bounce. Made from durable composite leather with deep channels for better control. Suitable for indoor and outdoor play. Perfect for practice, games, or casual shooting. Maintains shape and performance over time.',
}

# Update products
updated_count = 0
for slug, description in descriptions.items():
    try:
        product = Product.objects.get(slug=slug)
        product.description = description
        product.save()
        print(f"Updated: {product.name}")
        updated_count += 1
    except Product.DoesNotExist:
        print(f"Product not found: {slug}")

print(f"\nTotal products updated: {updated_count}")
