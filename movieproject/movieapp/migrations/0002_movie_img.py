# Generated by Django 3.2.11 on 2022-02-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='gfs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
