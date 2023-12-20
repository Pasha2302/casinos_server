# Generated by Django 5.0 on 2023-12-20 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0028_alter_withdrawallimit_daily_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawallimit',
            name='casino',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='withdrawal_limit', to='app_casinos.casino'),
        ),
    ]
