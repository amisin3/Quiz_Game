# Generated by Django 2.1.3 on 2019-01-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0007_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
