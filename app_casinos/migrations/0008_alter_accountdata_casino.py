# Generated by Django 5.0 on 2023-12-23 00:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0007_alter_accountdata_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdata',
            name='casino',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='account_data', to='app_casinos.casino', to_field='slug'),
        ),
    ]
