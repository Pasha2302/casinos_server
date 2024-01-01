# Generated by Django 5.0 on 2023-12-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0006_alter_casino_classic_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='link',
            field=models.URLField(verbose_name='Bonus URL'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Bonus Name'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Bonus Slug'),
        ),
    ]