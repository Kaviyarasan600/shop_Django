# Generated by Django 4.2.13 on 2024-05-19 15:28

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_category_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pages.models.getfilename),
        ),
    ]
