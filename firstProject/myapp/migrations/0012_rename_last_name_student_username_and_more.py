# Generated by Django 4.2.8 on 2024-07-30 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_student_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
    ]
