# Generated by Django 4.2.3 on 2023-07-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile/default.png', null=True, upload_to='media/profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]