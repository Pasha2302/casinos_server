# Generated by Django 5.0 on 2023-12-20 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0032_country_name3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawallimit',
            name='daily',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='withdrawallimit',
            name='monthly',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='withdrawallimit',
            name='selected_source',
            field=models.CharField(choices=[('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawallimit',
            name='weekly',
            field=models.IntegerField(null=True),
        ),
    ]