# Generated by Django 4.2.5 on 2023-10-09 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_audiofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiofile',
            name='user',
        ),
    ]
