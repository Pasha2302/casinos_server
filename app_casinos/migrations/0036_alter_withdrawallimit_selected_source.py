# Generated by Django 5.0 on 2023-12-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0035_alter_withdrawallimit_selected_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawallimit',
            name='selected_source',
            field=models.CharField(blank=True, choices=[('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], max_length=20, null=True),
        ),
    ]
