# Generated by Django 3.1.7 on 2021-04-13 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20210413_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='folder_name',
        ),
    ]
