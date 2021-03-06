# Generated by Django 4.0.3 on 2022-03-14 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customer_address_alter_customer_phone_number_and_more'),
        ('store', '0002_alter_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='account.seller'),
        ),
    ]
