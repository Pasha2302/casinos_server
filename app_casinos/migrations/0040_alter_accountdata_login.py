# Generated by Django 5.0 on 2024-01-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0039_rename_using_vpn_casino_vpn_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdata',
            name='login',
            field=models.CharField(max_length=50, verbose_name='Login'),
        ),
    ]
