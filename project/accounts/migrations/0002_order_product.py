# Generated by Django 4.2.3 on 2023-07-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('out for delvired', 'out for delvired'), ('delvired', 'delvired')], max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('indoor', 'indoor'), ('outdoor', 'outdoor')], max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]