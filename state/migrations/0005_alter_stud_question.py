# Generated by Django 4.1.3 on 2022-11-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0004_remove_ques_contact_remove_ques_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='question',
            field=models.CharField(max_length=1000),
        ),
    ]