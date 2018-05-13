# Generated by Django 2.0.1 on 2018-05-13 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180513_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_time', models.DateTimeField()),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Round')),
            ],
        ),
    ]