# Generated by Django 5.0 on 2024-01-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0040_alter_accountdata_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistercasino',
            name='casino',
        ),
        migrations.AddField(
            model_name='casino',
            name='sisters_casinos',
            field=models.ManyToManyField(related_name='casino', to='app_casinos.sistercasino'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='blocked_countries',
            field=models.ManyToManyField(help_text='List of restricted countries', related_name='casino', to='app_casinos.country'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='classic_currency',
            field=models.ManyToManyField(related_name='casino', to='app_casinos.classiccurrency'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='crypto_currencies',
            field=models.ManyToManyField(related_name='casino', to='app_casinos.cryptocurrency'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='game_providers',
            field=models.ManyToManyField(related_name='casino', to='app_casinos.provider'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='game_types',
            field=models.ManyToManyField(related_name='casino', to='app_casinos.gametype'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='games',
            field=models.ManyToManyField(related_name='casino', to='app_casinos.game'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='licenses',
            field=models.ManyToManyField(help_text='The license under which the casino operates', related_name='casino', to='app_casinos.licensingauthority'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='payment_methods',
            field=models.ManyToManyField(related_name='casino', to='app_casinos.paymentmethod'),
        ),
        migrations.AlterField(
            model_name='gametype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Game Type'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Provider Name'),
        ),
    ]