# Generated by Django 5.0 on 2024-01-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0045_alter_casino_casino_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='casino_rank',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, verbose_name='Casino Rank'),
        ),
    ]
