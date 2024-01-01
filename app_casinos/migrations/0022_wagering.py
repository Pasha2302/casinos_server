# Generated by Django 5.0 on 2024-01-01 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0021_bonus_bonus_only_bonus_bonus_plus_deposit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wagering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tbwr', models.TextField(blank=True, null=True, verbose_name='Turnover bonus wagering requirement')),
                ('tbwe', models.TextField(blank=True, null=True, verbose_name='Turnover bonus wagering example')),
                ('selected_source', models.CharField(choices=[('undefined', 'Undefined'), ('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], default='', max_length=20)),
                ('bonus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wagering', to='app_casinos.bonus', to_field='slug', unique=True)),
            ],
        ),
    ]
