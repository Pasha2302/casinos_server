# Generated by Django 5.0 on 2023-12-20 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0012_alter_accountdata_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountdata',
            options={'ordering': ['log'], 'verbose_name': 'Account Data', 'verbose_name_plural': 'Account Data'},
        ),
    ]