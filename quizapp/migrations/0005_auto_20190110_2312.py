# Generated by Django 2.1.3 on 2019-01-10 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_auto_20190109_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='related_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Question'),
        ),
    ]