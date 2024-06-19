# Generated by Django 5.0 on 2024-05-16 14:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('ecommerce', '0003_favo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('zip_code', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=50)),
                ('no_of_items', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('order_status', models.CharField(choices=[('placed', 'Order Placed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='placed', max_length=20)),
                ('delivery_status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('out_for_delivery', 'Out for Delivery'), ('delivered', 'Delivered')], default='pending', max_length=20)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
