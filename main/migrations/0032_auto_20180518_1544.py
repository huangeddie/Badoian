# Generated by Django 2.0.1 on 2018-05-18 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20180518_1511'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='meet',
            unique_together={('league', 'contest_index', 'start_year')},
        ),
    ]