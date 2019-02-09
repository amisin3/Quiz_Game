# Generated by Django 2.1.3 on 2019-01-08 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_question_right_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='right_ans',
        ),
        migrations.AddField(
            model_name='answer',
            name='right_ans',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='related_to',
        ),
        migrations.AddField(
            model_name='answer',
            name='related_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.Question'),
        ),
    ]