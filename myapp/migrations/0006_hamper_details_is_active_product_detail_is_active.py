# Generated by Django 5.0.1 on 2024-01-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_hamper_details_cat_id_delete_hamper_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamper_details',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]