from io import BytesIO
import json
import os
import random
from django.core.files.images import ImageFile
import requests
from PIL import Image as PillImage
from apps.categories.models import Category
from apps.products.models import Product
from unidecode import unidecode


def import_products_from_json(name: str):
    with open(name, "r") as file:
        data = json.load(file)
    name = name.split(".")[0]
    category = Category(name=name, slug=unidecode(name))
    print(category, category.slug)
    category.save()
    for i, product_data in enumerate(data, 1):
        name = product_data["name"][:295] + "..."
        price = product_data["price"]
        img_url = product_data["preimage"]
        stock = random.randint(0, 100)
        print(i)

        response = requests.get(img_url)
        if response.status_code == 200:
            image_content = BytesIO(response.content)
            image = PillImage.open(image_content) # noqa:F841
            image_file = ImageFile(image_content)
            product = Product.objects.create(
                name=name, price=price, stock=stock, category=category
            )
            product.photo.save(str(product.pk) + ".jpg", image_file, save=True)
            product.save()
        else:
            print(f"Failed to download image for product {name}")


# import_products_from_json(name)
files = os.listdir()
for file in files:
    if file.endswith(".json"):
        print(f"--------{file}------")
        import_products_from_json(file)
