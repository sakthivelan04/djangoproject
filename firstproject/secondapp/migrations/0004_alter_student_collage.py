# Generated by Django 4.2.17 on 2025-01-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0003_alter_student_collage_alter_student_register_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='collage',
            field=models.CharField(help_text='Enter your collage name', max_length=50),
        ),
    ]
