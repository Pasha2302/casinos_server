# Generated by Django 5.0 on 2024-01-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0044_casino_casino_rank_alter_bonusamount_selected_source_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='casino_rank',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Casino Rank'),
        ),
    ]
