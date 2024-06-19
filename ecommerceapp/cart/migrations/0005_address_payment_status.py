# Generated by Django 5.0 on 2024-05-17 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_address_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='payment_status',
            field=models.CharField(choices=[('cod', 'cash on delivery'), ('op', 'online payment')], default='pending', max_length=20),
        ),
    ]