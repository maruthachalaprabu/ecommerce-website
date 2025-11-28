import os
import django
from django.test import Client
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

c = Client()
try:
    response = c.get('/')
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print("Response Content:")
        print(response.content.decode('utf-8'))
except Exception:
    traceback.print_exc()
