# Generated by Django 5.0 on 2024-05-13 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0070_loyaltyprogram_loyalty_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotsWageringContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Wagering Contribution value %')),
                ('bonus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slots_wagering', to='app_casinos.bonus', to_field='slug')),
                ('slot', models.ManyToManyField(related_name='bonus_slots_wagering', to='app_casinos.game')),
            ],
        ),
    ]
