# Generated by Django 3.2.12 on 2022-02-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-03-10'),
            preserve_default=False,
        ),
    ]
