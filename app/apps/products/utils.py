from io import BytesIO
import json
import random
from django.core.files.images import ImageFile
from django.utils.text import slugify
import requests
from django.core.files.base import ContentFile
from PIL import Image as PillImage
from apps.categories.models import Category
from apps.products.models import Product


def import_products_from_json(name: str):
    with open(name, "r") as file:
        data = json.load(file)
    name = name.split('.')[0]
    category = Category(name=name, slug=slugify(name))
    category.save()
    for i, product_data in enumerate(data, 1):
        name = product_data["name"]
        price = product_data["price"]
        img_url = product_data["preimage"]
        stock = random.randint(0, 100)
        print(i)

        response = requests.get(img_url)
        if response.status_code == 200:
            image_content = BytesIO(response.content)
            image = PillImage.open(image_content)
            image_file = ImageFile(image_content)
            product = Product.objects.create(name=name, price=price, stock=12, category=category)
            product.photo.save(str(product.pk) + ".jpg", image_file, save=True)
            product.save()
        else:
            print(f"Failed to download image for product {name}")

name = "видеокарты.json"
import_products_from_json(name)
