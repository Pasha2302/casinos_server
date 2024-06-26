# Generated by Django 5.0 on 2024-04-03 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0055_bonusamount_unlimited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusamount',
            name='symbol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bonus_amount_symbol', to='app_casinos.basecurrency'),
        ),
        migrations.AlterField(
            model_name='bonusamount',
            name='value',
            field=models.IntegerField(blank=True, help_text="The maximum bonus amount that the casino can match. Usually defined defined as: 'up to 200 EUR'", null=True, verbose_name='(CAP) value'),
        ),
    ]
