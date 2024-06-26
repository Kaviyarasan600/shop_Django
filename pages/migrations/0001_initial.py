# Generated by Django 4.2.13 on 2024-05-19 09:46

from django.db import migrations, models
import django.db.models.deletion
import pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=pages.models.getfilename)),
                ('status', models.BooleanField(default=False, help_text='0-show, 1-Hidden')),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=pages.models.getfilename)),
                ('status', models.BooleanField(default=False, help_text='0-show, 1-Hidden')),
                ('created_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('old_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=pages.models.getfilename)),
                ('description', models.TextField(max_length=500)),
                ('highlight', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show, 1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default, 1-Trending')),
                ('created_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.subcategory')),
            ],
        ),
    ]
