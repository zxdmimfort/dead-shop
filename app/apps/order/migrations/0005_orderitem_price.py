# Generated by Django 5.0.6 on 2024-07-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_order_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="price",
            field=models.FloatField(null=True),
        ),
    ]
