# Generated by Django 5.0 on 2023-12-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0038_alter_mindep_selected_source_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawallimit',
            name='selected_source',
            field=models.CharField(choices=[('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website'), ('undefined', 'Undefined')], default='', max_length=20),
        ),
    ]