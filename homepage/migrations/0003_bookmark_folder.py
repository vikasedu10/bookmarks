# Generated by Django 3.1.7 on 2021-04-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_bookmark_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='folder',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]