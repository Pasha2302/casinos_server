# Generated by Django 5.0 on 2023-12-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0007_alter_accountdata_log_alter_accountdata_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name Currency'),
        ),
    ]
