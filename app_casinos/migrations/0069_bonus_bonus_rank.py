# Generated by Django 5.0 on 2024-05-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0068_alter_bonusmaxbetautomatic_automatic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonus',
            name='bonus_rank',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, verbose_name='Bonus Rank'),
        ),
    ]