# Generated by Django 4.0.3 on 2023-04-09 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_cart_created_at_cart_product_cart_quantity_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
