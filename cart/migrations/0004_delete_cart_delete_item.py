# Generated by Django 4.1 on 2024-07-25 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_item_cart_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
