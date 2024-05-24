# Generated by Django 5.0 on 2024-05-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0067_alter_casino_live_chat_competence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusmaxbetautomatic',
            name='automatic',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='bonusmaxbetautomatic',
            name='selected_source',
            field=models.CharField(blank=True, choices=[('undefined', 'Undefined'), ('terms_and_conditions', 'Terms & Conditions'), ('support', 'Support'), ('website', 'Website'), ('common_sense', 'Common Sense')], default='', max_length=20),
        ),
    ]