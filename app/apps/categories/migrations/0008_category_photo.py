# Generated by Django 5.0.6 on 2024-06-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0007_alter_category_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="categories"),
        ),
    ]