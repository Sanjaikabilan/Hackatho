# Generated by Django 4.1.3 on 2022-11-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0005_alter_stud_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud',
            name='answer',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
