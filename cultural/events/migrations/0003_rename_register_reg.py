# Generated by Django 4.2.17 on 2025-02-09 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_register_email_alter_register_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='reg',
        ),
    ]
