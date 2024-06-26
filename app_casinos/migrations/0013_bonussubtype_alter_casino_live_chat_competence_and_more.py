# Generated by Django 5.0 on 2024-01-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0012_alter_bonusamount_options_alter_bonusmaxwin_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusSubtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Name Bonus Subtype')),
            ],
        ),
        migrations.AlterField(
            model_name='casino',
            name='live_chat_competence',
            field=models.CharField(choices=[('high_competence', 'High Competence'), ('above_average', 'Above Average'), ('average', 'Average'), ('below_average', 'Below Average'), ('incompetent', 'Incompetent')], default='High Competence', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bonus',
            name='bonus_subtypes',
            field=models.ManyToManyField(blank=True, related_name='bonus', to='app_casinos.bonussubtype'),
        ),
    ]
