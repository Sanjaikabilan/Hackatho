# Generated by Django 4.1.3 on 2022-11-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0002_alter_state_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('question', models.CharField(max_length=1000)),
            ],
        ),
    ]
