# Generated by Django 5.0 on 2024-06-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_alter_userprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='images/users'),
        ),
    ]
