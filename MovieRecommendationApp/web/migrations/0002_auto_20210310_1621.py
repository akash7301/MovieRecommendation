# Generated by Django 2.2.1 on 2021-03-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
