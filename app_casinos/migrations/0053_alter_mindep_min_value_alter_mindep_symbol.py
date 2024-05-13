# Generated by Django 5.0 on 2024-01-29 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0052_alter_gametype_options_mindep_unlimited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mindep',
            name='min_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mindep',
            name='symbol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='min_dip_symbol', to='app_casinos.basecurrency'),
        ),
    ]