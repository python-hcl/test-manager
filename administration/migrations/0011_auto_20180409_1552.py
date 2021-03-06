# Generated by Django 2.1.dev20180322075356 on 2018-04-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0010_auto_20180409_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complexity',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='questionchoice',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='role',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='sectionmapping',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='test',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='testmapping',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='testsection',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
    ]
