# Generated by Django 4.2.5 on 2023-10-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_audiofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='desc',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
