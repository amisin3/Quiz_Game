# Generated by Django 2.1.3 on 2019-01-09 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_auto_20190109_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='answer_text',
        ),
    ]
