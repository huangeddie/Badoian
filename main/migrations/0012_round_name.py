# Generated by Django 2.0.1 on 2018-05-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180513_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='name',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]