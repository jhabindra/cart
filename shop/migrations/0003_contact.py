# Generated by Django 4.2.3 on 2023-08-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_product_category_product_image_product_price_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("msg_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("emial", models.CharField(default="", max_length=50)),
                ("phone", models.CharField(default="", max_length=10)),
                ("addres", models.CharField(default="", max_length=100)),
                ("desc", models.CharField(default="", max_length=500)),
            ],
        ),
    ]
