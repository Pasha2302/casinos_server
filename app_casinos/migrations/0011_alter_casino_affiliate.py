# Generated by Django 5.0 on 2024-01-05 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0010_remove_affiliate_casino_casino_affiliate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='affiliate',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casino', to='app_casinos.affiliate'),
        ),
    ]
