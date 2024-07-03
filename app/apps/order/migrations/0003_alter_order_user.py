# Generated by Django 5.0.6 on 2024-07-03 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_initial"),
        ("users", "0002_userproxy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.userproxy"
            ),
        ),
    ]
