# Generated by Django 5.0 on 2023-12-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0009_alter_accountdata_casino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdata',
            name='log',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='Login'),
        ),
    ]
