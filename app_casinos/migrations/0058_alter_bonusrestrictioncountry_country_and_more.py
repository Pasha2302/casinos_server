# Generated by Django 5.0 on 2024-04-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0057_alter_promotionperiod_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusrestrictioncountry',
            name='country',
            field=models.ManyToManyField(blank=True, help_text="Pick countries that can't receive this bonus", null=True, related_name='bonus_restriction_country', to='app_casinos.country'),
        ),
        migrations.AlterField(
            model_name='bonusrestrictionrtpgame',
            name='value',
            field=models.FloatField(blank=True, help_text='Some slots are not allowed for bonus wagering due to high RTP', null=True, verbose_name='Games with RTP higher than %'),
        ),
    ]
