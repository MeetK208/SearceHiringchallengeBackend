# Generated by Django 5.1.1 on 2024-09-13 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectcard', '0006_remove_project_lasteditedbyuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='last_updated_timestamp',
        ),
    ]
