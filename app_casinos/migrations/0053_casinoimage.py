# Generated by Django 5.0 on 2023-12-21 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0052_casino_affiliate_program_casino_link_affiliate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasinoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='casino_images/', verbose_name='Casino Image')),
                ('casino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app_casinos.casino')),
            ],
        ),
    ]