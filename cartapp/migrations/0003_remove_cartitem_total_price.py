# Generated by Django 4.0.3 on 2022-03-25 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_cart_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total_price',
        ),
    ]