# Generated by Django 5.0 on 2024-01-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0019_alter_bonus_days_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayofweek',
            name='day',
            field=models.CharField(default=None, max_length=10, verbose_name='Day'),
        ),
    ]
