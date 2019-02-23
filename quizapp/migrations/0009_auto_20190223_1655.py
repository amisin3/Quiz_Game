# Generated by Django 2.1.3 on 2019-02-23 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizapp', '0008_answer_answer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_specific_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Answer')),
                ('user_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='user',
        ),
    ]