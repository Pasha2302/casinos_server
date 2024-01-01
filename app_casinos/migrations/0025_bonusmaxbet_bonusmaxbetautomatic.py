# Generated by Django 5.0 on 2024-01-01 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0024_alter_wageringcontributionvalue_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusMaxBet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Bonus Max Bet value')),
                ('selected_source', models.CharField(choices=[('undefined', 'Undefined'), ('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], default='', max_length=20)),
                ('bonus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='max_bet', to='app_casinos.bonus', to_field='slug')),
                ('symbol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bonus_max_bet', to='app_casinos.basecurrency')),
            ],
        ),
        migrations.CreateModel(
            name='BonusMaxBetAutomatic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automatic', models.BooleanField(default=False)),
                ('selected_source', models.CharField(choices=[('undefined', 'Undefined'), ('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], default='', max_length=20)),
                ('bonus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='max_bet_automatic', to='app_casinos.bonus', to_field='slug', unique=True)),
            ],
        ),
    ]