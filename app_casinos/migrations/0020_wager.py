# Generated by Django 5.0 on 2023-12-31 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0019_bonusslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True, verbose_name='Wager value')),
                ('selected_source', models.CharField(choices=[('undefined', 'Undefined'), ('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], default='', max_length=20)),
                ('bonus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wager', to='app_casinos.bonus', to_field='slug', unique=True)),
            ],
        ),
    ]