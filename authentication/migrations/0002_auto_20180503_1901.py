# Generated by Django 2.0.5 on 2018-05-03 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NetworkConfig',
            new_name='NetworkType',
        ),
    ]
