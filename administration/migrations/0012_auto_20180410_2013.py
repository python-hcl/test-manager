# Generated by Django 2.1.dev20180322075356 on 2018-04-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0011_auto_20180409_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complexity',
            name='complex_name',
            field=models.CharField(max_length=250),
        ),
    ]