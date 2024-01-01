# Generated by Django 5.0 on 2023-12-31 01:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0008_bonussubtype_bonustype_remove_bonus_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='bonus_subtypes',
            field=models.ManyToManyField(blank=True, null=True, related_name='bonus', to='app_casinos.bonussubtype'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Bonus URL'),
        ),
        migrations.CreateModel(
            name='BonusAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True, verbose_name='(CAP) value')),
                ('selected_source', models.CharField(choices=[('undefined', 'Undefined'), ('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website')], default='', max_length=20)),
                ('bonus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bonus_amount', to='app_casinos.bonus', to_field='slug')),
                ('symbol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bonus_amount_symbol', to='app_casinos.basecurrency')),
            ],
        ),
    ]
