# Generated by Django 5.0 on 2024-01-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0046_alter_casino_casino_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mindep',
            name='min_value',
            field=models.FloatField(null=True),
        ),
    ]