# Generated by Django 5.0 on 2023-12-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0033_alter_withdrawallimit_daily_and_more'),
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
            field=models.CharField(choices=[('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='withdrawallimit',
            name='weekly',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]