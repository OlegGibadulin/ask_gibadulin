# Generated by Django 3.0.5 on 2020-04-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerManager',
        ),
        migrations.DeleteModel(
            name='QuestionManager',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='is_published',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='is_published',
            new_name='is_active',
        ),
    ]
