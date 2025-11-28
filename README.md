# E-commerce Website

A modern e-commerce website built with Django, HTML, CSS, and JavaScript. Features a Flipkart/Amazon-inspired design with full shopping cart functionality and user authentication.

## Features

- 🛍️ **Product Catalog**: Browse 29 products across 5 categories (Electronics, Clothing, Books, Furniture, Sports)
- 🛒 **Shopping Cart**: Add products, update quantities, and manage your cart
- 👤 **User Authentication**: Register and login functionality
- 🔍 **Category Filtering**: Filter products by category
- 💰 **Indian Rupee Currency**: Prices displayed in ₹
- 📱 **Responsive Design**: Modern UI that works on all devices
- 🖼️ **Product Images**: Real product images with detailed descriptions

## Tech Stack

- **Backend**: Django 5.2.8
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite3
- **Image Processing**: Pillow

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "ecommerce web"
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install django pillow
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
ecommerce web/
├── ecommerce_project/     # Main project settings
├── store/                 # Product catalog app
├── accounts/              # User authentication app
├── cart/                  # Shopping cart app
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── media/                 # User uploaded files
└── pictures/              # Product images
```

## Usage

### Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ to manage:
- Products and Categories
- User accounts
- Shopping carts

### Shopping
1. Browse products on the homepage
2. Filter by category using the sidebar
3. Click on a product to view details
4. Add products to cart
5. View and manage cart
6. Register/Login for checkout

## Database Population

To populate the database with sample products:
```bash
python populate_db.py
```

To update product descriptions:
```bash
python update_descriptions.py
```

## Screenshots

The website features:
- Modern product grid layout
- Detailed product pages with descriptions
- Functional shopping cart with quantity controls
- User authentication pages
- Category-based filtering

## License

This project is open source and available for educational purposes.

## Author

Created as a learning project for building e-commerce websites with Django.
