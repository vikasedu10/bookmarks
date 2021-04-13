# Generated by Django 3.1.7 on 2021-04-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_bookmark_folder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='folder',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='folder_name',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='homepage.Folder'),
        ),
    ]