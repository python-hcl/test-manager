# Generated by Django 2.1.dev20180322075356 on 2018-05-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0020_testmapping_testmap_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmapping',
            name='testmap_complete',
        ),
        migrations.AddField(
            model_name='testmapping',
            name='testmap_status',
            field=models.IntegerField(default=0),
        ),
    ]
