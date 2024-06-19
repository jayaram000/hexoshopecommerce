# Generated by Django 5.0 on 2024-06-16 07:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_address_payment_status'),
        ('ecommerce', '0006_alter_userprofile_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='delivery_status',
        ),
        migrations.RemoveField(
            model_name='address',
            name='no_of_items',
        ),
        migrations.RemoveField(
            model_name='address',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='address',
            name='ordered_date',
        ),
        migrations.RemoveField(
            model_name='address',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='address',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='address',
            name='product',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_items', models.IntegerField(default='#')),
                ('order_status', models.CharField(choices=[('placed', 'Order Placed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='placed', max_length=20)),
                ('payment_status', models.CharField(choices=[('cod', 'cash on delivery'), ('op', 'online payment')], default='pending', max_length=20)),
                ('delivery_status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('out_for_delivery', 'Out for Delivery'), ('delivered', 'Delivered')], default='pending', max_length=20)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('payment_id', models.CharField(default='#', max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]