# Generated by Django 5.0 on 2023-12-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0054_alter_casinoimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casinoimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='casino_images/', verbose_name='Casino Image'),
        ),
    ]
