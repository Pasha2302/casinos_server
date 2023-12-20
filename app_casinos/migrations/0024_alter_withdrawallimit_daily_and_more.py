# Generated by Django 5.0 on 2023-12-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0023_alter_withdrawallimit_daily_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawallimit',
            name='daily',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawallimit',
            name='monthly',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawallimit',
            name='selected_source',
            field=models.CharField(blank=True, choices=[('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawallimit',
            name='weekly',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
