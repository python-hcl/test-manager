# Generated by Django 2.1.dev20180322075356 on 2018-05-04 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0018_tempresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tempresponse',
            old_name='temp_response_question',
            new_name='choice_question',
        ),
        migrations.RenameField(
            model_name='tempresponse',
            old_name='temp_response_answer',
            new_name='choice_text',
        ),
        migrations.AddField(
            model_name='tempresponse',
            name='temp_response_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.Test'),
        ),
    ]
