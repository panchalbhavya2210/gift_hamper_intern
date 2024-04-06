# Generated by Django 5.0.1 on 2024-01-25 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_cart',
            name='Hamper_id',
        ),
        migrations.AddField(
            model_name='product_order',
            name='Hamper_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.hamper_details'),
        ),
    ]