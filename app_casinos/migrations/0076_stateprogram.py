# Generated by Django 5.0 on 2024-05-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0075_alter_bonus_game_providers'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True)),
                ('data', models.JSONField()),
                ('start_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'State Program',
                'verbose_name_plural': 'State Programs',
                'ordering': ['id'],
            },
        ),
    ]
