# Generated by Django 4.0.3 on 2022-03-26 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_customer__id_customer_state'),
        ('cartapp', '0003_remove_cartitem_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='account.customer'),
        ),
    ]
