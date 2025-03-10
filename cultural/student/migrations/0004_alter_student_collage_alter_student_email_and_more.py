# Generated by Django 4.2.17 on 2025-02-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_delete_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='collage',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='register_no',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
