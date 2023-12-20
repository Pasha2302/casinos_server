# Generated by Django 5.0 on 2023-12-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0016_alter_casino_link_loyalty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minwagering',
            name='min_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='minwagering',
            name='selected_source',
            field=models.CharField(choices=[('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], max_length=20, null=True),
        ),
    ]