# Generated by Django 4.2.17 on 2025-01-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='Enter your name', max_length=20)),
                ('register_no', models.IntegerField(help_text='Enter your register number', unique=True)),
                ('email', models.EmailField(help_text='Enter a valid email address', max_length=50, unique=True)),
                ('collage', models.CharField(help_text='Enter your collage name', max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
